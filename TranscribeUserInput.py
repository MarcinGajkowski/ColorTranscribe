import os
from pydub import AudioSegment
from TranscribeAssembly import lang_handler
# from TranscribeGoogleCloud import color_transcribe_file_with_multilanguage_gcs
from TranscribeWhisper import lang_whandler


def convert_if_necessary_then_transcribe():
    file_path = input("Enter file path to your audio file here "
                      "(Shift + Right Click -> Copy as Path on the file if you need to!) "
                      "(Don't forget to delete the quotation marks!): ")
    print(file_path)
    # check if path exists
    if os.path.exists(file_path):
        flac = file_path[:-4] + ".flac"

        # check file format
        if file_path.endswith(".mp3"):

            # handle .mp3 file - convert to .wav
            wav = file_path[:-4] + ".wav"
            if os.path.isfile(wav):
                print('File ' + wav + ' already exists')
            else:
                sound = AudioSegment.from_mp3(file_path)
                sound.export(wav, format="wav")
                print("Converted into a .wav file")

            # handle .mp3 file - convert to .flac with proper sampling rate for Whisper
            if os.path.isfile(flac):
                print('File ' + flac + ' already exists')
            else:
                sound = AudioSegment.from_mp3(file_path)
                sound.export(flac, format="flac")
                print("Converted into a .flac file.")

            # run transcriptions
            print("OK! Your files should be ready to be transcribed.")
            lang_handler(wav)
            lang_whandler(flac)

        # handle .wav file - convert to .flac with proper sampling rate for Whisper
        if file_path.endswith(".wav"):
            if os.path.isfile(flac):
                print('File ' + flac + ' already exists')
            else:
                sound = AudioSegment.from_wav(file_path)
                sound.export(flac, format="flac")
                print("Converted into a .flac file.")

            # run transcriptions
            print("OK! Your files should be ready to be transcribed.")
            lang_handler(file_path)
            lang_whandler(flac)

        # handle .flac file - change sampling rate and convert to .wav
        if file_path.endswith(".flac"):
            re_flac = AudioSegment.from_file(file_path, frame_rate=16000)
            re_flac.export(file_path, format='flac')
            print("Changed sampling rate of the .flac file (just in case)")
            wav = file_path[:-5] + ".wav"
            re_flac.export(wav, format='wav')
            print("Converted into a .wav file")

            # run transcriptions
            print("OK! Your files should be ready to be transcribed.")
            lang_handler(wav)
            lang_whandler(file_path)

    else:
        print("The given path doesn't lead to any file.")


convert_if_necessary_then_transcribe()
