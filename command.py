"""
commands module written for metabot

by thewatcher

have fun roasting me lel
"""
import discord
import requests
import subprocess
import sys

#input = raw_input

def actNoperm(client, channel, message):
	client.send_message(message.channel, 'you are not authorized to do that, ' + message.author.name)



def actLog(client, channel, message):
	msgData = message.author.name + ' ' + message.author.id + ' ' + message.content + '\n'
	msgData = msgData.replace('\n', '\n        ')
	print(msgData)
	logs = open("logs.txt", "a")
	logs.write(msgData)



def actError(client, channel, message):
	msgData = message.author.name + ' ' + message.author.id + ' ' + message.content + '\n'
	er_report = open("report-error.txt", "a")
	er_report.write(msgData)



def comAbout(client, channel, message):
	client.send_message(message.channel, " ``` can ping and host (currently only for watcher)``` ")



def comSummary(client, channel, message):
	client.send_message(message.channel, "read #summary before asking stuff!")



def comWiki(client, channel, message):
	client.send_message(message.channel, "http://wiki.databutt.com/index.php?title=Main_Page")



def comSource(client, channel, message):
	client.send_message(message.channel, " ```source: https://github.com/ikbenlike/metabot.git (probably out of date)``` ")



def comPing(client, channel, message):
	if message.author.id == '125422419736395777':
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		site = (' '.join(args))
		ping = subprocess.check_output(['ping', '-c 3', site], universal_newlines=True)
		client.send_message(message.channel, '```' + ping + '```')
	else:
		client.send_message(message.channel, "you're not allowed to do that, " + message.author.name)



def comHost(client, channel, message):
	if message.author.id == '125422419736395777':
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		site = (' '.join(args))
		host = subprocess.check_output(['host', site], universal_newlines=True)
		client.send_message(message.channel, '```' + host + '```')
	else:
		client.send_message(message.channel, "you're not allowed to do that, " + message.author.name)



def comUpvote(client, channel, message):
	client.send_message(message.channel, "+1")



def comDownvote(client, channel, message):
	client.send_message(message.channel, "-1")



def comRepost(client, channel, message):
	client.send_message(message.channel, 'thats a repost bitch')



def comBots():
	client.send_message(message.channel, '``` can ping and host ```')



def comShame(client, channel, message):
	client.send_message(message.channel, 'http://i.imgur.com/CFTIRA1.gif')



def comGame(client, channel, message):
	input_ = message.content
	input_.split(" ")[0]
	stuff = input_.split(" ")[1:]
	gameName = (" ".join(stuff))
	game = discord.Game()
	game.name = gameName
	client.change_status(game=game)
	client.send_message(message.channel, 'game has been set to ' + gameName)



def comExit(client, channel, message):
	client.send_message(message.channel, "why did you kill me?")
	sys.exit(1)



def comPing(client, channel, message):
	input_ = message.content
	input_.split(" ")[0]
	args = input_.split(" ")[1:]
	site = (' '.join(args))
	ping = subprocess.check_output(['ping', '-c 3', site], universal_newlines=True)
	client.send_message(message.channel, '```' + ping + '```')



def comHost(client, channel, message):
	input_ = message.content
	input_.split(" ")[0]
	args = input_.split(" ")[1:]
	site = (' '.join(args))
	host = subprocess.check_output(['host', site], universal_newlines=True)
	client.send_message(message.channel, '```' + host + '```')



def comSkynet(client, channel, message):
	client.send_message(message.channel, 'http://www.blastr.com/sites/blastr/files/Terminator-Salvation_0.jpg')



def comGarage(client, channel, message):
	client.send_message(message.channel, 'https://youtu.be/Cv1RJTHf5fk')



def comWam(client, channel, message):
	client.send_message(message.channel, 'https://youtu.be/_pVNvSuA2mM')



def comKappa(client, channel, message):
	client.send_message(message.channel, "http://apollo-na-uploads.s3.amazonaws.com/1437444611/kappa.jpg")



def comLmgtfy(client, channel, message):
	input_ = message.content
	input_.split(' '[0])
	searchString = input_.split(' ')[1:]
	search = ('+'.join(searchString))
	client.send_message(message.channel, 'http://lmgtfy.com/?q=' + search)



def comEcho(client, channel, message):
	if message.author.id != client.user.id:
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		client.send_message(message.channel, (" ".join(args)))



def comDarude(client, channel, message):
	client.send_message(message.channel, "https://youtu.be/y6120QOlsfU")


def comNo(client, channel, message):
	client.send_message(message.channel, "http://giphy.com/gifs/the-office-no-steve-carell-12XMGIWtrHBl5e")



def comSummary(client, channel, message):
	client.send_message(message.channel, "Metabot is an amazing python program, made by TheWatcher, that has commands that can can be executed with $ and a pre-made command")



def comSandstorm(client, channel, message):
	client.send_message(message.channel, "https://youtu.be/y6120QOlsfU")



def comNuke(client, channel, message):
	client.send_message(message.channel, "https://giphy.com/gifs/reaction-XevXoNu5WZxe0")



def comSpam(client, channel, message):
	client.send_message(message.channel, "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Spam_can.png/220px-Spam_can.png")



def comStrawman(client, channel, message):
	client.send_message(message.channel, "https://youtu.be/WPMcm7lef9Y")
