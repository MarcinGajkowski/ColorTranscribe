# man-made? transcripts taken from .txt files, marked as The Ground Truth
with open("GroundTruthTranscriptions/[English] Meet The Man Who Speaks 15 Languages.txt", 'r') as file:
    lines = file.readlines()
    truth_rawlings = []
    for l in lines:
        as_list = l.split(". ")
        truth_rawlings.append(as_list)

with open("GroundTruthTranscriptions/[English] ITALIAN POLYGLOT SPEAKING 15 LANGUAGES 2023 edition.txt", 'r') as file:
    lines = file.readlines()
    truth_italiano = []
    for l in lines:
        as_list = l.split(". ")
        truth_italiano.append(as_list)

with open("GroundTruthTranscriptions/[English] Why don't subtitles match dubbing.txt", 'r') as file:
    lines = file.readlines()
    truth_scott_en = []
    for l in lines:
        as_list = l.split(". ")
        truth_scott_en.append(as_list)

with open("GroundTruthTranscriptions/[French] Why don't subtitles match dubbing.txt", 'r') as file:
    lines = file.readlines()
    truth_scott_fr = []
    for l in lines:
        as_list = l.split(". ")
        truth_scott_fr.append(as_list)

with open("GroundTruthTranscriptions/[portugalski (Brazylia)] Why don't subtitles match dubbing.txt", 'r') as file:
    lines = file.readlines()
    truth_scott_pt = []
    for l in lines:
        as_list = l.split(". ")
        truth_scott_pt.append(as_list)


def calculate_metrics_rawlings(script: str):
    sentences = script.split(". ")
    num_correct = 0
    num_total = len(truth_rawlings)
    for i in range(num_total):
        if sentences[i] == truth_rawlings[i]:
            num_correct += 1
    precision = num_correct / len(sentences)
    recall = num_correct / num_total
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score


def calculate_metrics_italiano(script: str):
    sentences = script.split(". ")
    num_correct = 0
    num_total = len(truth_italiano)
    for i in range(num_total):
        if sentences[i] == truth_italiano[i]:
            num_correct += 1
    precision = num_correct / len(sentences)
    recall = num_correct / num_total
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score


def calculate_metrics_scott_en(script: str):
    sentences = script.split(". ")
    num_correct = 0
    num_total = len(truth_scott_en)
    for i in range(num_total):
        if sentences[i] == truth_scott_en[i]:
            num_correct += 1
    precision = num_correct / len(sentences)
    recall = num_correct / num_total
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score


def calculate_metrics_scott_fr(script: str):
    sentences = script.split(". ")
    num_correct = 0
    num_total = len(truth_scott_fr)
    for i in range(num_total):
        if sentences[i] == truth_scott_fr[i]:
            num_correct += 1
    precision = num_correct / len(sentences)
    recall = num_correct / num_total
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score


def calculate_metrics_scott_pt(script: str):
    sentences = script.split(". ")
    num_correct = 0
    num_total = len(truth_scott_pt)
    for i in range(num_total):
        if sentences[i] == truth_scott_pt[i]:
            num_correct += 1
    precision = num_correct / len(sentences)
    recall = num_correct / num_total
    f1_score = 2 * (precision * recall) / (precision + recall)

    return precision, recall, f1_score
