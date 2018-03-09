# Non-Verbal-Expression-For-Robots


Prosody Extraction using pyAudioAnalysis library

a. Extracting all speech features into a csv file.
python audioAnalysis.py featureExtractionFile -i data/speech_music_sample.wav -mw 1.0 -ms 1.0 -sw 0.050 -ss 0.050 -o data/speech_music_sample.wav


b. Extracting all speech features for a set of wav files (Batch mode.)
python audioAnalysis.py  featureExtractionDir -i data/ -mw 1.0 -ms 1.0 -sw 0.050 -ss 0.050

c. Beat extraction
python audioAnalysis.py beatExtraction -i data/beat/small.wav --plot

Reference - https://github.com/tyiannak/pyAudioAnalysis

