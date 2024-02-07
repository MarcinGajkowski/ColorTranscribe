# man-made? transcripts taken from .txt files, marked as The Ground Truth
with open("GroundTruthTranscriptions/[English] Meet The Man Who Speaks 15 Languages.txt", 'r',
          encoding='utf-8') as file:
    # read text file lines an initialize tables
    lines = file.readlines()
    truth_rawlings = []
    rawlings_all_words = []

    # put all lines to one table and all words into the other
    for line in lines:
        truth_rawlings.append(line)
        for word in line.split():
            rawlings_all_words.append(word)

with open("GroundTruthTranscriptions/[English] ITALIAN POLYGLOT SPEAKING 15 LANGUAGES 2023 edition.txt", 'r',
          encoding='utf-8') as file:
    # read text file lines an initialize tables
    lines = file.readlines()
    truth_italiano = []
    italiano_all_words = []

    # put all lines to one table and all words into the other
    for line in lines:
        truth_italiano.append(line)
        for word in line.split():
            italiano_all_words.append(word)

with open("GroundTruthTranscriptions/[English] Why don't subtitles match dubbing.txt", 'r',
          encoding='utf-8') as file:
    # read text file lines an initialize tables
    lines = file.readlines()
    truth_scott_en = []
    scott_en_all_words = []

    # put all lines to one table and all words into the other
    for line in lines:
        truth_scott_en.append(line)
        for word in line.split():
            scott_en_all_words.append(word)

with open("GroundTruthTranscriptions/[French] Why don't subtitles match dubbing.txt", 'r',
          encoding='utf-8') as file:
    # read text file lines an initialize tables
    lines = file.readlines()
    truth_scott_fr = []
    scott_fr_all_words = []

    # put all lines to one table and all words into the other
    for line in lines:
        truth_scott_fr.append(line)
        for word in line.split():
            scott_fr_all_words.append(word)

with open("GroundTruthTranscriptions/[portugalski (Brazylia)] Why don't subtitles match dubbing.txt", 'r',
          encoding='utf-8') as file:
    # read text file lines an initialize tables
    lines = file.readlines()
    truth_scott_pt = []
    scott_pt_all_words = []

    # put all lines to one table and all words into the other
    for line in lines:
        truth_scott_pt.append(line)
        for word in line.split():
            scott_pt_all_words.append(word)
