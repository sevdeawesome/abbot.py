import discord
from discord.ext import commands

# read TOKEN from token.txt
TOKEN = open('token.txt', 'r').read()

# print(TOKEN)

# intents = discord.Intents.default()
# intents.messages = True
# intents.guilds = True

# bot = commands.Bot(command_prefix='!', intents=intents)





intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def test(ctx):
    print("HELLO")
    await ctx.send("HERRO")


@bot.command()
async def join(ctx):
    print("JOIN")
    # await ctx.send("JOIN")


bot.run(TOKEN)
