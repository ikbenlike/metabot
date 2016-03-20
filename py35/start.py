import discord
import requests
import subprocess
import command
import sys
import os
import asyncio


logInFromFile = True

if logInFromFile == False:
	inEmail = input("email: ")
	inPassword = input("password: ")
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system('clear')
elif logInFromFile == True:
	with open("config/inemail.txt") as loginemail:
		inEmail = loginemail.read().replace('\n', '')
	with open("config/inpassword.txt") as loginpassword:
		inPassword = loginpassword.read().replace('\n', '')


with open("config/prefix.txt") as myfile:
    prefix=myfile.read().replace('\n', '')


client = discord.Client()


@client.event
async def on_message(message):
	channel = message.channel
	off = False
	if off != True:
		if message.content.startswith(prefix + 'start'):
			if message.author.id in command.modIDs:
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
