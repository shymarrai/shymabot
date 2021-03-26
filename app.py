import telegram

TOKEN = '1663679333:AAFr0l5wf1fU45mjVXqx_zJBYLFaeMf5hnI'

bot = telegram.Bot(token=TOKEN)

print(bot.get_me())