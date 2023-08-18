import bot

if __name__ == '__main__':
    TOKEN = open('token.txt', 'r').read()
    bot.run_discord_bot(TOKEN)