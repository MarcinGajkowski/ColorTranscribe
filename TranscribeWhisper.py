import torch
import torchaudio as torchaudio
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
# import whisper
# from WhisperLangDetection import detect_language_epicly
import Constants
from colored import Fore, Back, Style

# instructions on how to train the whisper-large-v3 model, taken from their page on HuggingFace
# decided to go with 'small' instead tho

# pick device to train the model on
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

# pick pretrained whisper model
model_id = "openai/whisper-small"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True, resume_download=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

# creating the pipeline
pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    stride_length_s=[6, 0],
    torch_dtype=torch_dtype,
    device=device,
)


def transcribe_and_detect(sample):
    # putting our sample file into the processor

    waveform, sample_rate = torchaudio.load(str(sample))
    input_features = processor(waveform.squeeze().numpy(), sampling_rate=sample_rate,
                               return_tensors="pt").input_features
    inputs = input_features.to(device)

    # generating timestamp IDs (sure hope they're useful)
    generate_ids = model.generate(inputs, return_timestamps=True, task="transcribe")
    processor.tokenizer.decode(generate_ids[0], decode_with_timestamps=True, output_offsets=True)

    # generating transcript
    result = pipe(sample)
    print(result["text"])

    model.config.forced_decoder_ids = processor.tokenizer.get_decoder_prompt_ids(task='transcribe')
    model.config.suppress_tokens = []

    model.generation_config.forced_decoder_ids = processor.tokenizer.get_decoder_prompt_ids(task='transcribe')
    model.generation_config.suppress_tokens = []

    lang_token = model.generate(inputs, max_new_tokens=1)[0, 1]
    lang_result = pipe.tokenizer.decode(lang_token)
    print(lang_result)

    # # an attempt at detecting languages and then changing the console text based on the language found
    # # too verbose and not necessary, but the probabilities shown are nice
    # print(detect_language_epicly(model, processor.tokenizer, input_features,
    #                              {"fr", "en", "de", "es", "ru", "pt", "ca", "nl", "ar", "sv",
    #                               "it", "he", "uk", "el", "ro", "hu", "no", "bg", "sr", "af",
    #                               "fa"}))

    return lang_result


def lang_whandler(sample):
    lang = transcribe_and_detect(sample)
    result = pipe(sample)
    match lang:
        case '<|en|>':
            color: str = f'{Fore.RED}{Back.BLUE}'
            print(f"Transcript (English): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|es|>':
            color: str = f'{Fore.RED}{Back.YELLOW}'
            print(f"Transcript (Spanish): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|ca|>':
            color: str = f'{Fore.YELLOW}{Back.RED}'
            print(f"Transcript (Catalan): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|fr|>':
            color: str = f'{Fore.WHITE}{Back.DARK_BLUE}'
            print(f"Transcript (French): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|de|>':
            color: str = f'{Fore.YELLOW}{Back.BLACK}'
            print(f"Transcript (German): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|it|>':
            color: str = f'{Fore.WHITE}{Back.GREEN}'
            print(f"Transcript (Italian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|pt|>':
            color: str = f'{Fore.BLUE}{Back.GREEN}'
            print(f"Transcript ((Brazilian) Portuguese): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|nl|>':
            color: str = f'{Fore.WHITE}{Back.ORANGE_1}'
            print(f"Transcript (Dutch): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|el|>':
            color: str = f'{Fore.BLUE}{Back.WHITE}'
            print(f"Transcript (Greek): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|ru|>':
            color: str = f'{Fore.WHITE}{Back.BLUE}'
            print(f"Transcript (Russian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|bg|>':
            color: str = f'{Fore.WHITE}{Back.RED}'
            print(f"Transcript (Bulgarian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|fa|>':
            color: str = f'{Fore.GREEN}{Back.WHITE}'
            print(f"Transcript (Farsi/Persian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|af|>':
            color: str = f'{Fore.GREEN}{Back.YELLOW}'
            print(f"Transcript (Afrikaans): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|hu|>':
            color: str = f'{Fore.RED}{Back.GREEN}'
            print(f"Transcript (Hungarian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|he|>':
            color: str = f'{Fore.WHITE}{Back.LIGHT_BLUE}'
            print(f"Transcript (Hebrew): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|ro|>':
            color: str = f'{Fore.WHITE}{Back.YELLOW}'
            print(f"Transcript (Romanian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|sv|>':
            color: str = f'{Fore.YELLOW}{Back.BLUE}'
            print(f"Transcript (Swedish): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|uk|>':
            color: str = f'{Fore.BLUE}{Back.YELLOW}'
            print(f"Transcript (Ukrainian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|no|>':
            color: str = f'{Fore.RED}{Back.DARK_BLUE}'
            print(f"Transcript (Norwegian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|sr|>':
            color: str = f'{Fore.GOLD_1}{Back.RED}'
            print(f"Transcript (Serbian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case '<|ar|>':
            color: str = f'{Fore.RED}{Back.WHITE}'
            print(f"Transcript (Arabic - Lebanon): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')

    return result["text"]


sample = Constants.FLAC_TOM3
lang_whandler(sample)
