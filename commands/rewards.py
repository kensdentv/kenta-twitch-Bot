from modules.say import speak
import modules.elabs_manager as elabs
import modules.obs_manager as obs
import winsound

async def stretch():
    speak('Stretch time')

async def hydrate():
    speak('Hydration time, drink some water.')

async def tts(message: str):
    elabs.speak(message)

async def applause():
     winsound.PlaySound(f'./assets/reward_sounds/applause.wav', winsound.SND_ALIAS)

async def petpet():
    speak('PetPet')
    obs.flash_item('PetPet')

async def girlvoice():
    speak('Valley Girl Voice Redeeemed')