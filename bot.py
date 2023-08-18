import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot(token):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return


        # print {username} sent {message} in {channel}
        print(f'{message.author} sent {message.content} in {message.channel}')
        
        is_private = isinstance(message.channel, discord.channel.DMChannel)
        await send_message(message, message.content, is_private)

    client.run(token)