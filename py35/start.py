import discord
import requests
import subprocess
import command
import sys
import os
import asyncio


inEmail = input("email: ")
inPassword = input("password: ")
if os.name == "nt":
	os.system("cls")
elif os.name == "posix":
	os.system('clear')


with open("config/prefix.txt") as myfile:
    prefix=myfile.read().replace('\n', '')


client = discord.Client()


@client.event
async def on_message(message):
	channel = message.channel
	off = False
	if off != True:
		if message.content.startswith(prefix + 'start'):
			if message.author.id == command.ownerID:
				p = subprocess.Popen(["python3.5", "metabot.py"])
				while p.poll() is None:
					await asyncio.sleep(1)
				return_code = p.poll()
				off = False
			else:
				await command.actNoperm(client, channel, message)
		if message.content.startswith(prefix + 'kill'):
			await command.comExit(client, channel, message)
			off = True


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


client.run(inEmail, inPassword)
