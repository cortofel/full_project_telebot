import telebot
from botLOGIC import gen_pass,gen_emodji,flip_coin
import time, threading,schedule



bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=["new_password"])
def gen_password(message):
    count = int(message.text.split()[1]) if len(message.text.split()) > 1 else 10
    bot.reply_to(message,gen_pass(count)) 
       

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    bot.reply_to(message,"Вот эмоджи: ", gen_emodji())

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")


def beep(chat_id) -> None:
    """Send the beep message."""
    bot.send_message(chat_id, text='Beep!')


@bot.message_handler(commands=['set'])
def set_timer(message):
    args = message.text.split()
    if len(args) > 1 and args[1].isdigit():
        sec = int(args[1])
        schedule.every(sec).seconds.do(beep, message.chat.id).tag(message.chat.id)
    else:
        bot.reply_to(message, 'Usage: /set <seconds>')


@bot.message_handler(commands=['unset'])
def unset_timer(message):
    schedule.clear(message.chat.id)
    

if __name__ == '__main__':
    threading.Thread(target=bot.infinity_polling, name='bot_infinity_polling', daemon=True).start()
while True:
    schedule.run_pending()
    time.sleep(1)

