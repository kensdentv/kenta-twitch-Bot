import commands.rewards as rewards
import winsound
import modules.obs_manager as obs
import threading

from twitchAPI.object.eventsub import ChannelPointsCustomRewardRedemptionData, ChannelPredictionEvent
from pprint import pprint


async def on_channel_points(data: ChannelPointsCustomRewardRedemptionData) -> None:
    # Get reward info
    reward_event: dict = data.to_dict().get('event', {})
    reward_object: dict = reward_event.get('reward', {})
    reward_title: str = reward_object.get('title', '')

    # Get user input if applicable
    user_input: str = reward_event.get('user_input', '')
    
    match reward_title:
        case 'TTS': await rewards.tts(user_input)
        case 'Pet Me!': await rewards.petpet()
        case 'Stretch!': await rewards.stretch()
        case 'Applause!': await rewards.applause()
        case 'Hydrate': await rewards.hydrate()
        case 'Talk to Judy Hopps': await rewards.ai_ask(user_input)
        case 'Girl Voice': await rewards.girlvoice()
        case 'Tell Me What To Do': await rewards.chat_command_me(user_input)

async def on_prediction_begin(_data: ChannelPredictionEvent) -> None:
    t1 = threading.Thread(target=play_gambline_sound)
    t2 = threading.Thread(target=show_coins)
    t1.start()
    t2.start()


def play_gambline_sound():
    winsound.PlaySound(f'./assets/predictions/gambling.wav', winsound.SND_ALIAS)

def show_coins():
    obs.flash_item('Coins', 4)