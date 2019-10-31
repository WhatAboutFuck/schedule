import telebot
import config
from config import token
import db
import pymongo
from sel import get_scrin
from telebot.apihelper import ApiException

bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def welcome(message):
    if not db.u_id.find_one({"id":message.from_user.id}):
        db.u_id.insert_one({"id":message.from_user.id})
        bot.send_message(message.from_user.id,
        f'''Привет,{message.from_user.first_name}\nВведи номер группы''')
        bot.register_next_step_handler(message,update_name)

    else:
        for doc in db.u_id.find({"id":message.from_user.id},{"_id":0,"id":0}):
            global x
            x = str(*list(doc.values()))
        bot.send_message(message.from_user.id,
        f'''Привет,{message.from_user.first_name}\nТвой номер группы:{x}''',
        reply_markup=config.markup_user)
        

@bot.message_handler(content_types = ['text'])
def check_corect(message):
    if message.text == 'Да':
        bot.send_photo(message.from_user.id,get_scrin(x))
    elif message.text == 'Нет':
        bot.send_message(message.from_user.id,"Введи номер группы")
        bot.register_next_step_handler(message,update_name)
    else:
        bot.register_next_step_handler(message,welcome)
def update_name(message):
    db.u_id.find_one_and_update({"id":message.from_user.id},{"$set":{"NameOfGroup":message.text.upper()}})
    for doc in db.u_id.find({"id":message.from_user.id},{"_id":0,"id":0}):
            y = str(*list(doc.values()))
    try:
        bot.send_photo(message.from_user.id,get_scrin(y))
    except ApiException:
        bot.send_message(message.from_user.id,'Группа не найдена!')




if __name__ == "__main__":
    bot.polling(none_stop = True)