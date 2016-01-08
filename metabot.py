import discord
import requests

client = discord.Client()
user = os.environ.get("DISCORD_USER", None)
password = os.environ.get("DISCORD_PASSWORD", None)

@client.event
def on_message(message):
    if message.content.startswith('$about'):
        client.send_message(message.channel, 'this bot can be used to read metadata from an image')
    if message.content.startswith('$meme'):
        client.send_message(message.channel, 'bit.ly/1ITzC4D')
    if message.content.startswith('$summary'):
        client.send_message(message.channel, 'read #summary before asking stuff!')
    if message.content.startswith('$wiki'):
        client.send_message(message.channel, 'http://wiki.databutt.com/index.php?title=Main_Page')
    if message.content.startswith('$ource'):
        client.send_message(message.channel, 'sourcecode: https://github.com/ikbenlike/metabot.git')
    if message.content.startswith('$ping'):
        client.send_message(message.channel, 'pong')

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
