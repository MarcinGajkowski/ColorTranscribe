import assemblyai as aai
import Constants
from colored import Fore, Back, Style

# my EPIC API key and Transcriber setup
aai.settings.api_key = Constants.ASS_AI_API_KEY


# the basic transcribing method from AssemblyAI with language detection turned on
def transcribe(wav_file):
    config = aai.TranscriptionConfig(speaker_labels=True, language_detection=True)
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(wav_file)
    if transcript.error:
        print(transcript.error)
    return transcript


# matching languages to their countries' respective football team colors (the easiest way to do it imo)
# putting in all the supported ones because why not (in case you want to translate stuff in more languages)
def lang_handler(sample):
    transcript = transcribe(sample)
    lang = transcript.config.language_code
    match lang:
        case 'en':
            color: str = f'{Fore.WHITE}{Back.BLACK}'
            print(f"Transcript (English): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'en_us':
            color: str = f'{Fore.WHITE}{Back.BLACK}'
            print(f"Transcript (American English): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'en_uk':
            color: str = f'{Fore.WHITE}{Back.BLACK}'
            print(f"Transcript (British English): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'es':
            color: str = f'{Fore.RED}{Back.YELLOW}'
            print(f"Transcript (Spanish): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'fr':
            color: str = f'{Fore.WHITE}{Back.DARK_BLUE}'
            print(f"Transcript (French): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'de':
            color: str = f'{Fore.YELLOW}{Back.BLACK}'
            print(f"Transcript (German): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'it':
            color: str = f'{Fore.GREEN}{Back.WHITE}'
            print(f"Transcript (Italian): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'pt':
            color: str = f'{Fore.RED}{Back.DARK_GREEN}'
            print(f"Transcript ((Brazilian) Portuguese): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'nd':
            color: str = f'{Fore.RED}{Back.LIGHT_BLUE}'
            print(f"Transcript (Dutch): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'fi':
            color: str = f'{Fore.BLUE}{Back.WHITE}'
            print(f"Transcript (Finnish): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'hi':
            color: str = f'{Fore.GREEN}{Back.ORANGE_1}'
            print(f"Transcript (Hindu): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'ja':
            color: str = f'{Fore.RED}{Back.GOLD_1}'
            print(f"Transcript (Japanese): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'ko':
            color: str = f'{Fore.BLACK}{Back.RED}'
            print(f"Transcript (Korean): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'pl':
            color: str = f'{Fore.WHITE}{Back.RED}'
            print(f"Transcript (Polish): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'ru':
            color: str = f'{Fore.GOLD_1}{Back.RED}'
            print(f"Transcript (Russian): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'tr':
            color: str = f'{Fore.RED}{Back.WHITE}'
            print(f"Transcript (Turkish): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'uk':
            color: str = f'{Fore.YELLOW}{Back.BLUE}'
            print(f"Transcript (Ukrainian): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'vi':
            color: str = f'{Fore.YELLOW}{Back.DARK_RED_1}'
            print(f"Transcript (Vietnamese): " + f'{color}{transcript.text}' + f'{Style.reset}')
    match lang:
        case 'zh':
            color: str = f'{Fore.YELLOW}{Back.RED}'
            print(f"Transcript (Chinese): " + f'{color}{transcript.text}' + f'{Style.reset}')

    return transcript.text


# ts_sample.config.language_code = 'en_uk'
lang_handler(Constants.SAMPLE_TOM3)
