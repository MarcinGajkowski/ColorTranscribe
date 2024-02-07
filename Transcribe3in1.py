import Constants
from TranscribeAssembly import lang_handler
from TranscribeGoogleCloud import color_transcribe_file_with_multilanguage_gcs
from TranscribeWhisper import lang_whandler
from MetricChecker import calculate_metrics_rawlings, calculate_metrics_italiano
from MetricChecker import calculate_metrics_scott_en, calculate_metrics_scott_fr, calculate_metrics_scott_pt
import MetricsStorage as metrics

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
rawlings_google = color_transcribe_file_with_multilanguage_gcs(g_flac1)
rawlings_whisper = lang_whandler(flac1)

# word and sentence totals (used for weighing averages)
rawlings_word_total = len(metrics.rawlings_all_words)
rawlings_sent_total = len(metrics.truth_rawlings)

italiano_word_total = len(metrics.italiano_all_words)
italiano_sent_total = len(metrics.truth_italiano)

scott_en_word_total = len(metrics.scott_en_all_words)
scott_en_sent_total = len(metrics.truth_scott_en)

scott_fr_word_total = len(metrics.scott_fr_all_words)
scott_fr_sent_total = len(metrics.truth_scott_fr)

scott_pt_word_total = len(metrics.scott_pt_all_words)
scott_pt_sent_total = len(metrics.truth_scott_pt)

# metrics for transcribing the Mark Rawlings video
assembly_wer1, assembly_precision1, assembly_recall1, assembly_f1_score1 = calculate_metrics_rawlings(rawlings_assembly)
print("AssemblyAI Speech-to-Text: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(assembly_wer1, assembly_precision1, assembly_recall1, assembly_f1_score1))

google_wer1, google_precision1, google_recall1, google_f1_score1 = calculate_metrics_rawlings(rawlings_google)
print("Google Cloud Transcribe: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(google_wer1, google_precision1, google_recall1, google_f1_score1))

whisper_wer1, whisper_precision1, whisper_recall1, whisper_f1_score1 = calculate_metrics_rawlings(rawlings_whisper)
print("Whisper (small): WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(whisper_wer1, whisper_precision1, whisper_recall1, whisper_f1_score1))

# transcripts for ItalianPolyglot.wav/flac
italiano_assembly = lang_handler(wav2)
italiano_google = color_transcribe_file_with_multilanguage_gcs(g_flac2)
italiano_whisper = lang_whandler(flac2)

# metrics for transcribing the Italian Polyglot video
assembly_wer2, assembly_precision2, assembly_recall2, assembly_f1_score2 = calculate_metrics_italiano(italiano_assembly)
print("AssemblyAI Speech-to-Text: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(assembly_wer2, assembly_precision2, assembly_recall2, assembly_f1_score2))

google_wer2, google_precision2, google_recall2, google_f1_score2 = calculate_metrics_italiano(italiano_google)
print("Google Cloud Transcribe: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(google_wer2, google_precision2, google_recall2, google_f1_score2))

whisper_wer2, whisper_precision2, whisper_recall2, whisper_f1_score2 = calculate_metrics_italiano(italiano_whisper)
print("Whisper (small): WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(whisper_wer2, whisper_precision2, whisper_recall2, whisper_f1_score2))

# transcripts for the English Tom Scott .wav/.flac files
scott_en_assembly = lang_handler(wav3)
scott_en_google = color_transcribe_file_with_multilanguage_gcs(g_flac3)
scott_en_whisper = lang_whandler(flac3)

# metrics for transcribing the English dub of the Tom Scott video
assembly_wer3, assembly_precision3, assembly_recall3, assembly_f1_score3 = calculate_metrics_scott_en(scott_en_assembly)
print("AssemblyAI Speech-to-Text: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(assembly_wer3, assembly_precision3, assembly_recall3, assembly_f1_score3))

google_wer3, google_precision3, google_recall3, google_f1_score3 = calculate_metrics_scott_en(scott_en_google)
print("Google Cloud Transcribe: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(google_wer3, google_precision3, google_recall3, google_f1_score3))

whisper_wer3, whisper_precision3, whisper_recall3, whisper_f1_score3 = calculate_metrics_scott_en(scott_en_whisper)
print("Whisper (small): WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(whisper_wer3, whisper_precision3, whisper_recall3, whisper_f1_score3))

# transcripts for the French Tom Scott .wav/.flac files
scott_fr_assembly = lang_handler(wav4)
scott_fr_google = color_transcribe_file_with_multilanguage_gcs(g_flac4)
scott_fr_whisper = lang_whandler(flac4)

# metrics for transcribing the French dub of the Tom Scott video
assembly_wer4, assembly_precision4, assembly_recall4, assembly_f1_score4 = calculate_metrics_scott_fr(scott_fr_assembly)
print("AssemblyAI Speech-to-Text: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(assembly_wer4, assembly_precision4, assembly_recall4, assembly_f1_score4))

google_wer4, google_precision4, google_recall4, google_f1_score4 = calculate_metrics_scott_fr(scott_fr_google)
print("Google Cloud Transcribe: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(google_wer4, google_precision4, google_recall4, google_f1_score4))

whisper_wer4, whisper_precision4, whisper_recall4, whisper_f1_score4 = calculate_metrics_scott_fr(scott_fr_whisper)
print("Whisper (small): WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(whisper_wer4, whisper_precision4, whisper_recall4, whisper_f1_score4))

# transcripts for the Brazilian Portuguese Tom Scott .wav/.flac files
scott_pt_assembly = lang_handler(wav5)
scott_pt_google = color_transcribe_file_with_multilanguage_gcs(g_flac5)
scott_pt_whisper = lang_whandler(flac5)

# metrics for transcribing the Portuguese dub of the Tom Scott video
assembly_wer5, assembly_precision5, assembly_recall5, assembly_f1_score5 = calculate_metrics_scott_pt(scott_pt_assembly)
print("AssemblyAI Speech-to-Text: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(assembly_wer5, assembly_precision5, assembly_recall5, assembly_f1_score5))

google_wer5, google_precision5, google_recall5, google_f1_score5 = calculate_metrics_scott_pt(scott_pt_google)
print("Google Cloud Transcribe: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(google_wer5, google_precision5, google_recall5, google_f1_score5))

whisper_wer5, whisper_precision5, whisper_recall5, whisper_f1_score5 = calculate_metrics_scott_pt(scott_pt_whisper)
print("Whisper (small): WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(whisper_wer5, whisper_precision5, whisper_recall5, whisper_f1_score5))

# calculate weighted averages for every metric

# Word Error Rate
assembly_wer_avg = (rawlings_word_total * assembly_wer1 + italiano_word_total * assembly_wer2
                    + scott_en_word_total * assembly_wer3 + scott_fr_sent_total * assembly_wer4
                    + scott_pt_word_total * assembly_wer5) \
                   / (rawlings_word_total + italiano_word_total + italiano_word_total +
                      scott_fr_word_total + scott_pt_word_total)

google_wer_avg = (rawlings_word_total * google_wer1 + italiano_word_total * google_wer2
                  + scott_en_word_total * google_wer3 + scott_fr_sent_total * google_wer4
                  + scott_pt_word_total * google_wer5) \
                 / (rawlings_word_total + italiano_word_total + italiano_word_total +
                    scott_fr_word_total + scott_pt_word_total)

whisper_wer_avg = (rawlings_word_total * whisper_wer1 + italiano_word_total * whisper_wer2
                   + scott_en_word_total * whisper_wer3 + scott_fr_sent_total * whisper_wer4
                   + scott_pt_word_total * whisper_wer5) \
                  / (rawlings_word_total + italiano_word_total + italiano_word_total +
                     scott_fr_word_total + scott_pt_word_total)

# Precision
assembly_precision_avg = (rawlings_sent_total * assembly_precision1
                          + italiano_sent_total * assembly_precision2
                          + scott_en_sent_total * assembly_precision3 +
                          scott_fr_sent_total * assembly_precision4
                          + scott_pt_sent_total * assembly_precision5) \
                         / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                            scott_fr_sent_total + scott_pt_sent_total)

google_precision_avg = (rawlings_sent_total * google_precision1
                        + italiano_sent_total * google_precision2
                        + scott_en_sent_total * google_precision3
                        + scott_fr_sent_total * google_precision4
                        + scott_pt_sent_total * google_precision5) \
                       / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                          scott_fr_sent_total + scott_pt_sent_total)

whisper_precision_avg = (rawlings_sent_total * whisper_precision1
                         + italiano_sent_total * whisper_precision2
                         + scott_en_sent_total * whisper_precision3
                         + scott_fr_sent_total * whisper_precision4
                         + scott_pt_sent_total * whisper_precision5) \
                        / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                           scott_fr_sent_total + scott_pt_sent_total)

# Recall
assembly_recall_avg = (rawlings_sent_total * assembly_recall1 + italiano_sent_total * assembly_recall2
                       + scott_en_sent_total * assembly_recall3 + scott_fr_sent_total * assembly_recall4
                       + scott_pt_sent_total * assembly_recall5) \
                      / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                         scott_fr_sent_total + scott_pt_sent_total)

google_recall_avg = (rawlings_sent_total * google_recall1 + italiano_sent_total * google_recall2
                     + scott_en_sent_total * google_recall3 + scott_fr_sent_total * google_recall4
                     + scott_pt_sent_total * google_recall5) \
                    / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                       scott_fr_sent_total + scott_pt_sent_total)

whisper_recall_avg = (rawlings_sent_total * whisper_recall1 + italiano_sent_total * whisper_recall2
                      + scott_en_sent_total * whisper_recall3 + scott_fr_sent_total * whisper_recall4
                      + scott_pt_sent_total * whisper_recall5) \
                     / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                        scott_fr_sent_total + scott_pt_sent_total)
# F1 Score
assembly_f1_avg = (rawlings_sent_total * assembly_f1_score1 + italiano_sent_total * assembly_f1_score2
                   + scott_en_sent_total * assembly_f1_score3 + scott_fr_sent_total * assembly_f1_score4
                   + scott_pt_sent_total * assembly_f1_score5) \
                  / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                     scott_fr_sent_total + scott_pt_sent_total)

google_f1_avg = (rawlings_sent_total * google_f1_score1 + italiano_sent_total * google_f1_score2
                 + scott_en_sent_total * google_f1_score3 + scott_fr_sent_total * google_f1_score4
                 + scott_pt_sent_total * google_f1_score5) \
                / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                   scott_fr_sent_total + scott_pt_sent_total)

whisper_f1_avg = (rawlings_sent_total * whisper_f1_score1 + italiano_sent_total * whisper_f1_score2
                  + scott_en_sent_total * whisper_f1_score3 + scott_fr_sent_total * whisper_f1_score4
                  + scott_pt_sent_total * whisper_f1_score5) \
                 / (rawlings_sent_total + italiano_sent_total + scott_en_sent_total +
                    scott_fr_sent_total + scott_pt_sent_total)

print("AssemblyAI averages: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(assembly_wer_avg, assembly_precision_avg, assembly_recall_avg, assembly_f1_avg))
print("Google Cloud averages: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(google_wer_avg, google_precision_avg, google_recall_avg, google_f1_avg))
print("Whisper (small) averages: WER={}, Precision={}, Recall={}, F1 Score={}\n"
      .format(whisper_wer_avg, whisper_precision_avg, whisper_recall_avg, whisper_f1_avg))
