url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9b041902-4e01-423d-bf28-a172e63c4633'
apikey = '5qyeamwa3aPf24giXXRITjGVIKo2EWx5ukMpWyvLsA1e'
from typing import Text
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# Setup Service
authenticator = IAMAuthenticator(apikey)
# New TTS Service
tts = TextToSpeechV1(authenticator=authenticator)
# Set Service URL
tts.set_service_url(url)

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hello World!', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
    



