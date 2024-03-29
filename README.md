# ColorTranscribe
a python script for transcribing audio files using dedicated AI Models
and then changing the color of the transcribed text based on the language spoken

type python .\Transcribe3in1.py (after downloading the whole project) into your CMD after travelling to this project's folder
to see all three transcription methods based on provided samples (they're kinda big, so maybe I'l add them later)

each method can be called separately by replacing Transcribe3in1.py with a given counterpart
(TranscribeGoogleCloud.py, TranscribeAssembly.py, TranscribeWhisper.py)
(be sure to uncomment out the functions at the bottom for them to work)

OR you could try to put your own .mp3, .wav or .flac file 
and get transcriptions for those with the .\TranscribeUserInput command
(be sure to leave the bottom functions commented out for THIS to work)

# AI Models used for this project:

AssemblyAI - https://github.com/AssemblyAI/cookbook

Google Cloud Speech-To-Text API - https://cloud.google.com/speech-to-text

Whisper by OpenAI - https://huggingface.co/openai/whisper-small; https://github.com/openai/whisper

# other Python AI projects I might have taken inspiration from:

custom language detection in Whisper (in case you want proper probability display for detected languages) - https://discuss.huggingface.co/t/language-detection-with-whisper/26003/2

language detection in Google Cloud STT - https://cloud.google.com/speech-to-text/docs/enable-language-recognition-speech-to-text#speech_transcribe_multilanguage_beta-python

metric calculation method taken from this paper from the Lviv Polytechnic National University by Leslav Kobylyukh, Zoriana Rybchak and Oleh Basystiuk - https://ceur-ws.org/Vol-3396/paper18.pdf (it's really basic, but still wanna credit regardless)

very slight inspiration from abhishekag03 for the conversion script - https://github.com/abhishekag03/mp3toflac/blob/master/mp3toflac.py

all written with the help of the PyCharm IDE by Jetbrains.

subtitle text files taken with the use of https://downsub.com/ .
