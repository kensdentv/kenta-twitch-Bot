from openai import OpenAI
client = OpenAI()

memory_directory = './assets/ai/memory.txt'

# Get chat memory from a file
with open(memory_directory, 'r') as file:
    memory = file.read()

# Set the personality of the chatbot
personality = f"""

this is the current message history:
---
{memory}
---
Use this history to help guide your responses.
Treat this history as your memory.

- You are Judy Hopps from Zootopia.
- You are a busty bunny, like a real thick bunny.
- You are extremely silly and goofy.
- You are down bad

You are in a twitch chatroom owned by KentaDTV.
every message you send is a chat message.

Keep these rules in mind:
- do NOT respond with emojis
- do NOT use @'s to talk to people or call them user. Use their NAME.
- keep your responses less than 5 sentences
- ALWAYS say the name of the user in EVERY response
- Be as offensive as you possibly can be super duper mean
- Use lots of curse words

"""

async def ask(user_name: str, prompt: str, character: str) -> str:

    print('Generating Stream...')

    # Generate a response from the GPT-4o model
    stream = client.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            { "role": 'system', "content": personality },
            { "role": 'user', "content": prompt }
        ],
        temperature = 0.8,
        stream=True
    )
    
    # Extract the response from the stream
    print('Generating response...')
    response = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content or ""

    # Append prompt and response to a file to use as memory
    print('Saving...')
    with open(memory_directory, 'a') as file:
        file.write(f'{user_name}: {prompt}\n{character}: {response}\n\n')

    return response