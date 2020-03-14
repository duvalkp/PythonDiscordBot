import discord
import youtube_dl
from discord.ext import commands
from YTAPI import search_with_api

#This is the token for the bot provided by discord to identify the program as
#the application registered with a discord account. It has been censored for security.
t = '*Censored*'
#This line sets the phrase to identify the message in a server as a command
cb = commands.Bot(command_prefix="!c")
#For play command
players = {}
global currently_in_channel

#This function sets the text under the bots name where the name of game being played usually is.
@cb.event
async def on_ready():
    await cb.change_presence(game=discord.Game(name='Catbot'))
    print('Bot has started')

#This is a simple command to test if the bot is online. The bot will respond with a message.
@cb.command()
async def ping():
    await cb.say('here')

#Another simple command left in to demonstrate the bot can perform math operations.
@cb.command()
async def TESTADDITION(left : int, right : int):
    try:
        result = left + right

    except Exception:
        await cb.say('Input was not int or wrong format')
        return

    await cb.say(result)

#does not work
@cb.command(pass_context=True)
async def kick(ctx, name: discord.User):
    await cb.kick(name)
    await cb.say('Kicked' + name)

@cb.command(pass_context=True)
async def join(ctx):
    voice_channel = ctx.message.author.voice.voice_channel
    await cb.join_voice_channel(voice_channel)

@cb.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = cb.voice_client_in(server)
    await voice_client.disconnect()
    currently_in_channel = False

##@cb.command(pass_context=True)
##async def newchannel()

@cb.command(pass_context=True)
async def play(ctx, *msg):
    
    query = " ".join(msg)
    #await cb.say(query)
    
    url = search_with_api(query) # youtube api search and get first result

    #await cb.say("This was requested: "+query)
    #await cb.say("This was found: "+url)
    server = ctx.message.server
    if cb.is_voice_connected(server) == False:
        voice_channel = ctx.message.author.voice.voice_channel #join voice cahnnel
        await cb.join_voice_channel(voice_channel)
     #   currently_in_channel = True
    
    
    voice_client = cb.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

#KEEP AT BOTTOM ALWAYS
cb.run(t)

