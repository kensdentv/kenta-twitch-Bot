from modules.say import speak
from modules.open_ai_manager import ask

import modules.elabs_manager as elabs
import modules.obs_manager as obs
import modules.rich_tts_manager as rich_tts
import winsound
import re

async def stretch() -> None: speak('Stretch time')
async def hydrate() -> None: speak('Hydration time, drink some water.')
async def tts(message: str) -> None: await rich_tts.parse_rich_tts(message)
async def applause() -> None: winsound.PlaySound(f'./assets/reward_sounds/applause.wav', winsound.SND_ALIAS)

async def petpet() -> None:
    speak('PetPet')
    obs.flash_item('PetPet')

async def girlvoice() -> None: speak('Valley Girl Voice Redeeemed')
async def chat_command_me(message: str) -> None: speak("Chat Commands you." + message)

async def ai_ask(prompt: str) -> None:
    speak(prompt)
    response = await ask(prompt)
    elabs.ai_speak(response, "hammond")
