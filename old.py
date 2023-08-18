import discord
from discord.ext import commands
import random
import asyncio

DEFAULT_REST_TIME = 15
DEFAULT_EXERCISE_TIME = 45
DEFAULT_NUM_EXERCISES = 8


ab_exercises = [
    "Crunches",
    "Heels to the Heavens",
    "Flutter Kicks",
    "Russian Twists",
    "V ups",
    "starfish crunches",
    "jack knives",
    # "plank",
    "bicycle crunches",
    "figure 8"
]





TOKEN = open('token.txt', 'r').read()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)




@bot.command()
async def test(ctx):
    print("HELLO")
    await ctx.send("HERRO")


@bot.command()
async def join(ctx, minutes=DEFAULT_NUM_EXERCISES, plank=False):
    channel = ctx.author.voice.channel
    await channel.connect()
    print("JOINED VOICE CHANNEL")

    await ctx.send(f"Joined {channel} for {minutes} minutes")

    if plank:
        await ctx.send("Plank time will be 1 minute")

    random.shuffle(ab_exercises)

    # count down from 5
    for i in range(5):
        await ctx.send(f"{5-i}", tts=True)
        await asyncio.sleep(1)

    for i in range(minutes):
        await ctx.send(f"{i+1}. {ab_exercises[i]} in 5 seconds", tts=True)
        await asyncio.sleep(5)

        await ctx.send(f"{ab_exercises[i]} GO GO GO", tts=True)
        await asyncio.sleep(DEFAULT_EXERCISE_TIME)

        await ctx.send(f"Rest for {DEFAULT_REST_TIME} seconds", tts=True)

        await asyncio.sleep(DEFAULT_REST_TIME - 5)

    await ctx.send("Finished nightly abs. congrats brvther. wagmi", tts=True)

        



bot.run(TOKEN)
