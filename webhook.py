import discord
import requests

webhook_url = webook

data = {
    "embeds": [
    {
        "title": "Ne beszélj csúnyán",
        "color": discord.Color.blue().value,
        "description": "** !!! **",
        "image": {
            "url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Ff1%2Ff6%2F41%2Ff1f641352c63ff033345538a8af6559f.jpg&f=1&nofb=1&ipt=1a7e3f3689b54d2e01b9bfd2fd822fda002424dde39c5b7396787112d601579f&ipo=images"
        }
    }
    ]
}

requests.post(webhook_url, json=data)