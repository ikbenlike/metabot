import discord
import requests
import threading
import subprocess

commands = '``` \n$about	about this bot\n$summary	tell someone to read summary\n$wiki	link to wiki\n$ource	displays source\n$linux	link to commandline guide\n!bots/;bots/$bots	prints bots\n$new	tells new guy what to do\n$ucommandsu	print useless commands```'
commandsu = '``` \n$meme	linksto very funny memes \n$ping	prints pong\n$upvote	prints +1\n$downvote	prints -1\n$repost	prints this is a repost bitch\n$hame	really funny gif\n$kynet	terminator reference\n$wam	dedotated wam\n```'

client = discord.Client()
user = os.environ.get("DISCORD_USER", None)
password = os.environ.get("DISCORD_PASSWORD", None)

@client.event
def on_message(message):
	if message.content.startswith('$about'):
		client.send_message(message.channel, 'this bot can be used to read metadata from an image')
	elif message.content.startswith('$meme'):
		client.send_message(message.channel, 'bit.ly/1ITzC4D')
	elif message.content.startswith('$summary'):
		client.send_message(message.channel, 'read #summary before asking stuff!')
	elif message.content.startswith('$wiki'):
		client.send_message(message.channel, 'http://wiki.databutt.com/index.php?title=Main_Page')
	elif message.content.startswith('$ource'):
		client.send_message(message.channel, 'sourcecode: https://github.com/ikbenlike/metabot.git')
	elif message.content.startswith('$ping'):
		client.send_message(message.channel, 'pong')
	elif message.content.startswith('$meta'):
		client.send_message(message.channel, 'this feature will be implemented later on')
	elif message.content.startswith('$upvote'):
		client.send_message(message.channel, '+1')
	elif message.content.startswith('$downvote'):
		client.send_message(message.channel, '-1')
	elif message.content.startswith('$repost'):
		client.send_message(message.channel, 'thats a repost bitch')
	elif message.content.startswith('$linux'):
		client.send_message(message.channel, 'https://www.codecademy.com/learn/learn-the-command-line')
	elif message.content.startswith('!bots'):
		client.send_message(message.channel, '``` bot that will eventually be able to get metadata from\nimages ```')
	elif message.content.startswith('$bots'):
		client.send_message(message.channel, '``` bot that will eventually be able to get metadata from\nimages ```')
	elif message.content.startswith(';bots'):
		client.send_message(message.channel, '``` bot that will eventually be able to get metadata from\nimages ```')
	elif message.content.startswith('$new'):
		client.send_message(message.channel, '``` \n read #rules for the rules \n read #summary for the summary \n read tools for useful tools \n ```')
	elif message.content.startswith('$hame'):
		client.send_message(message.channel, 'http://i.imgur.com/CFTIRA1.gif')
	elif message.content.startswith('$kynet'):
		client.send_message(message.channel, 'http://www.blastr.com/sites/blastr/files/Terminator-Salvation_0.jpg')
	elif message.content.startswith('$nigger'):
		client.send_message(message.channel, 'https://youtu.be/0yJn-5hpU94')
	elif message.content.startswith('$garage'):
		client.send_message(message.channel, 'https://youtu.be/Cv1RJTHf5fk')
	elif message.content.startswith('$wam'):
		client.send_message(message.channel, 'https://youtu.be/_pVNvSuA2mM')
	elif message.content.startswith('$toomuch'):
		client.send_message(message.channel, 'https://youtu.be/Nar-uT50-pM')
	elif message.content.startswith('$commands'):
		client.send_message(message.channel, commands)
	elif message.content.startswith('$ucommands'):
		client.send_message(message.channel, commandsu)
	elif message.content.startswith('$host'):
		#domain = message.content.split(' ')[1]
		output = subprocess.check_output(['host', '-a', 'google.com'], shell=True, stderr=subprocess.PIPE)
		client.send_message(message.channel, output)
		client.send_message(message.channel, output)
	elif message.content.startswith('$exit'):
		if message.author.id == '125422419736395777':
			client.send_message(message.channel, "why did you kill me?")
			sys.exit(1)
		else:
			client.send_message(message.channel, 'you are not authorized to do that, ' + message.author.name)
	elif message.content.startswith('$echo'):
		if message.author.id != '134727236615012354':
			input_ = message.content
			input_.split(" ")[0]
			args = input_.split(" ")[1:]
			client.send_message(message.channel, (" ".join(args)))

@client.event
def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	game = discord.Game()
	game.name = 'your mom'
	client.change_status(game=game)

client.run()
