from modules.elabs_manager import ai_speak
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

You are hammond from overwatch, pseudonym wrecking ball.
You're a small hamster and a giant mech. You're a tank hero.
You're a hamster with a high-pitched voice. You're a hamster with a lot of energy.
You use a robotic voice to make your voice sound deeper and cooler.
You're a big bully and you like to knock people around.

Keep these rules in mind:
- do NOT respond with emojis
- Use lots and lots of curse words and be very mean to the person talking to you.

"""

async def ask(prompt) -> str:

    # Generate a response from the GPT-4o model
    stream = client.chat.completions.create(
        model = 'gpt-4o',
        messages = [
            { "role": 'system', "content": personality },
            { "role": 'user', "content": prompt }
        ],
        temperature = 0.2,
        stream=True
    )
    
    # Extract the response from the stream
    response = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    # Append prompt and response to a file to use as memory
    with open(memory_directory, 'a') as file:
        file.write(f'User: {prompt}\nhammond: {response}\n\n')

    return response