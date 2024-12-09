from modules.say import speak
from modules.open_ai_manager import ask
from modules.elabs_manager import ai_make_audio, play

import modules.obs_manager as obs
import modules.rich_tts_manager as rich_tts
import winsound
import random


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
    character = "judy"
    response = await ask(prompt, character)
    
    audio = ai_make_audio(response, character)
    obs.activate_filter('Slide In', 'Group', True)
    play(audio)
    obs.activate_filter('Slide Out', 'Group', True)

def kiss() -> None:
    kiss_sounds = [
        './assets/reward_sounds/kiss_1.wav',
        './assets/reward_sounds/kiss_2.wav',
        './assets/reward_sounds/kiss_3.wav',
    ]
    chosen_kiss_sound = random.choice(kiss_sounds)
    winsound.PlaySound(chosen_kiss_sound, winsound.SND_ALIAS)
    print(chosen_kiss_sound)
    obs.flash_item('Kiss', 3)