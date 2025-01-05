import threading
import winsound
import modules.obs_manager as obs
from twitchAPI.object.eventsub import ChannelPointsCustomRewardRedemptionData, ChannelPredictionEvent


async def on_prediction_begin(_data: ChannelPredictionEvent) -> None:
    t1 = threading.Thread(target=play_gambline_sound)
    t2 = threading.Thread(target=show_coins)
    t1.start()
    t2.start()

def play_gambline_sound():
    winsound.PlaySound(f'./assets/predictions/gambling.wav', winsound.SND_ALIAS)

def show_coins():
    obs.flash_item("Layer - Overlay", 'Coins', 4)
