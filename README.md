# Non-Verbal-Expression-For-Robots


Prosody Extraction using pyAudioAnalysis library

a. python audioAnalysis.py featureExtractionFile -i data/speech_music_sample.wav -mw 1.0 -ms 1.0 -sw 0.050 -ss 0.050 -o data/speech_music_sample.wav
To extract all speech features into a csv file.

b. python audioAnalysis.py  featureExtractionDir -i data/ -mw 1.0 -ms 1.0 -sw 0.050 -ss 0.050
To extract all speech features for a set of wav files (Batch mode.)

c. Reference - https://github.com/tyiannak/pyAudioAnalysis

