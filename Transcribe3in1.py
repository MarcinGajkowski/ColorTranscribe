import assemblyai as aai

# my EPIC API key and Trasncriber setup
aai.settings.api_key = "d722ee39e3484b3e807a1d7d024f7501"
transcriber = aai.Transcriber()

# text colors picked by language supported


# sample file path
SAMPLE_URL = './ColorTransSamples/polyglotSample.wav'

# the most basic transcribing method from AssemblyAI
transcript = transcriber.transcribe(SAMPLE_URL)
if transcript.error:
   print(transcript.error)


print(transcript.text)