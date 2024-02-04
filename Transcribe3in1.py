import Constants
from TranscribeAssembly import lang_handler, transcribe
from TranscribeGoogleCloud import color_transcribe_file_with_multilanguage_gcs
from TranscribeWhisper import lang_whandler, pipe, transcribe_and_detect

# sample .flac files from Google Cloud
flac1 = Constants.GOOG_URI1
flac2 = Constants.GOOG_URI2
flac3 = Constants.GOOG_URI3

# sample file paths
wav1 = Constants.SAMPLE_URL1
wav2 = Constants.SAMPLE_URL2
wav3 = Constants.SAMPLE_URL3

lang_handler(transcribe(wav1))
color_transcribe_file_with_multilanguage_gcs(flac1)
lang_whandler(pipe(wav1))

# lang_handler(transcribe(wav2))
# color_transcribe_file_with_multilanguage_gcs(flac2)
# lang_whandler(pipe(wav2))

# lang_handler(transcribe(wav3))
# color_transcribe_file_with_multilanguage_gcs(flac3)
# lang_whandler(pipe(wav3))
