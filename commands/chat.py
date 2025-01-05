from twitchAPI.chat import ChatMessage

links = {
    "discord": 'https://discord.gg/ZcqBEtsZNj',
    "tiktok": 'https://www.tiktok.com/@kentadtv',
    "youtube": 'https://www.youtube.com/@kentadtv',
    "twitter": 'https://x.com/KentaDTV',
    "github": 'https://github.com/komdog',
}

async def get_response(chat_message: ChatMessage, command: str) -> None:
    match command:
        case '!discord': await chat_message.chat.send_message(chat_message.room, links['discord'])
        case '!github': await chat_message.chat.send_message(chat_message.room, links['github'])
        case '!tiktok': await chat_message.chat.send_message(chat_message.room, links['tiktok'])
        case '!twitter': await chat_message.chat.send_message(chat_message.room, links['twitter'])
        case '!youtube': await chat_message.chat.send_message(chat_message.room, links['youtube'])
        case '!socials': await chat_message.chat.send_message(chat_message.room, ' '.join(links.values()))
        case '!commands': await chat_message.chat.send_message(chat_message.room, 'We Have Custom Chat Commands! You can find them all here: https://docs.google.com/spreadsheets/d/1tWjnshP2L7E1rxQuV7nLvjpeo-70vrl5UhHIS_W0Gd4/edit?usp=sharing')