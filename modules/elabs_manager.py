import os

from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(
    api_key = os.getenv("ELEVENLABS_API_KEY")
)

voice_name = "judy"

def speak(message):

    # Generate audio from message
    audio = client.generate(
        text = message,
        voice = voice_name,
        model = "eleven_multilingual_v2"
    )

    # Print message and play audio
    print(f'\n{message}')
    play(audio)