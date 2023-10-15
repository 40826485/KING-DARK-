import telebot
from requests import get
import time,random,os
from telebot import types

token = '6687054033:AAH2oe11-vppaZgQ-HkdwcMjvhjUgmI07bs'

bot = telebot.TeleBot(token)
bot.set_my_commands([telebot.types.BotCommand("/start", "🤖 Start the bot")])


@bot.message_handler(commands=['start'])
def start(message):
    
    name = message.from_user.first_name
    
    my = types.InlineKeyboardButton(text='😂اقوي مبرمج")
    
    xx = types.InlineKeyboardMarkup()
    xx.add(my)
    
    n = message.chat.first_name
    us = f'{n}'

    bot.reply_to(message, f'<b> 𝐇𝒊 » {us} \n\nEnter Your Bin 6 Numper \nIR ارسل البن المكون من 6 ارقام</b>',parse_mode='HTML', reply_markup=xx)
  
@bot.message_handler(func=lambda m:True)
#تلي @A_R_53

def r(message):
    
    iy = message.text

    num = '1234567890'
    
    for i in range(1000):
        
        us = str("".join(random.choice(num)for i in range(10)))
        ue = str("".join(random.choice(num)for i in range(3)))
        
        ii = '01','02','03','04','05','06','07','08','09','10','11','12'
        
        um = random.choice(ii)
        num = '456789'
        u = str("".join(random.choice(num)for i in range(1)))
        
        us = str(iy + us + '|' + um + '|' + f'202{u}' + '|' + ue)
#جميع الحقوق محفوضه لدى حسو ال علي        

        with open("visa @A_R_53.txt", "a") as file:
            file.write(us + "\n")
    
    with open("visa @A_R_53.txt", "rb") as file:
                
        
        
        bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id,'<b>✅ Good 1000 Vise\n~ ~ ~ ~ ~ ~ ~ ~ ~\@A_R_53</b>',parse_mode='HTML')
        
        os.remove("visa @llxxx3.txt")
        
        
print('Running Go Bot Telegram /start ')

bot.infinity_polling()

