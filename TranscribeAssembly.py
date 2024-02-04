import assemblyai as aai
import Constants
from colored import Fore, Back, Style

# my EPIC API key and Transcriber setup
aai.settings.api_key = Constants.ASS_AI_API_KEY


# the basic transcribing method from AssemblyAI with language detection turned on
def transcribe(wav_file):
    config = aai.TranscriptionConfig(language_detection=True, speaker_labels=True)
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(wav_file)
    if transcript.error:
        print(transcript.error)
    return transcript


# matching languages to their countries' respective football team colors (the easiest way to do it imo)
def lang_handler(transcript):
    lang = transcript.config.language_detection
    match lang:
        case 'en_us':
            color: str = f'{Fore.RED}{Back.WHITE}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case 'es':
            color: str = f'{Fore.RED}{Back.YELLOW}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case 'fr':
            color: str = f'{Fore.WHITE}{Back.BLUE}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case 'de':
            color: str = f'{Fore.YELLOW}{Back.BLACK}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case 'it':
            color: str = f'{Fore.GREEN}{Back.WHITE}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case 'pt':
            color: str = f'{Fore.RED}{Back.GREEN}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case 'nd':
            color: str = f'{Fore.RED}{Back.LIGHT_BLUE}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
    match lang:
        case _:
            color: str = f'{Fore.WHITE}{Back.BLACK}'
            print(f'{color}{transcript.text}' + f' {Style.reset}')
