import os
import asyncio
import modules.twitch_command_handler as command_handler
import modules.twitch_reward_manager as reward_manager
import modules.twitch_prediction_manager as prediction_manager

from uuid import UUID

# Twitch API
from twitchAPI.helper import first
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from twitchAPI.eventsub.websocket import EventSubWebsocket


USER_SCOPES = [
    AuthScope.CHAT_READ, 
    AuthScope.CHAT_EDIT,
    AuthScope.BITS_READ,
    AuthScope.CHANNEL_READ_REDEMPTIONS,
    AuthScope.CHANNEL_READ_PREDICTIONS

]

APP_ID = os.getenv('TWITCH_APP_ID')
APP_SECRET = os.getenv('TWITCH_APP_SECRET')
TARGET_CHANNEL = 'kentadtv'

async def on_ready( ready_event: EventData ):
    print( f"Connected to channel..." )
    await ready_event.chat.join_room( TARGET_CHANNEL )

async def on_message( chat_message: ChatMessage ):
    await command_handler.handle_command(chat_message)



async def main():
    # Login to twitch
    twitch = await Twitch( APP_ID , APP_SECRET )
    auth = UserAuthenticator( twitch, USER_SCOPES, force_verify=False )
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication( token, USER_SCOPES, refresh_token )
    user = await first(twitch.get_users()) # Get me!
    
    # Start the chat listener
    chat = await Chat( twitch )
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.start()

    # Eventsub
    eventsub = EventSubWebsocket( twitch )
    eventsub.start()
    await eventsub.listen_channel_points_custom_reward_redemption_add( user.id, reward_manager.on_channel_points )
    await eventsub.listen_channel_prediction_begin( user.id, prediction_manager.on_prediction_begin )

    # lets run till we press enter in the console
    try: 
        input('press ENTER to stop\\n')
    except KeyboardInterrupt:
        pass
    finally:
        # now we can close the chat bot and the twitch api client
        chat.stop()
        await eventsub.stop()
        await twitch.close()
   

asyncio.run( main() )