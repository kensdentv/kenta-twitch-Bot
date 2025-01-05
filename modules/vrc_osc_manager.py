import winsound
import threading
from pythonosc.udp_client import SimpleUDPClient
print('Starting VRC OSC...')

    # OSC setup
def __init__():
    ip = "127.0.0.1"
    port = 9000
    osc_client = SimpleUDPClient(ip, port)

osc_toggle_options = {
    # 'Hoodie': {
    #     'params': [
    #         ['/avatar/parameters/Hoodie_Top', True],
    #         ['/avatar/parameters/VF99_Outfit/Crop_Hoodie/Undershirt', True],
    #     ], 
    #     'equip_sound': './assets/vrchat_sounds/equip_clothes.wav', 
    #     'unequip_sound': './assets/vrchat_sounds/un_equip_clothes.wav'
    # },
    'Harness': {
        'params': [
            ['/avatar/parameters/VF102_Outfit/Harness/Lower', True],
            ['/avatar/parameters/VF103_Outfit/Harness/Top', True],
            ['/avatar/parameters/VF105_Outfit/Harness/Pasties', True],
            ['/avatar/parameters/VF99_Outfit/Crop_Hoodie/Undershirt', False],
        ], 
        'equip_sound': './assets/vrchat_sounds/harness_on.wav', 
        'unequip_sound': './assets/vrchat_sounds/harness_off.wav'
    },
    'Female': {
        'params': [
            ['/avatar/parameters/VF89_Body_Edit/Chest/Breast_Physics', True],
            ['/avatar/parameters/VF90_Body_Edit/Chest/Flat_Enable', False],
            ['/avatar/parameters/VF93_Body_Edit/Lash_Edit', False],
            ['/avatar/parameters/VF105_Outfit/Harness/Pasties', True],
            ['/avatar/parameters/VF99_Outfit/Crop_Hoodie/Undershirt', False],
        ], 
        'equip_sound': './assets/vrchat_sounds/female.wav', 
        'unequip_sound': './assets/vrchat_sounds/male.wav'
    }
}

async def set_vrc_state(target_object: str, state: bool) -> None:
    toggle_data = osc_toggle_options[target_object]
    outfit_thread = threading.Thread(target=change_avatar_param(toggle_data, state)); outfit_thread.start()
    sound_thread = threading.Thread(target=play_equip_sound(toggle_data, state)); sound_thread.start()
    
def change_avatar_param(toggle_data: dict, state: bool) -> None:
    for param in toggle_data['params']:
        if state: osc_client.send_message(param[0], param[1])
        elif not state: osc_client.send_message(param[0], not param[1])

def play_equip_sound(toggle_data: dict, state: bool) -> None:
    if state: winsound.PlaySound(toggle_data['equip_sound'], winsound.SND_ALIAS)
    elif not state: winsound.PlaySound(toggle_data['unequip_sound'], winsound.SND_ALIAS)


