# -*- coding: utf-8 -*-

import config

import telebot

import time

from telebot import types

bot = telebot.TeleBot(config.token)


def main_menu_keyboard():

    buttons = [
                types.InlineKeyboardButton(text='Горячая линия', callback_data='hotline_query'),
                types.InlineKeyboardButton(text='О нас', callback_data='informations_query'),
                types.InlineKeyboardButton(text='Контакты', callback_data='contacts_query'),
                types.InlineKeyboardButton(text='Полезные ссылки', callback_data='links_query'),            
                types.InlineKeyboardButton(text='Юридический уголок', callback_data='legal_query')
                ]

    keyboard=types.InlineKeyboardMarkup()

    for button in buttons:

        keyboard.add(button)

    return keyboard


def hotline_menu_keyboard():
        
    buttons = [
        types.InlineKeyboardButton(text='Помощь', url='https://t.me/Pomoth'),
        types.InlineKeyboardButton(text='Чат, если бан', url='https://t.me/joinchat/HUGe2kdgu8_3lkWy2qvrvA'),
        types.InlineKeyboardButton(text='Назад', callback_data='main_menu_query')
        ]
        
    keyboard=types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


@bot.message_handler(content_types="text")

def text_handler(message):

    if message.from_user.first_name in ['Zaosi', 'Yarik78', 'pomoth']:

        keyboard = main_menu_keyboard()
        
        keyboard.add(types.InlineKeyboardButton(text='Пост', callback_data='post_query'))
        
        bot.send_message(message.chat.id, 'Выберите интересующий пункт из меню.', reply_markup=keyboard)

    else:
        
        bot.send_message(message.chat.id, 'Выберите интересующий пункт из меню.', reply_markup = main_menu_keyboard())
        

@bot.callback_query_handler(func=lambda inline_query: True)

def inline_handler(inline_query):

    if(inline_query.data=='main_menu_query'):

        bot.edit_message_text(
            
                chat_id=inline_query.message.chat.id,
                
                message_id=inline_query.message.message_id,
    
                text='Выберите интересующий пункт из меню.',
                
                reply_markup=main_menu_keyboard(),
                                    
                parse_mode='Markdown')
    
    elif(inline_query.data=='hotline_query'):
        
        bot.edit_message_text(
            
                chat_id=inline_query.message.chat.id,
                
                message_id=inline_query.message.message_id,
    
                text='Вы можете позвонить нам по бесплатному номеру: \n'
                '8-800-333-09-81, \n'
                'Пишите нам: @Yarik78, @Zaosi',
                
                reply_markup=hotline_menu_keyboard(),
                                    
                parse_mode='Markdown')
        
#    elif(inline_query.data=='informations_query'):
        
#    elif(inline_query.data=='contacts_query'):
        
#    elif(inline_query.data=='links_query'):
        
#    elif(inline_query.data=='legal_query'):
        
if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True)
            
            time.sleep(3)
            
        except Exception as e: 
            
            print(e)
           
            time.sleep(10)