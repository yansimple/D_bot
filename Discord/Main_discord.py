from discord.ext import commands
prefix = "?"
bot = commands.Bot(command_prefix=prefix)

TOKEN = "NTUwNjk3OTk4NTU2ODU2MzMw.D1pwrg.GVnAGTwneWfj_guSjJkvsuR3Xxs"

@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.event
async def on_message(message):
    print("The message's content was", message.content)


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


bot.run(TOKEN)
