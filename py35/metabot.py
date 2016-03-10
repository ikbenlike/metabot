import discord
import requests
import subprocess
import threading
import sys
import sh
import os
import command
import asyncio


inEmail = input("email: ")
inPassword = input("password: ")
os.system('clear')
prefix = "$"


commands = ('``` \n$about				   about this bot\n'
				 '$summary				 tell someone to read summary\n'
				 '$wiki					link to wiki\n'
				 '$ource				   displays source\n'
				 '$linux				   link to commandline guide\n'
				 '!bots/;bots/$bots		prints bots\n'
				 '$new					 tells new guy what to do\n'
				 '$ping 				   ping a site (currently only for owner)\n'
				 '$host 				   find out the IP address of a site\n'
				 '$exit					exits bot (only for owner)\n'
				 '$kill 				   exits wrapper (only for owner)\n'
				 '$echo 				   repeats a message\n'
				 '$game 				   set game (only for owner)\n'
				 '$lmgtfy 				 search for something on google\n'
				 '$report 				 report an error in the bot\n'
				 '$clear -t/-l/-erl		clear terminal with -t, log with -l and errorlog with -erl (owner only)\n'
				 '$end -l/-erl/-a		  send log with -l, errorlog with -erl and both with -a (owner only)\n'
				 '$ucommands			   print useless commands```'
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
	channel = message.channel
	command.actLog(client, channel, message)
	if message.content.startswith(prefix + 'about'):
		await client.send_message(message.channel, 'can ping and host')
	elif message.content.startswith(prefix + 'meme'):
		await client.send_message(message.channel, 'bit.ly/1ITzC4D')
	elif message.content.startswith(prefix + 'summary'):
		await client.send_message(message.channel, 'read #summary before asking stuff!')
	elif message.content.startswith('$wiki'):
		await client.send_message(message.channel, 'http://wiki.databutt.com/index.php?title=Main_Page')
	elif message.content.startswith('$ource'):
		await command.comSource(client, channel, message)
	elif message.content.startswith('$ping'):
		await command.comPing(client, channel, message)
	elif message.content.startswith('$host'):
		await command.comHost(client, channel, message)
	elif message.content.startswith('$upvote'):
		await command.comUpvote(client, channel, message)
	elif message.content.startswith('$downvote'):
		await client.send_message(message.channel, '-1')
	elif message.content.startswith('$repost'):
		await client.send_message(message.channel, 'thats a repost bitch')
	elif message.content.startswith('$linux'):
		await client.send_message(message.channel, 'https://www.codecademy.com/learn/learn-the-command-line')
	elif message.content.startswith('!bots'):
		await client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith('$bots'):
		await client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith(';bots'):
		await client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith('$new'):
		await client.send_message(message.channel, '``` \n read #rules for the rules \n read #summary for the summary \n read tools for useful tools \n ```')
	elif message.content.startswith('$hame'):
		await command.comShame(client, channel, message)
	elif message.content.startswith('$kynet'):
		await command.comSkynet(client, channel, message)
	elif message.content.startswith('$garage'):
		await command.comGarage(client, channel, message)
	elif message.content.startswith('$wam'):
		await command.comWam(client, channel, message)
	elif message.content.startswith('$toomuch'):
		await client.send_message(message.channel, 'https://youtu.be/Nar-uT50-pM')
	elif message.content.startswith('$commands'):
		await client.send_message(message.channel, commands)
	elif message.content.startswith('$ucommands'):
		await client.send_message(message.channel, commandsu)
	elif message.content.startswith('$exit'):
		await command.comExit(client, channel, message)
	elif message.content.startswith('$echo'):
		await command.comEcho(client, channel, message)
	elif message.content.startswith('$game'):
		await command.comGame(client, channel, message)
	elif message.content.startswith('$lmgtfy '):
		await command.comLmgtfy(client, channel, message)
	elif message.content.startswith('$report'):
		await command.actError(client, channel, message)
	elif message.content.startswith('$kappa'):
		await command.comKappa(client, channel, message)
	elif message.content.startswith('$no'):
		await command.comNo(client, channel, message)
	elif message.content.startswith('#summary'):
		await command.comSummary(client, channel, message)
	elif message.content.startswith('$andstorm'):
		await command.comDarude(client, channel, message)
	elif message.content.startswith('$nuke'):
		await command.comNuke(client, channel, message)
	elif message.content.startswith('$pam'):
		await command.comSpam(client, channel, message)
	elif message.content.startswith('$trawman'):
		await command.comStrawman(client, channel, message)
	elif message.content.startswith('$narude'):
		await command.comNarude(client, channel, message)
	elif message.content.startswith('$clear'):
		await command.actClear(client, channel, message)
	elif message.content.startswith('$end'):
		await command.actSend(client, channel, message)
	elif message.content.startswith('$wizard'):
		await command.comWizard(client, channel, message)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print('----MetaBot has started----')

client.run(inEmail, inPassword)
