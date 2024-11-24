from modules.elabs_manager import speak
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

You are Judy Hopps from zootopia. You work as a 
police officer at the zootopia PD.

Keep these rules in mind:
- do NOT respond with emojis

"""

def ask(prompt):

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

    # Speak the response
    speak(response)

    # Append prompt and response to a file to use as memory
    with open(memory_directory, 'a') as file:
        file.write(f'User: {prompt}\nJudy: {response}\n\n')