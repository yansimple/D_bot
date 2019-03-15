import discord

token ='NTUwNjk3OTk4NTU2ODU2MzMw.D1pwrg.GVnAGTwneWfj_guSjJkvsuR3Xxs'

client = discord.Client()

@client.event
async def on_ready():
    print("Ready to die!")
    #await client.change_presence(game=discord.Game(name="Make some pain"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "hello":
        await client.send_message(message.channel, "hola!")
client.run(token)
