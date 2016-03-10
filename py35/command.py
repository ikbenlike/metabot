"""
commands module written for metabot

by thewatcher

have fun roasting me lel
"""
import discord
import requests
import subprocess
import sys
import socket
import os
import asyncio

ownerID = "125422419736395777"

async def actNoperm(client, channel, message):
	await client.send_message(message.channel, 'you are not authorized to do that, ' + message.author.name)



def actLog(client, channel, message):
	msgData = message.author.name + ' ' + message.author.id + ' ' + message.content + '\n'
	msgData = msgData.replace('\n', '\n        ')
	print(msgData)
	logs = open("logs.txt", "a")
	logs.write(msgData)



async def actError(client, channel, message):
	msgData = message.author.name + ' ' + message.author.id + ' ' + message.content + '\n'
	er_report = open("report-error.txt", "a")
	er_report.write(msgData)
	er_report.close()



async def comAbout(client, channel, message):
	await client.send_message(message.channel, " ``` can ping and host (currently only for watcher)``` ")



async def comSummary(client, channel, message):
	await client.send_message(message.channel, "read #summary before asking stuff!")



async def comWiki(client, channel, message):
	await client.send_message(message.channel, "http://wiki.databutt.com/index.php?title=Main_Page")



async def comSource(client, channel, message):
	await client.send_message(message.channel, " ```source: https://github.com/ikbenlike/metabot.git (probably out of date)``` ")



async def comPing(client, channel, message):
	if message.author.id == ownerID:
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		site = (' '.join(args))
		ping = subprocess.check_output(['ping', '-c 3', site], universal_newlines=True)
		await client.send_message(message.channel, '```' + ping + '```')
	else:
		await actNoperm(client, channel, message)



async def comUpvote(client, channel, message):
	await client.send_message(message.channel, "+1")



async def comDownvote(client, channel, message):
	await client.send_message(message.channel, "-1")



async def comRepost(client, channel, message):
	await client.send_message(message.channel, 'thats a repost bitch')



async def comBots():
	await client.send_message(message.channel, '``` can ping and host ```')



async def comShame(client, channel, message):
	await client.send_message(message.channel, 'http://i.imgur.com/CFTIRA1.gif')



async def comGame(client, channel, message):
	if message.author.id == ownerID:
		input_ = message.content
		input_.split(" ")[0]
		stuff = input_.split(" ")[1:]
		gameName = (" ".join(stuff))
		game = discord.Game()
		game.name = gameName
		await client.change_status(game=game)
		await client.send_message(message.channel, 'game has been set to ' + gameName)
	else:
		await actNoperm(client, channel, message)



async def comExit(client, channel, message):
	await client.send_message(message.channel, "why did you kill me?")
	print("[exiting metabot]")
	await client.logout()



async def comPing(client, channel, message):
	input_ = message.content
	input_.split(" ")[0]
	args = input_.split(" ")[1:]
	site = (' '.join(args))
	ping = subprocess.check_output(['ping', '-c 3', site], universal_newlines=True)
	await client.send_message(message.channel, '```' + ping + '```')



async def comHost(client, channel, message):
	input_ = message.content
	input_.split(" ")[0]
	args = input_.split(" ")[1:]
	site = (' '.join(args))
	host = "\n".join([s[4][0] for s in socket.getaddrinfo(site, "443")])
	await client.send_message(message.channel, '```' + host + '```')



async def comSkynet(client, channel, message):
	await client.send_message(message.channel, 'http://www.blastr.com/sites/blastr/files/Terminator-Salvation_0.jpg')



async def comGarage(client, channel, message):
	await client.send_message(message.channel, 'https://youtu.be/Cv1RJTHf5fk')



async def comWam(client, channel, message):
	await client.send_message(message.channel, 'https://youtu.be/_pVNvSuA2mM')



async def comKappa(client, channel, message):
	await client.send_message(message.channel, "http://apollo-na-uploads.s3.amazonaws.com/1437444611/kappa.jpg")



async def comLmgtfy(client, channel, message):
	input_ = message.content
	input_.split(' '[0])
	searchString = input_.split(' ')[1:]
	search = ('+'.join(searchString))
	await client.send_message(message.channel, 'http://lmgtfy.com/?q=' + search)



async def comEcho(client, channel, message):
	if message.author.id != client.user.id:
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		await client.send_message(message.channel, (" ".join(args)))



async def comDarude(client, channel, message):
	await client.send_message(message.channel, "https://youtu.be/y6120QOlsfU")


async def comNo(client, channel, message):
	await client.send_message(message.channel, "http://giphy.com/gifs/the-office-no-steve-carell-12XMGIWtrHBl5e")



async def comSummary(client, channel, message):
	await client.send_message(message.channel, "Metabot is an amazing python program, made by TheWatcher, that has commands that can can be executed with $ and a pre-made command")



async def comSandstorm(client, channel, message):
	await client.send_message(message.channel, "https://youtu.be/y6120QOlsfU")



async def comNuke(client, channel, message):
	await client.send_message(message.channel, "https://giphy.com/gifs/reaction-XevXoNu5WZxe0")



async def comSpam(client, channel, message):
	await client.send_message(message.channel, "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Spam_can.png/220px-Spam_can.png")



async def comStrawman(client, channel, message):
	await client.send_message(message.channel, "https://youtu.be/WPMcm7lef9Y")



async def comNarude(client, channel, message):
	await client.send_message(message.channel, "https://youtu.be/1gVMv1pw4Gw")



async def actClear(client, channel, message):
	if message.author.id == ownerID:
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		if "-t" in args:
			if os.name == "nt":
				os.system("cls")
			elif os.name == "posix":
				os.system("clear")
		if "-l" in args:
			logs = open("logs.txt", "w")
			logs.write("[reset logs]\n")
			logs.close()
		if "-erl" in args:
			er_report = open("report-error.txt", "w")
			er_report.write("[reset logs]\n")
			er_report.close()
	else:
		await actNoperm(client, channel, message)



async def actSend(client, channel, message):
	if message.author.id == ownerID:
		input_ = message.content
		input_.split(" ")[0]
		args = input_.split(" ")[1:]
		if "-l" in args:
			await client.send_file(message.channel, "logs.txt")
		if "-erl" in args:
			await client.send_file(message.channel, "report-error.txt")
		if "-a" in args:
			await client.send_file(message.channel, "logs.txt")
			await client.send_file(message.channel, "report-error.txt")
	else:
		await actNoperm(client, channel, message)



async def comWizard(client, channel, message):
	await client.send_message(message.channel, "https://youtu.be/tKNhPpUR0Pg")
