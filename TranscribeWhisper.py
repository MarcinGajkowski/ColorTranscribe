import whisper
from colored import Fore, Back, Style

model = whisper.load_model("small")


def lang_whandler(sample):
    result = model.transcribe(sample)
    lang = result["language"]
    match lang:
        case 'en':
            color: str = f'{Fore.RED}{Back.BLUE}'
            print(f"Transcript (English): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'es':
            color: str = f'{Fore.RED}{Back.YELLOW}'
            print(f"Transcript (Spanish): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'ca':
            color: str = f'{Fore.YELLOW}{Back.RED}'
            print(f"Transcript (Catalan): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'fr':
            color: str = f'{Fore.WHITE}{Back.DARK_BLUE}'
            print(f"Transcript (French): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'de':
            color: str = f'{Fore.YELLOW}{Back.BLACK}'
            print(f"Transcript (German): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'it':
            color: str = f'{Fore.WHITE}{Back.GREEN}'
            print(f"Transcript (Italian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'pt':
            color: str = f'{Fore.DARK_BLUE}{Back.GREEN}'
            print(f"Transcript ((Brazilian) Portuguese): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'nl':
            color: str = f'{Fore.WHITE}{Back.ORANGE_1}'
            print(f"Transcript (Dutch): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'el':
            color: str = f'{Fore.BLUE}{Back.WHITE}'
            print(f"Transcript (Greek): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'ru':
            color: str = f'{Fore.WHITE}{Back.BLUE}'
            print(f"Transcript (Russian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'bg':
            color: str = f'{Fore.WHITE}{Back.RED}'
            print(f"Transcript (Bulgarian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'fa':
            color: str = f'{Fore.GREEN}{Back.WHITE}'
            print(f"Transcript (Farsi/Persian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'af':
            color: str = f'{Fore.GREEN}{Back.YELLOW}'
            print(f"Transcript (Afrikaans): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'hu':
            color: str = f'{Fore.RED}{Back.GREEN}'
            print(f"Transcript (Hungarian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'he':
            color: str = f'{Fore.WHITE}{Back.LIGHT_BLUE}'
            print(f"Transcript (Hebrew): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'ro':
            color: str = f'{Fore.WHITE}{Back.YELLOW}'
            print(f"Transcript (Romanian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'sv':
            color: str = f'{Fore.YELLOW}{Back.BLUE}'
            print(f"Transcript (Swedish): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'uk':
            color: str = f'{Fore.BLUE}{Back.YELLOW}'
            print(f"Transcript (Ukrainian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'no':
            color: str = f'{Fore.RED}{Back.DARK_BLUE}'
            print(f"Transcript (Norwegian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'sr':
            color: str = f'{Fore.GOLD_1}{Back.RED}'
            print(f"Transcript (Serbian): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')
    match lang:
        case 'ar':
            color: str = f'{Fore.RED}{Back.WHITE}'
            print(f"Transcript (Arabic - Lebanon): " + f'{color}{result["text"]}'
                  + f'{Style.reset}')

    return result["text"]


# sample = Constants.FLAC_TOM3
# lang_whandler(sample)
