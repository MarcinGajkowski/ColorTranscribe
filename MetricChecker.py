import MetricsStorage as metrics


def calculate_metrics_rawlings(script: str):
    # initialize Word Error Rate-checking variables
    words_to_check = []
    words_correct = 0
    sentences = script.split(". ")
    for sentence in sentences:
        sentence.split()
        for word in sentence:
            words_to_check.append(word)

    # check if the words match between tables and calculate WER
    true_words = metrics.rawlings_all_words
    if len(words_to_check) > len(true_words):
        for w in range(len(words_to_check) - len(true_words)):
            true_words.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(words_to_check))
    print(len(true_words))
    for i in range(len(true_words)):
        if words_to_check[i] == true_words[i]:
            words_correct += 1
    word_error_rate = words_correct / len(true_words)

    # check if given sentences are 100% correct
    sent_correct = 0
    true_sentences = metrics.truth_rawlings
    if len(sentences) > len(true_sentences):
        for j in range(len(sentences) - len(true_sentences) - 1):
            true_sentences.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(sentences))
    print(len(true_sentences))
    for i in range(len(true_sentences)):
        if sentences[i] == true_sentences[i]:
            sent_correct += 1

    # calculate precision, recall and F1 score
    precision = sent_correct / len(sentences)
    recall = sent_correct / len(true_sentences)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return word_error_rate, precision, recall, f1_score


def calculate_metrics_italiano(script: str):
    # initialize Word Error Rate-checking variables
    words_to_check = []
    words_correct = 0
    sentences = script.split(". ")
    for sentence in sentences:
        sentence.split()
        for word in sentence:
            words_to_check.append(word)

    # check if the words match between tables and calculate WER
    true_words = metrics.italiano_all_words
    if len(words_to_check) > len(true_words):
        for w in range(len(words_to_check) - len(true_words)):
            true_words.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(words_to_check))
    print(len(true_words))
    for i in range(len(true_words)):
        if words_to_check[i] == true_words[i]:
            words_correct += 1
    word_error_rate = words_correct / len(true_words)

    # check if given sentences are 100% correct
    sent_correct = 0
    true_sentences = metrics.truth_italiano
    if len(sentences) > len(true_sentences):
        for j in range(len(sentences) - len(true_sentences) - 1):
            true_sentences.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(sentences))
    print(len(true_sentences))
    for i in range(len(true_sentences)):
        if sentences[i] == true_sentences[i]:
            sent_correct += 1

    # calculate precision, recall and F1 score
    precision = sent_correct / len(sentences)
    recall = sent_correct / len(true_sentences)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return word_error_rate, precision, recall, f1_score


def calculate_metrics_scott_en(script: str):
    # initialize Word Error Rate-checking variables
    words_to_check = []
    words_correct = 0
    sentences = script.split(". ")
    for sentence in sentences:
        sentence.split()
        for word in sentence:
            words_to_check.append(word)

    # check if the words match between tables and calculate WER
    true_words = metrics.scott_en_all_words
    if len(words_to_check) > len(true_words):
        for w in range(len(words_to_check) - len(true_words)):
            true_words.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(words_to_check))
    print(len(true_words))
    for i in range(len(true_words)):
        if words_to_check[i] == true_words[i]:
            words_correct += 1
    word_error_rate = words_correct / len(true_words)

    # check if given sentences are 100% correct
    sent_correct = 0
    true_sentences = metrics.truth_scott_en
    if len(sentences) > len(true_sentences):
        for j in range(len(sentences) - len(true_sentences) - 1):
            true_sentences.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(sentences))
    print(len(true_sentences))
    for i in range(len(true_sentences)):
        if sentences[i] == true_sentences[i]:
            sent_correct += 1

    # calculate precision, recall and F1 score
    precision = sent_correct / len(sentences)
    recall = sent_correct / len(true_sentences)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return word_error_rate, precision, recall, f1_score


def calculate_metrics_scott_fr(script: str):
    # initialize Word Error Rate-checking variables
    words_to_check = []
    words_correct = 0
    sentences = script.split(". ")
    for sentence in sentences:
        sentence.split()
        for word in sentence:
            words_to_check.append(word)

    # check if the words match between tables and calculate WER
    true_words = metrics.scott_fr_all_words
    if len(words_to_check) > len(true_words):
        for w in range(len(words_to_check) - len(true_words)):
            true_words.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(words_to_check))
    print(len(true_words))
    for i in range(len(true_words)):
        if words_to_check[i] == true_words[i]:
            words_correct += 1
    word_error_rate = words_correct / len(true_words)

    # check if given sentences are 100% correct
    sent_correct = 0
    true_sentences = metrics.truth_scott_fr
    if len(sentences) > len(true_sentences):
        for j in range(len(sentences) - len(true_sentences) - 1):
            true_sentences.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(sentences))
    print(len(true_sentences))
    for i in range(len(true_sentences)):
        if sentences[i] == true_sentences[i]:
            sent_correct += 1

    # calculate precision, recall and F1 score
    precision = sent_correct / len(sentences)
    recall = sent_correct / len(true_sentences)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return word_error_rate, precision, recall, f1_score


def calculate_metrics_scott_pt(script: str):
    # initialize Word Error Rate-checking variables
    words_to_check = []
    words_correct = 0
    sentences = script.split(". ")
    for sentence in sentences:
        sentence.split()
        for word in sentence:
            words_to_check.append(word)

    # check if the words match between tables and calculate WER
    true_words = metrics.scott_pt_all_words
    if len(words_to_check) > len(true_words):
        for w in range(len(words_to_check) - len(true_words)):
            true_words.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(words_to_check))
    print(len(true_words))
    for i in range(len(true_words)):
        if words_to_check[i] == true_words[i]:
            words_correct += 1
    word_error_rate = words_correct / len(true_words)

    # check if given sentences are 100% correct
    sent_correct = 0
    true_sentences = metrics.truth_scott_pt
    if len(sentences) > len(true_sentences):
        for j in range(len(sentences) - len(true_sentences) - 1):
            true_sentences.append('\n')  # very temporary fix, don't know to do it otherwise
    print(len(sentences))
    print(len(true_sentences))
    for i in range(len(true_sentences)):
        if sentences[i] == true_sentences[i]:
            sent_correct += 1

    # calculate precision, recall and F1 score
    precision = sent_correct / len(sentences)
    recall = sent_correct / len(true_sentences)
    f1_score = 2 * (precision * recall) / (precision + recall)

    return word_error_rate, precision, recall, f1_score
