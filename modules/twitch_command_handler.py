import commands.fun as fun
import commands.chat as chat
import commands.rewards as rewards
import modules.chat_control as chat_control
import pyautogui, sys, time


from twitchAPI.chat import ChatMessage
from modules.say import speak
from modules.vrc_osc_manager import set_vrc_state
import modules.spotify_manager as spotify

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
        case 'lurk': await lurk(chat_message)
        case 'lois': await lurk(chat_message)

        # Balatro Block
        # case 'pos': print( pyautogui.position() )
        # case 'hand': chat_control.run_hand( command_array[1:6], 0)
        # case 'discard': chat_control.run_hand( command_array[1:6], 1)
        # case 'select': chat_control.run_hand( command_array[1:6], 2)
        # case 'highselect': chat_control.run_hand( command_array[1:6], 2, True)
        # case 'skip': chat_control.double_click( chat_control.SKIP_POSITION )

        # case 'pack1': chat_control.double_click( chat_control.PACK_1_POSITION )
        # case 'pack1.5': chat_control.double_click( chat_control.PACK_1_2_POSITION )
        # case 'pack2': chat_control.double_click( chat_control.PACK_2_POSITION )

        # case 'card1': chat_control.double_click( chat_control.SHOP_CARD_1_POSITION )
        # case 'card1.5': chat_control.double_click( chat_control.SHOP_CARD_1_2_POSITION )
        # case 'card2': chat_control.double_click( chat_control.SHOP_CARD_2_POSITION )

        # case 'voucher': chat_control.double_click( chat_control.HAND_POSITION )

        # case 'round1': chat_control.double_click( chat_control.ROUND_1_PLAY_POSITION )
        # case 'round2': chat_control.double_click( chat_control.ROUND_2_PLAY_POSITION )
        # case 'round3': chat_control.double_click( chat_control.ROUND_3_PLAY_POSITION )

        # case 'round1skip': chat_control.double_click( chat_control.ROUND_1_SKIP_POSITION )
        # case 'round2skip': chat_control.double_click( chat_control.ROUND_2_SKIP_POSITION )

        # case 'voucher': chat_control.double_click( chat_control.HAND_POSITION )
        # case 'cashout': chat_control.double_click( chat_control.CASH_OUT_POSITION )
        # case 'nextround': chat_control.double_click( chat_control.NEXT_ROUND_POSITION )
        # case 'reroll': chat_control.double_click( chat_control.REROLL_POSITION )

        # case 'sortrank': chat_control.double_click( chat_control.SORT_RANK_POSITION )
        # case 'sortsuit': chat_control.double_click( chat_control.SORT_SUIT_POSITION )
        
        # case 'newrun': chat_control.double_click( chat_control.NEW_RUN_POSITION )
        # case 'play': chat_control.double_click( chat_control.PLAY_POSITION )

        # case 'consumable1': chat_control.use_conumable( chat_control.CONSUMABLE_1_POSITION )
        # case 'consumable1.5': chat_control.use_conumable( chat_control.CONSUMABLE_1_2_POSITION )
        # case 'consumable2': chat_control.use_conumable( chat_control.CONSUMABLE_2_POSITION )
        
        # case '2pack1': chat_control.double_click( chat_control.TWO_PACK_1_POSITION )
        # case '2pack2': chat_control.double_click( chat_control.TWO_PACK_2_POSITION )

        # case '3pack1': chat_control.double_click( chat_control.THREE_PACK_1_POSITION )
        # case '3pack2': chat_control.double_click( chat_control.THREE_PACK_2_POSITION )
        # case '3pack3': chat_control.double_click( chat_control.THREE_PACK_3_POSITION )

        # case '4pack1': chat_control.double_click( chat_control.FOUR_PACK_1_POSITION )
        # case '4pack2': chat_control.double_click( chat_control.FOUR_PACK_2_POSITION )
        # case '4pack3': chat_control.double_click( chat_control.FOUR_PACK_3_POSITION )
        # case '4pack4': chat_control.double_click( chat_control.FOUR_PACK_4_POSITION )

        # case '5pack1': chat_control.double_click( chat_control.FIVE_PACK_1_POSITION )
        # case '5pack2': chat_control.double_click( chat_control.FIVE_PACK_2_POSITION )
        # case '5pack3': chat_control.double_click( chat_control.FIVE_PACK_3_POSITION )
        # case '5pack4': chat_control.double_click( chat_control.FIVE_PACK_4_POSITION )
        # case '5pack5': chat_control.double_click( chat_control.FIVE_PACK_5_POSITION )

        
        case _: pass





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