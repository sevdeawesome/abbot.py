import bot

if __name__ == '__main__':
    # read TOKEN from token.txt
    TOKEN = open('token.txt', 'r').read()
    bot.run_discord_bot(TOKEN)