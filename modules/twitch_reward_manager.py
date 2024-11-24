import commands.rewards as rewards

from twitchAPI.object.eventsub import ChannelPointsCustomRewardRedemptionData
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
        case 'Girl Voice': await rewards.girlvoice()