import discord
from discord.ext.commands import bot

client = discord.Client()

#good morning  I love you 

#Confirms the bot is online
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$alex'):
        await message.channel.send('Alex is a bitch!')

@client.event   #Event to detect when a user joins the server
async def on_member_join(member):
    await member.send('Hi! Welcome to our server!')
    verifiedRole = discord.utils.get(member.guild.roles, id=842062523041185802)
    await member.add_roles(verifiedRole)

client.run('Your Bot Token Here')





