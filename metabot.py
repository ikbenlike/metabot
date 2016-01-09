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
    if message.content.startswith('$meta'):
	    client.send_message(message.channel, 'this feature will be implemented later on')
	if message.content.startswith('$commands'):
		client.send_message(message.channel, 'this feature will be implemented later on')
	if message.content.startswith('$upvote'):
		client.send_message(message.channel, '+1')
	if message.content.startswith('$downvote'):
		client.send_message(message.channel, '-1')
	if message.content.startswith('$repost'):
		client.send_message(message.channel, 'thats a repost bitch')
	if message.content.startswith('$linux'):
		client.send_message(message.channel, 'https://www.codecademy.com/learn/learn-the-command-line')
	if message.content.startswith('!bots'):
		client.send_message(message.channel, '``` bot that will eventually be able to get metadata from\nimages ```')
	if message.content.startswith('$bots'):
		client.send_message(message.channel, '``` bot that will eventually be able to get metadata from\nimages ```')
	if message.content.startswith('$new'):
		client.send_message(message.channel, '``` \n read #rules for the rules \n read #summary for the summary \n read tools for useful tools \n ```')

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
