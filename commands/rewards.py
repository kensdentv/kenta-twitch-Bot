from modules.say import speak
from modules.open_ai_manager import ask

import modules.elabs_manager as elabs
import modules.obs_manager as obs
import winsound
import re

async def stretch() -> None:
    speak('Stretch time')

async def hydrate() -> None:
    speak('Hydration time, drink some water.')

async def tts(message: str) -> None:
    tts_array = []

    pattern = r"(\w+):\s(.*?)(?=\s\w+:|$)"
    matches = re.findall(pattern, message.lower())

    # Use the regex to create tts objects for each character message
    for name, text in matches: tts_array.append({"character": name, "message": text.strip()})
    if matches == []: tts_array.append({"character": "judy", "message": message})

    # run each tts message one after the other
    for tts in tts_array:
        tts_character = tts.get('character', 'judy')
        tts_message = tts.get('message', '')
        elabs.ai_speak( tts_message , tts_character)


async def applause() -> None:
     winsound.PlaySound(f'./assets/reward_sounds/applause.wav', winsound.SND_ALIAS)

async def petpet() -> None:
    speak('PetPet')
    obs.flash_item('PetPet')

async def girlvoice() -> None:
    speak('Valley Girl Voice Redeeemed')

async def chat_command_me(message: str) -> None:
    speak("Chat Commands you." + message)

async def ai_ask(prompt: str) -> None:
    speak(prompt)
    response = await ask(prompt)
    elabs.ai_speak(response, "hammond")
