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

You are in a twitch chatroom talking to users.
every message you send is a response to a user.

Keep these rules in mind:
- do NOT respond with emojis
- keep your responses less than 8 sentences

"""

async def ask(prompt: str, character: str) -> str:

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
        file.write(f'User: {prompt}\n{character}: {response}\n\n')

    return response