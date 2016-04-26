import discord
import requests
import subprocess
import command
import sys
import os
import asyncio


logInFromFile = True

if logInFromFile == False:
	inToken = input("token: ")
	if os.name == "nt":
		os.system("cls")
	elif os.name == "posix":
		os.system('clear')
elif logInFromFile == True:
	with open("config/intoken.txt") as intoken:
		inToken = intoken.read().replace('\n', '')


prefixFile = open("config/prefix.txt", "r")
prefix = prefixFile.read().replace("\n", "")

modIDList = open("config/mods.txt", "r")
modIDs = modIDList.read().replace("\n", " ")

client = discord.Client()


@client.event
async def on_message(message):
	global prefix
	global modIDs
	global modIDList
	global prefixFile
	channel = message.channel
	off = False
	if off != True:
		if message.content.startswith(prefix + 'start'):
			if message.author.id in modIDs:
				p = subprocess.Popen(["python3.5", "metabot.py"])
				while p.poll() is None:
					await asyncio.sleep(1)
				return_code = p.poll()
				off = False
			else:
				await command.actNoperm(client, channel, message)
		elif message.content.startswith(prefix + 'kill'):
			await command.comExit(client, channel, message)
			off = True
		elif message.content.startswith(prefix + "mod"):
			modIDList.close()
			modIDList = open("config/mods.txt", "r")
			modIDs = modIDList.read().replace("\n", " ")
		elif message.content.startswith(prefix + "prefix"):
			prefixFile.close()
			prefixFile = open("config/prefix.txt", "r")
			prefix = prefixFile.read().replace("\n", "")




@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


client.run(inToken)
