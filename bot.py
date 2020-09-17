import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

#Comment Test
TOKEN = ""
client = commands.Bot(command_prefix = '.')
channel_id = 751691937077133385


@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity=discord.Game(name='Coding'))
    
    '''Would set Activity, and set
    activity = discord.Activity(name='Helping Coders...', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)'''
    
@client.event 
async def on_member_join(member):
    print(f"{member} has joined.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left.")

#Auto Voice-pinger
@client.event
async def on_voice_state_update(member, before, after):
    
    if before.channel is None and after.channel is not None:
        channel = client.get_channel(channel_id)
        print("member joined Vc")
        members = channel.members
        member_names = '\n'.join([x.name for x in members])

        await channel.send(f'@everyone')


    elif before.channel is not None and after.channel is None:
        channel = client.get_channel(channel_id)
        print("member left Vc")
        await channel.purge(limit = 10, check = lambda m: m.author == client.user)

    


@client.command()
async def repeat(ctx, x):
    await ctx.send(f"Hey, {x}")

@client.command(aliases = ["alert"])
async def ping(ctx):
    await ctx.send("@everyone")

@client.command(aliases = ['del'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)   



client.run(TOKEN)

