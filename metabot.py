import discord
import requests
import subprocess
import threading
import sys
import sh
import os
import command


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
				 '$ucommands			   print useless commands```'
			)

commandsu = ('``` \n$meme		linksto very funny memes \n'
					'$ping		prints pong\n'
					'$upvote	  prints +1\n'
					'$downvote	prints -1\n'
					'$repost	  prints this is a repost bitch\n'
					'$hame		really funny gif\n'
					'$kynet	   terminator reference\n'
					'$wam		 dedotated wam\n```'
			)
client = discord.Client()
client.login(inEmail, inPassword)
@client.event
def on_message(message):
	channel = message.channel
	command.actLog(client, channel, message)
	if message.content.startswith(prefix + 'about'):
		client.send_message(message.channel, 'can ping and host')
	elif message.content.startswith(prefix + 'meme'):
		client.send_message(message.channel, 'bit.ly/1ITzC4D')
	elif message.content.startswith(prefix + 'summary'):
		client.send_message(message.channel, 'read #summary before asking stuff!')
	elif message.content.startswith('$wiki'):
		client.send_message(message.channel, 'http://wiki.databutt.com/index.php?title=Main_Page')
	elif message.content.startswith('$ource'):
		command.comSource(client, channel, message)
	elif message.content.startswith('$ping'):
		command.comPing(client, channel, message)
	elif message.content.startswith('$host'):
		command.comHost(client, channel, message)
	elif message.content.startswith('$upvote'):
		command.comUpvote(client, channel, message)
	elif message.content.startswith('$downvote'):
		client.send_message(message.channel, '-1')
	elif message.content.startswith('$repost'):
		client.send_message(message.channel, 'thats a repost bitch')
	elif message.content.startswith('$linux'):
		client.send_message(message.channel, 'https://www.codecademy.com/learn/learn-the-command-line')
	elif message.content.startswith('!bots'):
		client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith('$bots'):
		client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith(';bots'):
		client.send_message(message.channel, '``` can ping and host ```')
	elif message.content.startswith('$new'):
		client.send_message(message.channel, '``` \n read #rules for the rules \n read #summary for the summary \n read tools for useful tools \n ```')
	elif message.content.startswith('$hame'):
		command.comShame(client, channel, message)
	elif message.content.startswith('$kynet'):
		command.comSkynet(client, channel, message)
	elif message.content.startswith('$garage'):
		command.comGarage(client, channel, message)
	elif message.content.startswith('$wam'):
		command.comWam(client, channel, message)
	elif message.content.startswith('$toomuch'):
		client.send_message(message.channel, 'https://youtu.be/Nar-uT50-pM')
	elif message.content.startswith('$commands'):
		client.send_message(message.channel, commands)
	elif message.content.startswith('$ucommands'):
		client.send_message(message.channel, commandsu)
	elif message.content.startswith('$exit'):
		client.send_message(message.channel, "why did you kill me?")
		sys.exit(1)
	elif message.content.startswith('$echo'):
		command.comEcho(client, channel, message)
	elif message.content.startswith('$game'):
		command.comGame(client, channel, message)
	elif message.content.startswith('$lmgtfy '):
		command.comLmgtfy(client, channel, message)
	elif message.content.startswith('$members'):
		members = message.channel.server.members
		client.send_message(message.channel, members)
	elif message.content.startswith('$report'):
		command.actError(client, channel, message)
	elif message.content.startswith('$kappa'):
		command.comKappa(client, channel, message)
	elif message.content.startswith('$no'):
		command.comNo(client, channel, message)
	elif message.content.startswith('#summary'):
		command.comSummary(client, channel, message)
	elif message.content.startswith('$andstorm'):
		command.comDarude(client, channel, message)
	elif message.content.startswith('$nuke'):
		command.comNuke(client, channel, message)
	elif message.content.startswith('$pam'):
		command.comSpam(client, channel, message)
	elif message.content.startswith('$trawman'):
		command.comStrawman(client, channel, message)
	elif message.content.startswith('$narude'):
		command.comNarude(client, channel, message)
	elif message.content.startswith('$clear'):
		command.actClear(client, channel, message)
	elif message.content.startswith('$end'):
		command.actSend(client, channel, message)
	elif message.content.startswith('$wizard'):
		command.comWizard(client, channel, message)

@client.event
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	print('----MetaBot has started----')

client.run()
