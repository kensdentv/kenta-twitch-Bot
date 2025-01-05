import commands.fun as fun
import commands.chat as chat
import commands.rewards as rewards

from twitchAPI.chat import ChatMessage
from modules.say import speak
from modules.vrc_osc_manager import set_vrc_state


async def handle_command(chat_message: ChatMessage) -> None:
    
    message = chat_message.text
    command_array = message.split(' ')

    await check_for_response(chat_message)

    if not command_array[0].startswith('!'): return # Not a command

    await check_for_sound(message)

    command = command_array[0][1:].lower()
    match command:
        # case 'story': await story()
        # case 'hoodieon': await set_vrc_state( 'Hoodie' , True )
        # case 'hoodieoff': await set_vrc_state( 'Hoodie' , False )
        case 'harnesson': await set_vrc_state( 'Harness' , True )
        case 'harnessoff': await set_vrc_state( 'Harness' , False )
        case 'female': await set_vrc_state( 'Female' , True )
        case 'male': await set_vrc_state( 'Female' , False )
        case _: pass

async def story() -> None:
    with open('./assets/ai/story.txt', 'r') as file: story = file.read()
    print(story)
    await rewards.tts(story)

# Check for a play sound command
async def check_for_sound(message: str):
    command_array = message.split('!')
    await fun.play_sound(command_array[1])

# Check for a chat response command
async def check_for_response(chat_message: ChatMessage):
    command_array = chat_message.text.split(' ')
    await chat.get_response(chat_message, command_array[0])