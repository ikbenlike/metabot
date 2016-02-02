import discord
import requests
import subprocess

client = discord.Client()
user = os.environ.get("DISCORD_USER", None)
password = os.environ.get("DISCORD_PASSWORD", None)

@client.event
def on_message(message):
	if message.content.startswith('$tart'):
		if message.author.id == '125422419736395777':
			subprocess.call(['python3', 'metabot.py'], universal_newlines=True)
			client.send_message(message.channel, 'MetaBot started')
		else:
			client.send_message(message.channel, 'you are not allowed to do that')

@client.event
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run()
