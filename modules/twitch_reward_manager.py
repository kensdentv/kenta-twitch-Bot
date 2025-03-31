import commands.rewards as rewards
from modules.say import speak
import winsound

from twitchAPI.object.eventsub import ChannelPointsCustomRewardRedemptionData

async def on_channel_points(data: ChannelPointsCustomRewardRedemptionData) -> None:
    # Get reward info
    reward_event: dict = data.to_dict().get('event', {})
    reward_object: dict = reward_event.get('reward', {})
    reward_title: str = reward_object.get('title', '')

    # Get user input if applicable
    user_name: set = reward_event.get('user_name', 'Twitch User')
    user_input: str = reward_event.get('user_input', '')
    
    match reward_title:
        case 'TTS': await rewards.tts(user_input)
        case 'Pet me!': speak('PetPet')
        case 'Spin me!': winsound.PlaySound(f'./assets/reward_sounds/spin.wav', winsound.SND_ASYNC)
        case 'Yeet me!': winsound.PlaySound(f'./assets/reward_sounds/yeet.wav', winsound.SND_ASYNC)
        case 'Stretch!': await rewards.stretch()
        case 'Applause!': await rewards.applause()
        case 'Hydrate': await rewards.hydrate()
        case 'Talk to Judy Hopps': await rewards.ai_ask(user_name, user_input)
        case 'Girl Voice': await rewards.girlvoice()
        case 'Tell Me What To Do': await rewards.chat_command_me(user_input) 
        case 'Smooch Me': rewards.kiss()
        case 'Laugh Track': rewards.laugh()
        case 'Lois': rewards.lois() 



