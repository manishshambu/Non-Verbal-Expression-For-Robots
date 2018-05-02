from __future__ import print_function, division, unicode_literals

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

import io
import os
import sys

sys.path.insert(0, "/Users/anuj/coursework_cuboulder/spring_2018/algo_hri/torchMoji-master")

import json
import csv
import numpy as np

from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis
from torchmoji.global_variables import PRETRAINED_PATH, VOCAB_PATH

import subprocess

from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.silence import detect_nonsilent, detect_silence

import pickle

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import LSTM
from keras import backend as K

import time

# google speech-to-text and prosody extraction require mono audio input
def convert_audio_to_mono(data_folder):
    output_filename = data_folder + 'mono_myrecording.wav'
    command = ['sox', data_folder + 'myrecording.wav', '-c', '1', output_filename] 
    subprocess.Popen(command)
    
    time.sleep(2)  # subprocess takes time!
    
    return output_filename

# relative to torso, so torso x,y,z is always 0,0,0
def get_relative_joint_positions(data_folder):
    # read in joint coordinates json
    # all values in this json are defined in the kinect camera frame
    def get_skeleton_dict(data_folder):
        filename = data_folder + 'realWorldCoords.json'
        json_contents = json.load(open(filename))
        return json_contents

    skeletal_data = get_skeleton_dict(data_folder)
    output = []
    for frame in skeletal_data:
        d = {}
        x_orig_torso, y_orig_torso, z_orig_torso = frame['torso'].split(',')
        x_orig_torso, y_orig_torso, z_orig_torso = float(x_orig_torso[1:]), float(y_orig_torso), float(z_orig_torso[:-1])
        for joint, position in frame.items():
            if joint == 'time_ms':
                d[joint] = position
                continue
            if joint not in d.keys():
                d[joint] = []
            x_orig, y_orig, z_orig = position.split(',')
            x_orig, y_orig, z_orig = float(x_orig[1:]), float(y_orig), float(z_orig[:-1])
            d[joint] = [x_orig - x_orig_torso, y_orig - y_orig_torso, z_orig - z_orig_torso]
        output.append(d)
    return output

def get_prosody_features_from_audio(audio_filename):
    name = audio_filename.split('/')[-1].split('.wav')[0]
    command = 'python /Users/anuj/coursework_cuboulder/spring_2018/algo_hri/DisVoice-master/prosody/prosody.py \"'+audio_filename+'\" \"'+'/'.join(audio_filename.split('/')[:-1])+'/'+'prosody_'+ name+'.txt\" "static" "false"'
    subprocess.call(command, shell=True)
    
    time.sleep(2)  # subprocess takes time!
    
    return command.split('"')[-6]

def get_text_from_speech(audio_filename):
    # https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/speech/cloud-client/transcribe_async.py
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_creds.json"

    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    with io.open(audio_filename, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(language_code='en-US')

    # Detects speech in the audio file
    text = ''
    response = client.recognize(config, audio)
    if len(response.results) != 0:
        text = response.results[0].alternatives[0].transcript
    a = audio_filename.split('/')
    filename = '/'+'/'.join(a[1:-1])+'/text_'+a[-1].split('.wav')[0]+'.txt'
    with open(filename, 'w') as f:
        f.write(text)
    
    return text

def get_emotion_features_from_text(text, audio_filename):
    # https://github.com/huggingface/torchMoji/blob/master/examples/score_texts_emojis.py
    
    if text == '':
        emoji_ids = []
        one_hot_encodings = []
    else:
        text = [text]
        def top_elements(array, k):
            ind = np.argpartition(array, -k)[-k:]
            return ind[np.argsort(array[ind])][::-1]

        maxlen = 30

        with open(VOCAB_PATH, 'r') as f:
            vocabulary = json.load(f)

        st = SentenceTokenizer(vocabulary, maxlen)

        model = torchmoji_emojis(PRETRAINED_PATH)
        tokenized, _, _ = st.tokenize_sentences(text)
        prob = model(tokenized)

        for prob in [prob]:
            # Find top emojis for each sentence. Emoji ids (0-63)
            # correspond to the mapping in emoji_overview.png
            # at the root of the torchMoji repo.
            scores = []
            for i, t in enumerate(text):
                t_tokens = tokenized[i]
                t_score = [t]
                t_prob = prob[i]
                ind_top = top_elements(t_prob, 5)
                t_score.append(sum(t_prob[ind_top]))
                t_score.extend(ind_top)
                t_score.extend([t_prob[ind] for ind in ind_top])
                scores.append(t_score)

        emoji_ids = scores[0][2:2+5]
        one_hot_encodings = []
        for emoji_idx in emoji_ids:
            one_hot_encodings.append([0 if i!=emoji_idx else 1 for i in range(64)])
            
    a = audio_filename.split('/')
    
    filename = '/'+'/'.join(a[1:-1])+'/onehot_emotion_'+a[-1].split('.wav')[0]+'.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(one_hot_encodings, f)
        
    filename = '/'+'/'.join(a[1:-1])+'/emoji_ids_'+a[-1].split('.wav')[0]+'.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(emoji_ids, f)

    return emoji_ids, one_hot_encodings
