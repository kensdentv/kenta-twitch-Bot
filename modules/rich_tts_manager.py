import re
import winsound
import modules.elabs_manager as elabs

# Split the message into individual character messages
async def parse_rich_tts(message: str) -> None:
    tts_array = []

    pattern = r"(\w+):\s(.*?)(?=\s\w+:|$)"
    matches = re.findall(pattern, message.lower())

    # Use the regex to create tts objects for each character message
    for name, text in matches: tts_array.append({"character": name, "message": text.strip()})
    if matches == []: tts_array.append({"character": "judy", "message": message})

    # Take each character message and split the text and sound effects
    for tts in tts_array: await parse_message_pieces( tts )

# Take each tts message and parses the character, text, any sound effects in the message
async def parse_message_pieces(tts: dict) -> None:
    tts_character = tts.get('character', 'judy')
    tts_message = tts.get('message', '')

    # Use regex to find all text and parenthesis content
    # Remove any empty strings that might appear in the result
    sfx_split = re.split(r'(\([^()]*\))', tts_message)
    sfx_split = [item for item in sfx_split if item]

    for split_message in sfx_split: await run_rich_tts(split_message, tts_character)
        

async def run_rich_tts(message: str, tts_character: str) -> None:
    if message == ' ': return
    if not message.startswith('('): 
        audio = elabs.ai_make_audio( message , tts_character); 
        elabs.play(audio)
        return
    winsound.PlaySound(f'./assets/sounds/{message[1:-1]}.wav', winsound.SND_ALIAS)

        