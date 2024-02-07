from google.cloud import speech_v1p1beta1 as speechbeta
import Constants
from colored import Fore, Back, Style


# transcription method taken straight from Google Cloud's docs, modified to add some color to the mix
# any of my comments will be marked by an ! in the beginning
def color_transcribe_file_with_multilanguage_gcs(gcs_uri: str) -> str:
    # ! create Google client
    client = speechbeta.SpeechClient()

    # list of detectable languages (based on the sample videos)
    first_language = "en-GB"
    alternate_languages = {"fr-FR", "nl-NL", "el-GR", "ru-RU", "it-IT", "de-DE", "af-ZA", "hu-HU", "es-ES", "iw-IL",
                           "en-US", "bg-BG", "ca-ES", "fa-IR", "pt-BR", "ro-RO", "sv-SE", "uk-UA", "no-NO", "sr-RS",
                           "ar-LB"}

    # Configure request to enable multiple languages
    recognition_config = speechbeta.RecognitionConfig(
        encoding=speechbeta.RecognitionConfig.AudioEncoding.FLAC,
        audio_channel_count=2,
        sample_rate_hertz=44100,
        model="latest_long",
        language_code=first_language,
        alternative_language_codes=alternate_languages,
        enable_automatic_punctuation=True,
    )

    # Set the remote path for the audio file
    audio = speechbeta.RecognitionAudio(uri=gcs_uri)

    # Use non-blocking call for getting file transcription
    response = client.long_running_recognize(
        config=recognition_config, audio=audio
    ).result(timeout=1000)

    # ! matching languages to their countries' respective football team colors (the easiest way to do it imo)
    transcript_builder = []
    for i, result in enumerate(response.results):
        lang = recognition_config.language_code
        alternative = result.alternatives[0]
        match lang:
            case 'en-GB':
                color: str = f'{Fore.WHITE}{Back.BLACK}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'en-US':
                color: str = f'{Fore.WHITE}{Back.BLACK}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'el-GR':
                color: str = f'{Fore.BLUE}{Back.WHITE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'ru-RU':
                color: str = f'{Fore.WHITE}{Back.BLUE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'bg-BG':
                color: str = f'{Fore.WHITE}{Back.RED}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'fa-IR':
                color: str = f'{Fore.GREEN}{Back.WHITE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'af-ZA':
                color: str = f'{Fore.GREEN}{Back.YELLOW}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'hu-HU':
                color: str = f'{Fore.RED}{Back.GREEN}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'iw-IL':
                color: str = f'{Fore.WHITE}{Back.LIGHT_BLUE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'ro-RO':
                color: str = f'{Fore.WHITE}{Back.YELLOW}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'sv-SE':
                color: str = f'{Fore.YELLOW}{Back.BLUE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'uk-UA':
                color: str = f'{Fore.BLUE}{Back.YELLOW}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'no-NO':
                color: str = f'{Fore.RED}{Back.DARK_BLUE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'sr-RS':
                color: str = f'{Fore.GOLD_1}{Back.RED}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'ar-LB':
                color: str = f'{Fore.RED}{Back.WHITE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'es-ES':
                color: str = f'{Fore.RED}{Back.YELLOW}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'ca-ES':
                color: str = f'{Fore.YELLOW}{Back.RED}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'fr-FR':
                color: str = f'{Fore.WHITE}{Back.DARK_BLUE}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'de-DE':
                color: str = f'{Fore.YELLOW}{Back.BLACK}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'it-IT':
                color: str = f'{Fore.WHITE}{Back.GREEN}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'pt-BR':
                color: str = f'{Fore.DARK_BLUE}{Back.GREEN}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')
        match lang:
            case 'nl-NL':
                color: str = f'{Fore.WHITE}{Back.ORANGE_1}'
                transcript_builder.append(f'{color}{alternative.transcript}'
                                          + f'{Style.reset}')

    transcript = "".join(transcript_builder)
    print(transcript)

    return transcript


color_transcribe_file_with_multilanguage_gcs(Constants.GOOG_TOM1)
