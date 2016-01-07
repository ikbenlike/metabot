import discord

client = discord.Client()

user = os.environ.get("DISCORD_USER", None)
password = os.environ.get("DISCORD_PASSWORD", None)

if not user or not password:
    raise Exception("Your Discord login details are missing inside the enviornment. " +
                    "Please set DISCORD_USER and DISCORD_PASSWORD before running this bot.")

@client.event
def on_message(message):
    if message.content.startswith('$about'):
        client.send_message(message.channel, 'this bot can be used to read metadata from an image')

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
