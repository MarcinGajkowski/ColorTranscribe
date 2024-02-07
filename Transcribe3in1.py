import Constants
from TranscribeAssembly import lang_handler
from TranscribeGoogleCloud import color_transcribe_file_with_multilanguage_gcs
from TranscribeWhisper import lang_whandler
from MetricChecker import calculate_metrics_rawlings, calculate_metrics_italiano
from MetricChecker import calculate_metrics_scott_en, calculate_metrics_scott_fr, calculate_metrics_scott_pt


# .flac file paths
flac1 = Constants.FLAC_URL1
flac2 = Constants.FLAC_URL2
flac3 = Constants.FLAC_TOM1
flac4 = Constants.FLAC_TOM2
flac5 = Constants.FLAC_TOM3

# sample .flac files from Google Cloud
g_flac1 = Constants.GOOG_URI1
g_flac2 = Constants.GOOG_URI2
g_flac3 = Constants.GOOG_TOM1
g_flac4 = Constants.GOOG_TOM2
g_flac5 = Constants.GOOG_TOM3

# sample file paths
wav1 = Constants.SAMPLE_URL1
wav2 = Constants.SAMPLE_URL2
wav3 = Constants.SAMPLE_TOM1
wav4 = Constants.SAMPLE_TOM2
wav5 = Constants.SAMPLE_TOM3


# transcripts for polyglotSample.wav/flac
rawlings_assembly = lang_handler(wav1)
rawlings_google = color_transcribe_file_with_multilanguage_gcs(flac1)
rawlings_whisper = lang_whandler(wav1)

# metrics for transcribing the Mark Rawlings video
assembly_precision, assembly_recall, assembly_f1_score = calculate_metrics_rawlings(rawlings_assembly)
print("AssemblyAI Speech-to-Text: Precision={}, Recall={}, F1 Score = {}"
      .format(assembly_precision, assembly_recall, assembly_f1_score))

google_precision, google_recall, google_f1_score = calculate_metrics_rawlings(rawlings_google)
print("Google Cloud Transcribe: Precision={}, Recall={}, F1 Score={}"
      .format(google_precision, google_recall, google_f1_score))

whisper_precision, whisper_recall, whisper_f1_score = calculate_metrics_rawlings(rawlings_whisper)
print("Whisper (small): Precision={}, Recall={}, F1 Score = {}"
      .format(whisper_precision, whisper_recall, whisper_f1_score))


# transcripts for ItalianPolyglot.wav/flac
italiano_assembly = lang_handler(wav2)
italiano_google = color_transcribe_file_with_multilanguage_gcs(flac2)
italiano_whisper = lang_whandler(wav2)

# metrics for transcribing the Italian Polyglot video
assembly_precision, assembly_recall, assembly_f1_score = calculate_metrics_italiano(italiano_assembly)
print("AssemblyAI Speech-to-Text: Precision={}, Recall={}, F1 Score = {}"
      .format(assembly_precision, assembly_recall, assembly_f1_score))

google_precision, google_recall, google_f1_score = calculate_metrics_italiano(italiano_google)
print("Google Cloud Transcribe: Precision={}, Recall={}, F1 Score={}"
      .format(google_precision, google_recall, google_f1_score))

whisper_precision, whisper_recall, whisper_f1_score = calculate_metrics_italiano(italiano_whisper)
print("Whisper (small): Precision={}, Recall={}, F1 Score = {}"
      .format(whisper_precision, whisper_recall, whisper_f1_score))


# transcripts for the English Tom Scott .wav/.flac files
scott_en_assembly = lang_handler(wav3)
scott_en_google = color_transcribe_file_with_multilanguage_gcs(flac3)
scott_en_whisper = lang_whandler(wav3)

# metrics for transcribing the English dub of the Tom Scott video
assembly_precision, assembly_recall, assembly_f1_score = calculate_metrics_scott_en(scott_en_assembly)
print("AssemblyAI Speech-to-Text: Precision={}, Recall={}, F1 Score = {}"
      .format(assembly_precision, assembly_recall, assembly_f1_score))

google_precision, google_recall, google_f1_score = calculate_metrics_scott_en(scott_en_google)
print("Google Cloud Transcribe: Precision={}, Recall={}, F1 Score={}"
      .format(google_precision, google_recall, google_f1_score))

whisper_precision, whisper_recall, whisper_f1_score = calculate_metrics_scott_en(scott_en_whisper)
print("Whisper (small): Precision={}, Recall={}, F1 Score = {}"
      .format(whisper_precision, whisper_recall, whisper_f1_score))


# transcripts for the French Tom Scott .wav/.flac files
scott_fr_assembly = lang_handler(wav4)
scott_fr_google = color_transcribe_file_with_multilanguage_gcs(flac4)
scott_fr_whisper = lang_whandler(wav4)

# metrics for transcribing the French dub of the Tom Scott video
assembly_precision, assembly_recall, assembly_f1_score = calculate_metrics_scott_fr(scott_fr_assembly)
print("AssemblyAI Speech-to-Text: Precision={}, Recall={}, F1 Score = {}"
      .format(assembly_precision, assembly_recall, assembly_f1_score))

google_precision, google_recall, google_f1_score = calculate_metrics_scott_fr(scott_fr_google)
print("Google Cloud Transcribe: Precision={}, Recall={}, F1 Score={}"
      .format(google_precision, google_recall, google_f1_score))

whisper_precision, whisper_recall, whisper_f1_score = calculate_metrics_scott_fr(scott_fr_whisper)
print("Whisper (small): Precision={}, Recall={}, F1 Score = {}"
      .format(whisper_precision, whisper_recall, whisper_f1_score))


# transcripts for the French Tom Scott .wav/.flac files
scott_pt_assembly = lang_handler(wav5)
scott_pt_google = color_transcribe_file_with_multilanguage_gcs(flac5)
scott_pt_whisper = lang_whandler(wav5)

# metrics for transcribing the French dub of the Tom Scott video
assembly_precision, assembly_recall, assembly_f1_score = calculate_metrics_scott_pt(scott_pt_assembly)
print("AssemblyAI Speech-to-Text: Precision={}, Recall={}, F1 Score = {}"
      .format(assembly_precision, assembly_recall, assembly_f1_score))

google_precision, google_recall, google_f1_score = calculate_metrics_scott_pt(scott_pt_google)
print("Google Cloud Transcribe: Precision={}, Recall={}, F1 Score={}"
      .format(google_precision, google_recall, google_f1_score))

whisper_precision, whisper_recall, whisper_f1_score = calculate_metrics_scott_pt(scott_pt_whisper)
print("Whisper (small): Precision={}, Recall={}, F1 Score = {}"
      .format(whisper_precision, whisper_recall, whisper_f1_score))
