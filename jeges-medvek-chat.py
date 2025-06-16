import discord
import requests

webhook_url = webook

data = {
    "embeds": [
    {
        "title": "Boldog Karácsonyt",
        "color": discord.Color.blue().value,
        "description": "",
        "image": {
            "url": "https://i.pinimg.com/originals/d4/6b/db/d46bdb39f104f17641b540bbfe8a35f2.gif"
        }
    }
    ]
}

requests.post(webhook_url, json=data)