
import modules.twitch_manager as twitch
import asyncio

notif_index = 1
notification_messages =[
    'Remember to check out the Discord server! https://discord.gg/ZcqBEtsZNj',
    'Join our VRChat group for meetups! https://vrc.group/KENDTV.9059',
    'You can play sound effects in chat for FREE type !commands for a list of silly sounds',
    'If you enjoy the stream, consider following! It helps me out a lot!',
    'Want to support the stream? Consider subscribing!',
]

async def run_notif_loop():
    while True:
        await send_notification()
        await asyncio.sleep(600)

async def send_notification():
        if twitch.chat is None: return

        global notif_index
        notif_index = (notif_index + 1) % len(notification_messages)

        chatroom = twitch.chat.room_cache.get(twitch.TARGET_CHANNEL)
        await twitch.chat.send_message(chatroom, notification_messages[notif_index]) # Send a message to the chatroom

async def main():
    print('Starting notifications manager...')
    asyncio.create_task( run_notif_loop() )


