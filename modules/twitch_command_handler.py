import commands.fun as fun
import commands.chat as chat

from twitchAPI.chat import ChatMessage
from modules.say import speak


async def handle_command(chat_message: ChatMessage) -> None:
    
    message = chat_message.text
    command_array = message.split(' ')

    await check_for_sound(message)
    await check_for_response(chat_message)

    if not command_array[0].startswith('!'): return # Not a command

    command = command_array[0][1:].lower()
    match command: 
        case _: pass


# Check for a play sound command
async def check_for_sound(message: str):
    command_array = message.split(' ')
    await fun.play_sound(command_array[0])

# Check for a chat response command
async def check_for_response(chat_message: ChatMessage):
    command_array = chat_message.text.split(' ')
    await chat.get_response(chat_message, command_array[0])