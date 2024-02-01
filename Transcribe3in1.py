import assemblyai as aai
import Constants
from colored import Fore, Back, Style

# my EPIC API key and Transcriber setup
aai.settings.api_key = Constants.ASS_AI_API_KEY
transcriber = aai.Transcriber()

# remember to fuck around with utterances maybe

# text colors picked by language supported


# example of proper 'colored' usage
print(f'{Fore.white}{Back.green}Colored is Awesome!!!{Style.reset}')

# sample file path
SAMPLE_URL = './ColorTransSamples/polyglotSample.wav'

# the most basic transcribing method from AssemblyAI
transcript = transcriber.transcribe(SAMPLE_URL)
if transcript.error:
    print(transcript.error)

print(transcript.text)
