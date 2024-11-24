from modules.say import speak
from modules.open_ai_manager import ask

import modules.elabs_manager as elabs
import modules.obs_manager as obs
import winsound

async def stretch():
    speak('Stretch time')

async def hydrate():
    speak('Hydration time, drink some water.')

async def tts(message: str):
    elabs.ai_speak(message)

async def applause():
     winsound.PlaySound(f'./assets/reward_sounds/applause.wav', winsound.SND_ALIAS)

async def petpet():
    speak('PetPet')
    obs.flash_item('PetPet')

async def girlvoice():
    speak('Valley Girl Voice Redeeemed')

async def ai_ask(prompt: str):
    speak(prompt)
    response = await ask(prompt)
    elabs.ai_speak(response, "hammond")
