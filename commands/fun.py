import os

import modules.obs_manager as obs
import modules.say as say
import winsound

async def play_sound(sound_name):
    if not os.path.exists(f'./assets/sounds/{sound_name}.wav'): return
    winsound.PlaySound(f'./assets/sounds/{sound_name}.wav', winsound.SND_ALIAS)