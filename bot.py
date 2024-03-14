import discord
from discord.ext import commands
from discordLevelingSystem import DiscordLevelingSystem, LevelUpAnnouncement, RoleAward


from config import DISCORD_BOT_TOKEN

intents = discord.Intents.default()
intents.messages = True 
intents.message_content = True 

bot = commands.Bot(..., intents=discord.Intents(messages=True, guilds=True, members=True))

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event

async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('World!')

bot.run(DISCORD_BOT_TOKEN)
