import discord
import requests
import subprocess
import sys
import os
import command
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


commands = ('``` \nabout				   about this bot\n'
				 'summary				 tell someone to read summary\n'
				 'wiki					link to wiki\n'
				 'source				   displays source\n'
				 'linux				   link to commandline guide\n'
				 '!bots/;bots			 prints bots\n'
				 'new					 tells new guy what to do\n'
				 'ping 				   ping a site (currently only for owner)\n'
				 'host 				   find out the IP address of a site\n'
				 'exit					exits bot (only for owner)\n'
				 'kill 				   exits wrapper (only for owner)\n'
				 'echo 				   repeats a message\n'
				 'game 				   set game (only for owner)\n'
				 'lmgtfy 				 search for something on google\n'
				 'report 				 report an error in the bot\n'
				 'clear -t/-l/-erl		clear terminal with -t, log with -l and errorlog with -erl (owner only)\n'
				 'send -l/-erl/-a		 send log with -l, errorlog with -erl and both with -a (owner only)\n'
				 'ucommands			   print useless commands```'
			)

commandsu = ('``` \n$meme		linksto very funny memes \n'
					'$upvote	  prints +1\n'
					'$downvote	prints -1\n'
					'$repost	  prints this is a repost bitch\n'
					'$hame		really funny gif\n'
					'$kynet	   terminator reference\n'
					'$wam		 dedotated wam\n```'
			)

client = discord.Client()

@client.event
async def on_message(message):
	global prefix
	channel = message.channel
	command.actLog(client, channel, message)
	if message.content.startswith(prefix + 'about'):
		await client.send_message(message.channel, 'can ping and host')
	elif message.content.startswith(prefix + 'meme'):
		await client.send_message(message.channel, 'bit.ly/1ITzC4D')
	elif message.content.startswith(prefix + 'summary'):
		await client.send_message(message.channel, 'read #summary before asking stuff!')
	elif message.content.startswith(prefix + 'wiki'):
		await client.send_message(message.channel, 'http://wiki.databutt.com/index.php?title=Main_Page')
	elif message.content.startswith(prefix + 'source'):
		await command.comSource(client, channel, message)
	elif message.content.startswith(prefix + 'ping'):
		await command.comPing(client, channel, message)
	elif message.content.startswith(prefix + 'host'):
		await command.comHost(client, channel, message)
	elif message.content.startswith(prefix + 'upvote'):
		await command.comUpvote(client, channel, message)
	elif message.content.startswith(prefix + 'downvote'):
		await client.send_message(message.channel, '-1')
	elif message.content.startswith(prefix + 'repost'):
		await client.send_message(message.channel, 'thats a repost bitch')
	elif message.content.startswith(prefix + 'linux'):
		await client.send_message(message.channel, 'https://www.codecademy.com/learn/learn-the-command-line')
	elif message.content.startswith('!bots'):
		await client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith(prefix + 'bots'):
		await client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith(';bots'):
		await client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith(prefix + 'new'):
		await client.send_message(message.channel, '``` \n read #rules for the rules \n read #summary for the summary \n read tools for useful tools \n ```')
	elif message.content.startswith(prefix + 'shame'):
		await command.comShame(client, channel, message)
	elif message.content.startswith(prefix + 'skynet'):
		await command.comSkynet(client, channel, message)
	elif message.content.startswith(prefix + 'garage'):
		await command.comGarage(client, channel, message)
	elif message.content.startswith(prefix + 'wam'):
		await command.comWam(client, channel, message)
	elif message.content.startswith(prefix + 'toomuch'):
		await client.send_message(message.channel, 'https://youtu.be/Nar-uT50-pM')
	elif message.content.startswith(prefix + 'commands'):
		await client.send_message(message.channel, 'my prefix is "' + prefix + '"')
		await client.send_message(message.channel, commands)
	elif message.content.startswith(prefix + 'ucommands'):
		await client.send_message(message.channel, commandsu)
	elif message.content.startswith(prefix + 'exit'):
		await command.comExit(client, channel, message)
	elif message.content.startswith(prefix + 'echo'):
		await command.comEcho(client, channel, message)
	elif message.content.startswith(prefix + 'game'):
		await command.comGame(client, channel, message)
	elif message.content.startswith(prefix + 'lmgtfy '):
		await command.comLmgtfy(client, channel, message)
	elif message.content.startswith(prefix + 'report'):
		await command.actError(client, channel, message)
	elif message.content.startswith(prefix + 'kappa'):
		await command.comKappa(client, channel, message)
	elif message.content.startswith(prefix + 'no'):
		await command.comNo(client, channel, message)
	elif message.content.startswith('#summary'):
		await command.comSummary(client, channel, message)
	elif message.content.startswith(prefix + 'sandstorm'):
		await command.comDarude(client, channel, message)
	elif message.content.startswith(prefix + 'nuke'):
		await command.comNuke(client, channel, message)
	elif message.content.startswith(prefix + 'spam'):
		await command.comSpam(client, channel, message)
	elif message.content.startswith(prefix + 'strawman'):
		await command.comStrawman(client, channel, message)
	elif message.content.startswith(prefix + 'narude'):
		await command.comNarude(client, channel, message)
	elif message.content.startswith(prefix + 'clear'):
		await command.actClear(client, channel, message)
	elif message.content.startswith(prefix + 'send'):
		await command.actSend(client, channel, message)
	elif message.content.startswith(prefix + 'wizard'):
		await command.comWizard(client, channel, message)
	elif message.content.startswith(prefix + 'hogwarts'):
		await command.comHogwarts(client, channel, message)
	elif message.content.startswith(prefix + 'nice'):
		await command.comNoice(client, channel, message)
	elif message.content.startswith(prefix + 'nigif'):
		await command.comNigif(client, channel, message)
	elif message.content.startswith(prefix + 'glory'):
		await command.comGlory(client, channel, message)
	elif message.content.startswith(prefix + 'log'):
		await command.actSwitchLog(client, channel, message)
	elif message.content.startswith(prefix + 'pm'):
		await command.comPM(client, channel, message)
	elif message.content.startswith(prefix + 'id'):
		await command.comID(client, channel, message)
	elif message.content.startswith(prefix + 'bing'):
		await command.comBing(client, channel, message)
	elif message.content.startswith(prefix + 'duck'):
		await command.comDuck(client, channel, message)
	elif message.content.startswith(prefix + 'puppet'):
		await command.comPuppet(client, channel, message)
	elif message.content.startswith(prefix + 'hobbits'):
		await command.comHobbits(client, channel, message)
	elif message.content.startswith(prefix + 'rum'):
		await command.comRum(client, channel, message)
	elif message.content.startswith(prefix + 'troll'):
		command.comTroll(client, channel, message)
	elif message.content.startswith(prefix + 'boyz'):
		await command.comBoyz(client, channel, message)
	elif message.content.startswith(prefix + 'prefix'):
		await command.actPrefix(client, channel, message)
		with open("config/prefix.txt") as myfile:
			prefix=myfile.read().replace('\n', '')
	if '<@' + client.user.id + '>' in message.content:
		await command.comOnmention(client, channel, message)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print('----MetaBot has started----')

client.run(inEmail, inPassword)
