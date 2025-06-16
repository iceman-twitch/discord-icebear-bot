import discord
from discord.ext import commands
from discord.ext.commands import bot
import time
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

api_url = "https://api.openai.com/v1/engines/turbo-small/completions"
api_key = "API_KEY"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

responses = {
    "szia": ["Hello", "Helló", "Szia", "Cső"],
    "hello": ["Hello", "Helló", "Szia", "Cső"],
    "helló": ["Hello", "Helló", "Szia", "Cső"],
    "cső": ["Hello", "Helló", "Szia", "Cső"],
    "cso": ["Hello", "Helló", "Szia", "Cső"],
    "csao": ["Hello", "Helló", "Szia", "Cső"],
    "mizu": ["Semmi veled?", "Semmi", "Szarul"],
    "hogy vagy": ["Semmi veled?", "Semmi", "Szarul"],
    "mi a helyzet": ["Semmi veled?", "Semmi", "Szarul"],
    # "what is your name": ["I am a bot! You can call me anything you like!"],
    # "how can I help you": ["I can assist you with various tasks. Try asking me for help with something!"],

}
@client.event
async def on_message(message):
    channel = message.channel
    messages = []
    admin_id = ADMINID
    
    if message.author == client.user:
        return

    if message.content.startswith('$delete') and message.author.id == admin_id:
        try:
            async for message in channel.history(limit=100):
                messages.append(message)
            for msg in messages:
                time.sleep(random.uniform(0.1, 0.9)
)
                await msg.delete()
                print("The message has been deleted.")
                
            # message = await channel.fetch_message(1159083911549300766)
            # await message.delete()
            # print("The message has been deleted.")
        except discord.HTTPException:
            pass
            
    for user in message.mentions:
        if user.id == client.user.id:
            msg = message.content.lower()
            # data = {
                # "prompt": msg,
                # "max_tokens": 150,
                # "temperature": 0.7,
                # "model", "gpt-3.5-turbo",
            # }
            response = requests.post(api_url, headers=headers, json={'prompt': msg, 'max_tokens': 100})
            if response.status_code == 200:
                data = response.json()
                response_text = data['choices'][0]['text'].strip()
                await message.channel.send(response_text)
            else:
                await message.channel.send('An error occurred while processing your request. Please try again later.')
            # await message.channel.send(chat_response)
            # reply = ""
            # print( ' uzenet: ', msg )
            # for key, value in responses.items():
                # print( key, value )
                # if key in msg:
                    # print( 'FOUND KEY' )
                    # reply = random.choice(responses[ key ])
                    # await message.channel.send( reply )
                    # return
            # if any(word in msg for word in responses.keys()):
                # await message.channel.send(random.choice(responses[word]))
            
client.run("TOKENS")

