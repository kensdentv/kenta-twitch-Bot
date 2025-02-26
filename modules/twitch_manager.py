import os
import modules.twitch_command_handler as command_handler
import modules.twitch_reward_manager as reward_manager
import modules.twitch_prediction_manager as prediction_manager
import asyncio

# Twitch API
from twitchAPI.helper import first
from twitchAPI.twitch import Twitch
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
from twitchAPI.object.eventsub import ChannelFollowEvent
from twitchAPI.eventsub.websocket import EventSubWebsocket


USER_SCOPES = [
    AuthScope.CHAT_READ, 
    AuthScope.CHAT_EDIT,
    AuthScope.BITS_READ,
    AuthScope.CHANNEL_READ_REDEMPTIONS,
    AuthScope.CHANNEL_READ_PREDICTIONS,
    AuthScope.MODERATOR_READ_FOLLOWERS

]

chat = None
APP_ID = os.getenv('TWITCH_APP_ID')
APP_SECRET = os.getenv('TWITCH_APP_SECRET')
TARGET_CHANNEL = 'kentadtv'

async def on_ready( ready_event: EventData ):
    print( f"Connected to channel..." )
    await ready_event.chat.join_room( TARGET_CHANNEL )

async def on_message( chat_message: ChatMessage ):
    await command_handler.handle_command(chat_message)

async def on_follow( follow: ChannelFollowEvent ):
    if chat is None: return
    chatroom = chat.room_cache.get(TARGET_CHANNEL)
    await chat.send_message(chatroom, f"@{follow.event.user_name}, Thank you for the follow!") 

async def main():
    # Login to twitch
    twitch = await Twitch( APP_ID , APP_SECRET )
    auth = UserAuthenticator( twitch, USER_SCOPES, force_verify=False )
    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication( token, USER_SCOPES, refresh_token )
    user = await first(twitch.get_users()) # Get me!
    
    # Start the chat listener
    global chat
    chat = await Chat( twitch )
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    chat.start()

    # Eventsub
    eventsub = EventSubWebsocket( twitch )
    eventsub.start()
    await eventsub.listen_channel_points_custom_reward_redemption_add( user.id, reward_manager.on_channel_points )
    await eventsub.listen_channel_prediction_begin( user.id, prediction_manager.on_prediction_begin )
    await eventsub.listen_channel_follow_v2( user.id, user.id, on_follow)

    # lets run till we press enter in the console
    try: await asyncio.Event().wait()
    except KeyboardInterrupt: pass
    finally:
        print("Cleaning up before shutdown...")
        chat.stop()
        await eventsub.stop()
        await twitch.close()
   
