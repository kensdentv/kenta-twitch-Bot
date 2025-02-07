from enum import Enum
import time, pyautogui

HAND_POSITION = [852, 871]
DISCARD_POSITION = [1186, 869]
SKIP_POSITION = [1255, 903]

SHOP_CARD_1_POSITION = [1059, 605]
SHOP_CARD_1_2_POSITION = [1129, 605]
SHOP_CARD_2_POSITION = [1206, 605]

PACK_1_POSITION = [1136, 903]
PACK_1_2_POSITION = [1215, 903]
PACK_2_POSITION = [1290, 903]

ROUND_1_PLAY_POSITION = [739,403]
ROUND_2_PLAY_POSITION = [1024,403]
ROUND_3_PLAY_POSITION = [1307,403]

ROUND_1_SKIP_POSITION = [777,780]
ROUND_2_SKIP_POSITION = [1044,780]

CASH_OUT_POSITION = [1013,468]
NEXT_ROUND_POSITION = [756,477]
REROLL_POSITION = [756,583]

SORT_RANK_POSITION = [988, 892]
SORT_SUIT_POSITION = [1056, 892]

NEW_RUN_POSITION = [1171, 795]
PLAY_POSITION = [961, 805]

CONSUMABLE_1_POSITION = [1368, 270]
CONSUMABLE_1_2_POSITION = [1458, 270]
CONSUMABLE_2_POSITION = [1548, 270]

TWO_PACK_1_POSITION = [946, 800]
TWO_PACK_2_POSITION = [1106, 800]

THREE_PACK_1_POSITION = [884, 800]
THREE_PACK_2_POSITION = [1034, 800]
THREE_PACK_3_POSITION = [1174, 800]

FOUR_PACK_1_POSITION = [756, 800]
FOUR_PACK_2_POSITION = [936, 800]
FOUR_PACK_3_POSITION = [1116, 800]
FOUR_PACK_4_POSITION = [1296, 800]

FIVE_PACK_1_POSITION = [760, 800]
FIVE_PACK_2_POSITION = [900, 800]
FIVE_PACK_3_POSITION = [1040, 800]
FIVE_PACK_4_POSITION = [1180, 800]
FIVE_PACK_5_POSITION = [1320, 800]

HIGH_CARD_Y = 480
LOW_CARD_Y = 700

# CARD_1_POSITION = [669,700]
# CARD_2_POSITION = [769,700]
# CARD_3_POSITION = [869,700]
# CARD_4_POSITION = [969,700]
# CARD_5_POSITION = [1069,700]
# CARD_6_POSITION = [1169,700]
# CARD_7_POSITION = [1269,700]
# CARD_8_POSITION = [1369,700]

TYPE_HAND = 0
TYPE_DISCARD = 1
TYPE_SELECT = 2

def get_all_card_positions(y_pos: int) -> list[list[int]]:
    return [
        [669,y_pos],
        [769,y_pos],
        [869,y_pos],
        [969,y_pos],
        [1069,y_pos],
        [1169,y_pos],
        [1269,y_pos],
        [1369,y_pos]
    ]
    

def run_hand(cards: list[int], type: int, high: bool = False) -> None:
        
    # Validate list of cards
    if cards is None: return
    if len(cards) <= 0: return

    unique_cards = list(set(cards))
    print(unique_cards)

    if high: card_positions = get_all_card_positions(HIGH_CARD_Y)
    else: card_positions = get_all_card_positions(LOW_CARD_Y)

    # Click Every Card
    last_card = int(unique_cards[-1])
    for card in unique_cards: 

        if not card.isdigit(): continue
        if int(card) < 1 or int(card) > 8: continue
        if int(card) < 1 or int(card) > 8: continue

        x_pos = card_positions[ int(card) - 1][0]
        y_pos = card_positions[ int(card) - 1][1]
        
        pyautogui.click(x_pos, y_pos)

    # Pres Button
    if len(cards) > 1: pyautogui.click(card_positions[last_card - 1][0], card_positions[last_card - 1][1])
    if type == TYPE_HAND: double_click(HAND_POSITION)
    if type == TYPE_DISCARD: double_click(DISCARD_POSITION)
    if type == TYPE_SELECT: pass
    else: pass


def use_conumable(pos: list) -> None:
    # Select Card
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(0.05)
    pyautogui.click(button=pyautogui.PRIMARY)

    # Click Use
    time.sleep(0.05)
    pyautogui.moveTo(pos[0] + 100, pos[1])
    time.sleep(0.05)
    pyautogui.click(button=pyautogui.PRIMARY)

def double_click(pos: list) -> None:
    pyautogui.moveTo(pos[0], pos[1])
    time.sleep(0.05)
    pyautogui.click(button=pyautogui.PRIMARY)
    time.sleep(0.05)
    pyautogui.click(button=pyautogui.PRIMARY)