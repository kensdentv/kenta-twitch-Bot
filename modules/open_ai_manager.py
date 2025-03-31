from openai import OpenAI
client = OpenAI()

# Set the personality of the chatbot
personality = f"""

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