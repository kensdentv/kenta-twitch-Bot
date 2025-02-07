import time
from twitchAPI.chat import ChatMessage
import modules.spotify_manager as spotify
import modules.obs_manager as obs 

links = {
    "discord": 'https://discord.gg/ZcqBEtsZNj',
    "tiktok": 'https://www.tiktok.com/@kentadtv',
    "youtube": 'https://www.youtube.com/@kentadtv',
    "twitter": 'https://x.com/KentaDTV',
    "github": 'https://github.com/kentadtv',
}

async def get_response(chat_message: ChatMessage, command_array: list) -> None:
    match command_array[0]:
        # Social Response Commands
        case '!discord': await chat_message.chat.send_message(chat_message.room, links['discord'])
        case '!github': await chat_message.chat.send_message(chat_message.room, links['github'])
        case '!tiktok': await chat_message.chat.send_message(chat_message.room, links['tiktok'])
        case '!twitter': await chat_message.chat.send_message(chat_message.room, links['twitter'])
        case '!youtube': await chat_message.chat.send_message(chat_message.room, links['youtube'])
        case '!socials': await chat_message.chat.send_message(chat_message.room, ' '.join(links.values()))
        case '!commands': await chat_message.chat.send_message(chat_message.room, 'We Have Custom Chat Commands! You can find them all here: https://docs.google.com/spreadsheets/d/1tWjnshP2L7E1rxQuV7nLvjpeo-70vrl5UhHIS_W0Gd4/edit?usp=sharing')
        
        # Spotify Commands
        case '!song': await chat_message.chat.send_message(chat_message.room, spotify.get_current_song())
        # case '!prev': spotify.prev_song(); time.sleep(0.5) ;await chat_message.chat.send_message(chat_message.room, spotify.get_current_song())
        # case '!next': spotify.next_song(); time.sleep(0.5) ;await chat_message.chat.send_message(chat_message.room, spotify.get_current_song())
        # case '!queue': 
        #     if len(command_array) < 1: await chat_message.chat.send_message(chat_message.room, 'Please enter a valid Spotify URL (len)'); return
        #     await chat_message.chat.send_message(chat_message.room, spotify.queue_song(command_array[1]))
        
        # Funny Commands
        # case '!big': obs.big_center_screen("Screen")

