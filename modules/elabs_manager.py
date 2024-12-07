import os

from elevenlabs.client import ElevenLabs
from elevenlabs import play

client = ElevenLabs(
    api_key = os.getenv("ELEVENLABS_API_KEY")
)

available_voices = [
    'Alice',
    'narrator',
    'diane',
    'mrwolf',
    'judy',
    'nick',
    'bellwether',
    'mrsotterton',
    'nicole',
    'sonic',
    'hammond',
    'goku',
    'kratos',
    'peter',
    'tails',
    'bugs'
]

def ai_make_audio(message, voice_name = "Alice"):

    if voice_name not in available_voices: voice_name = "Alice"

    # Generate audio from message
    audio = client.generate(
        text = message,
        voice = voice_name,
        model = "eleven_multilingual_v2"
    )

    return audio

