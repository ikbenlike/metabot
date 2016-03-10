import discord
import requests
import subprocess
import command
import sys
import os
import asyncio


inEmail = input("email: ")
inPassword = input("password: ")
os.system('clear')

client = discord.Client()

@client.event
async def on_message(message):
	channel = message.channel
	off = False
	if off != True:
		if message.content.startswith('$tart'):
			if message.author.id == '125422419736395777':
				subprocess.call(['python3.5', 'metabot.py'], universal_newlines=True)
				off = True
			else:
				await command.actNoperm(client, channel, message)
		if message.content.startswith('$kill'):
			await command.comExit(client, channel, message)



@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(inEmail, inPassword)
