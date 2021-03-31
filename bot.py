# bot.py
import os

import discord
from dotenv import load_dotenv
#https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-guild

# https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#discord.ext.commands.Bot

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
DEST = os.getenv('DEST')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.content.startswith('$uh'):
        channel = message.channel

        if message.content == '$uh':
            await channel.send('Enter a question with $uh *question here*')
        else:
            await channel.send("""Hello {.author}! Now I\'ll delete your question. A receipt was sent to our staff and direct messaged to you""".format(message))

            for guild in client.guilds:
                if guild.name == GUILD:
                    for c in guild.channels:
                        if c.name == DEST:
                            await c.send('Author: {.author}\n'.format(message) + 'Message:\n' + message.content)
                            await message.author.send("Your message: \n" + message.content)
                            break
                    break
            await message.delete()

client.run(TOKEN)