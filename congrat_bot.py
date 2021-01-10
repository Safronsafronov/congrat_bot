#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import telebot
import datetime


# In[ ]:


# заготовки для частей
fitst_part = ['Привет дружочек!', 'Привет!', 'Доброго дня!', 'Салют!', 'Вечер в хату!']
second_part = ['Сегодня прекрасный день, ведь у тебя День рождения!', 'Мне шепнули, что у кого-то сегодня праздник.', 'Говорят, у кого-то сегодня праздник.', 
              'Сегодня, ты стал чуточку старше!', 'Сегодня кто-то постарел, возможно это ты:)']
third_part = ['Именно поэтому я поздравляю тебя с Днем рождения и желаю тебе']
fourth_part_1 = ['счастья,', 'всего наилучшего,']
fourth_part_2 = ['здоровья,', 'исполнения всех желаний,', 'найти дело по душе,']
fourth_part_3 = ['познакомиться с новыми и интересными людьми,', 'узнать много нового,', 'развиваться,']
fourth_part_4 = ['стать лучше, чем ты был в прошлом году!', 'не грустить и ничего не бояться!']
last_part = ['Проведи этот день весело!', 'Проведи этот день в кругу друзей!', 'Отметь свой день рождения как следует:)']




# команды

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доброго дня! Я бот поздравитель. Напиши мне "начать" и я пришлю тебе поздравление.')
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот поздравитель! Если тебе нужно поздравить друга, то я тебе помогу.\n/start - начать работу\n/congratulations - получить поздравление\n/end - закончить работу с ботом')
@bot.message_handler(commands=['congratulations'])
def start_message(message):
    msg = random.choice(fitst_part) + ' ' + random.choice(second_part) + ' ' + random.choice(third_part) + ' ' + random.choice(fourth_part_1) + ' ' + random.choice(fourth_part_2) + ' ' + random.choice(fourth_part_3) + ' ' + random.choice(fourth_part_4) + ' ' + random.choice(last_part)
    bot.send_message(message.from_user.id, msg)
@bot.message_handler(commands=['end'])
def start_message(message):
    bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAANoX_MgpelOx2AWhMn5f0lZOpWtuXcAAkADAAK1cdoGuRLw3B1VGFweBA')


@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Доброго дня! Я бот поздравитель. Напиши мне "начать" и я пришлю тебе поздравление.')
    elif message.text.lower() == 'дата':
        bot.send_message(message.from_user.id, datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    elif message.text.lower() == 'начать':
        msg = random.choice(fitst_part) + ' ' + random.choice(second_part) + ' ' + random.choice(third_part) + ' ' + random.choice(fourth_part_1) + ' ' + random.choice(fourth_part_2) + ' ' + random.choice(fourth_part_3) + ' ' + random.choice(fourth_part_4) + ' ' + random.choice(last_part)
        bot.send_message(message.from_user.id, msg)
    elif message.text.lower() == 'спасибо':
        bot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAANoX_MgpelOx2AWhMn5f0lZOpWtuXcAAkADAAK1cdoGuRLw3B1VGFweBA')
    else: bot.send_message(message.from_user.id, 'Я гордый, для начала поздоровайся со мной (напиши мне "привет")')

        
bot.polling(none_stop=True, interval=0)
# print (datetime.date.today())

