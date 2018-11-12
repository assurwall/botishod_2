# -*- coding: utf-8 -*-

import config

import telebot

import time

from telebot import types


bot = telebot.TeleBot(config.token)

users = {}

information='''
Мы помогаем людям, зависимым от наркотиков и алкоголя, уже более 16 лет. За это время тысячи судеб обрели новую жизнь: 9000 человек успешно прошли нашу программу реабилитации. На данный момент у нас 36 реабилитационных центров по всей России. Наши плюсы очевидны: 
- мы не эксплуатируем труд участников программы; 
- не применяем дорогие препараты и ненужные процедуры; 
- используем индивидуальный подход к каждому участнику программы; 
- мы представляем наших участников в судах и в органах опеки; 
- восстанавливаем трудовые навыки. 
Предлагаемая программа преодоления алкогольной и наркотической зависимости уникальна тем, что она разработана людьми, имеющим личный опыт преодоления зависимости. Её эффективность подтверждена временем, высокими оценками специалистов и данными статистики. 
Нашим горячим желанием всегда было и остается: «помочь ещё одному», все потому, что мы когда-то сами проходили все этапы нашей программы реабилитации. Выход есть и он реален, и мы хотим доказать это каждому.
Найти всю информацию о нас, а так же ознакомиться с нашей программой вы сможете на нашем сайте. http://www.reabcentr.ru/
Или на нашей странице в Вк
https://vk.com/reabcentr
Помните, наша команда трудится для вас всегда, в любое время. Пишите и мы вам обязательно поможем !!!'''


def main_menu_keyboard():

    buttons = [
            types.InlineKeyboardButton(text='Горячая линия', callback_data='hotline_query'),
            types.InlineKeyboardButton(text='О нас', callback_data='information_query'),
            types.InlineKeyboardButton(text='Контакты', callback_data='contacts_query'),
            types.InlineKeyboardButton(text='Полезные ссылки', callback_data='links_query'),            
            types.InlineKeyboardButton(text='Юридический уголок', callback_data='legal_query')
            ]

    keyboard = types.InlineKeyboardMarkup()

    for button in buttons:

        keyboard.add(button)

    return keyboard


def hotline_menu_keyboard():
        
    buttons = [
            types.InlineKeyboardButton(text='Помощь', url='https://t.me/Pomoth'),
            types.InlineKeyboardButton(text='Чат, если бан', url='https://t.me/joinchat/HUGe2kdgu8_3lkWy2qvrvA'),
            types.InlineKeyboardButton(text='Назад', callback_data='main_menu_query')
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


def post_menu_keyboard():
    
    buttons = [
            types.InlineKeyboardButton(text='Начать отправку', callback_data='post_record_query'),
            types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu_query')
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard

def post_record_menu_keyboard():
    
    buttons = [
            types.InlineKeyboardButton(text='Завершить отправку', callback_data='post_end_record_query'),
            types.InlineKeyboardButton(text='Отмена', callback_data='post_cancel_query')
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard

def information_menu_keyboard():

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='main_menu_query'))
    
    return keyboard


@bot.message_handler(content_types="text")

def text_handler(message):

    if(users[message.from_user.username]): #Проверяем записывать ли данное сообщение как часть отправляемой новости
    
        
        
    elif(message.text=='пост3.16'):
        
        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите пункт "Начать отправку" чтобы отправить новость.', 
            reply_markup=post_menu_keyboard())
        
    else:
        
        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите интересующий пункт из меню.', 
            reply_markup=main_menu_keyboard())
        

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
                text='''Вы можете позвонить нам по бесплатному номеру: \n8-800-333-09-81, \nПишите нам: @Yarik78, @Zaosi''',
                reply_markup=hotline_menu_keyboard(),
                parse_mode='Markdown')
        
    elif(inline_query.data=='information_query'):
        
        bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text=information,
                reply_markup=information_menu_keyboard(),
                parse_mode='Markdown')
        
#    elif(inline_query.data=='contacts_query'):
        
#    elif(inline_query.data=='links_query'):
        
#    elif(inline_query.data=='legal_query'):

    elif(inline_query.data=='post_cancel_query'):
        
        users[inline_query.message.from_user.username] = False
        
        bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text='Выберите пункт "Начать отправку" чтобы отправить новость.',
                reply_markup=post_menu_keyboard(),
                parse_mode='Markdown')

    elif(inline_query.data=='post_record_query'):
        
        users[inline_query.message.from_user.username] = True
        
        bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text='Отправьте вашу новость и нажмите кнопку "Завершить отправку"',
                reply_markup=post_record_menu_keyboard(),
                parse_mode='Markdown')
        
    elif(inline_query.data=='post_end_record_query'):
        
        users[inline_query.message.from_user.username] = False
        
        for

if __name__ == '__main__': 
    
    while True:
        
        try:
            
            bot.polling(none_stop=True)
            
            time.sleep(3)
            
        except Exception as e: 
            
            print(e)
           
            time.sleep(10)