import commands.fun as fun
import commands.chat as chat
import commands.rewards as rewards
import modules.chat_control as chat_control
import pyautogui, sys, time



from twitchAPI.chat import ChatMessage
from modules.say import speak

from modules.vrc_osc_manager import set_vrc_state
import modules.spotify_manager as spotify

last_user = None

async def handle_command(chat_message: ChatMessage) -> None:
    
    message = chat_message.text
    command_array = message.split(' ')

    await check_for_response(chat_message)

    if not command_array[0].startswith('!'): return # Not a command

    await check_for_sound(message)

    command = command_array[0][1:].lower()
    
    global last_user
    if last_user == chat_message.user.name: return
   
    match command:
        # case 'story': await story()
        # case 'hoodieon': await set_vrc_state( 'Hoodie' , True )
        # case 'hoodieoff': await set_vrc_state( 'Hoodie' , False )
        case 'harnesson': await set_vrc_state( 'Harness' , True )
        case 'harnessoff': await set_vrc_state( 'Harness' , False )
        case 'female': await set_vrc_state( 'Female' , True )
        case 'male': await set_vrc_state( 'Female' , False )
        case 'lurk': await lurk(chat_message)
        case 'lois': await lurk(chat_message)
    
        case _: pass

    last_user = chat_message.user.name

    

async def lurk(chat_message: ChatMessage) -> None:
    await chat_message.chat.send_message(chat_message.room, 'Thank you for lurking! every viewer is appreciated on our road to Twitch Partner 💖')

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
    await chat.get_response(chat_message, command_array)