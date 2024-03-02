import discord
from discord.ext import commands

from config import DISCORD_BOT_TOKEN

intents = discord.Intents.default()
intents.messages = True  # If you need to listen to messages
intents.message_content = True 

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event

async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    # Responds with 'Pong!' to '!ping'
    await ctx.send('Pong!')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run(DISCORD_BOT_TOKEN)