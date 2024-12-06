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