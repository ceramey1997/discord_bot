from discord.ext import commands
import asyncio
prefix = "?"
bot = commands.Bot(command_prefix=prefix)


@bot.event
@ascyncio.coroutine
def on_ready():
    print("Everything's all ready to go~")


@bot.event
@ascyncio.coroutine
def on_message(message):
    print("The message's content was", message.content)


@bot.command()
@ascyncio.coroutine
def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
@ascyncio.coroutine
def echo(ctx, *, content:str):
    await ctx.send(content)


bot.run(TOKEN)