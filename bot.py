# -*- coding: utf-8 -*-

import time

import telebot

from telebot import types


import config

import data


bot = telebot.TeleBot(config.token, threaded=False)


def send_all_db(current_chat_id):
    
    for chat_id, username in data.users_username.items():
        
        bot.send_message(
            chat_id=current_chat_id, 
            text='Chat_id:'+str(chat_id)+' Username:'+username+'\n')


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


def post_menu_keyboard(username):
    
    buttons = [
            types.InlineKeyboardButton(text='Начать отправку', callback_data='post_record_query:'+username),
            types.InlineKeyboardButton(text='Главное меню', callback_data='main_menu_query')
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


def post_record_menu_keyboard(username):
    
    buttons = [
            types.InlineKeyboardButton(text='Завершить отправку', callback_data='post_end_record_query:'+username),
            types.InlineKeyboardButton(text='Отмена', callback_data='post_cancel_query:'+username)
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


def back_main_menu_keyboard():

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='main_menu_query'))
    
    return keyboard


def back_contacts_keyboard():

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='contacts_query'))
    
    return keyboard


def contacts_menu_keyboard():
    
    buttons = [
            types.InlineKeyboardButton(text='Центр матери и ребёнка Мир', callback_data='contacts_0_query'),
            types.InlineKeyboardButton(text='Санкт-Петербург и Ленинградская область', callback_data='contacts_1_query'),
            types.InlineKeyboardButton(text='Самара ', callback_data='contacts_2_query'),
            types.InlineKeyboardButton(text='Воронеж', callback_data='contacts_3_query'),
            types.InlineKeyboardButton(text='Липецк', callback_data='contacts_4_query'),
            types.InlineKeyboardButton(text='Орел', callback_data='contacts_5_query'),
            types.InlineKeyboardButton(text='Старый Оскол', callback_data='contacts_6_query'),
            types.InlineKeyboardButton(text='Пенза', callback_data='contacts_7_query'),
            types.InlineKeyboardButton(text='Брянск', callback_data='contacts_8_query'),
            types.InlineKeyboardButton(text='Москва и Московская область', callback_data='contacts_9_query'),
            types.InlineKeyboardButton(text='Королев', callback_data='contacts_10_query'),
            types.InlineKeyboardButton(text='Ногинск', callback_data='contacts_11_query'),
            types.InlineKeyboardButton(text='Тверь', callback_data='contacts_12_query'),
            types.InlineKeyboardButton(text='Подольск', callback_data='contacts_13_query'),
            types.InlineKeyboardButton(text='Щелково', callback_data='contacts_14_query'),
            types.InlineKeyboardButton(text='Фрязино', callback_data='contacts_15_query'),
            types.InlineKeyboardButton(text='Рязань', callback_data='contacts_16_query'),
            types.InlineKeyboardButton(text='Серпухов', callback_data='contacts_17_query'),
            types.InlineKeyboardButton(text='Химки', callback_data='contacts_18_query'),
            types.InlineKeyboardButton(text='Калужская область', callback_data='contacts_19_query'),
            types.InlineKeyboardButton(text='Калининградская область', callback_data='contacts_20_query'),
            types.InlineKeyboardButton(text='Черноморское побережье', callback_data='contacts_21_query'),
            types.InlineKeyboardButton(text='Краснодарский край', callback_data='contacts_22_query'),
            types.InlineKeyboardButton(text='Ставропольский край', callback_data='contacts_23_query'),
            types.InlineKeyboardButton(text='Невинномысск', callback_data='contacts_24_query'),
            types.InlineKeyboardButton(text='Ессентуки', callback_data='contacts_25_query'),
            types.InlineKeyboardButton(text='Пятигорск', callback_data='contacts_26_query'),
            types.InlineKeyboardButton(text='Астрахань', callback_data='contacts_27_query'),
            types.InlineKeyboardButton(text='Михайловск', callback_data='contacts_28_query'),
            types.InlineKeyboardButton(text='Ростовская область', callback_data='contacts_29_query'),
            types.InlineKeyboardButton(text='Волгодонск', callback_data='contacts_30_query'),
            types.InlineKeyboardButton(text='Азов', callback_data='contacts_31_query'),
            types.InlineKeyboardButton(text='Таганрог', callback_data='contacts_32_query'),
            types.InlineKeyboardButton(text='Шахты', callback_data='contacts_33_query'),
            types.InlineKeyboardButton(text='Новочеркасск', callback_data='contacts_34_query'),
            types.InlineKeyboardButton(text='Батайск', callback_data='contacts_35_query'),
            types.InlineKeyboardButton(text='Владикавказ ', callback_data='contacts_36_query'),
            types.InlineKeyboardButton(text='Назад', callback_data='main_menu_query')
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard
        
    
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
            text=data.information,
            reply_markup=back_main_menu_keyboard(),
            parse_mode='Markdown')
        
    elif(inline_query.data=='contacts_query'):
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='''Выберите регион из представленных ниже''',
            reply_markup=contacts_menu_keyboard(),
            parse_mode='Markdown')
         
#    elif(inline_query.data=='links_query'):
        
#    elif(inline_query.data=='legal_query'):

    elif(inline_query.data.split(':')[0] == 'post_record_query'):
        
        data.users_username.update({str(inline_query.message.chat.id) : 'record'})
        
        send_all_db(inline_query.message.chat.id)
        
        data.update_db(data.users_username)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Отправьте вашу новость и нажмите кнопку "Завершить отправку"',
            reply_markup=post_record_menu_keyboard(inline_query.data.split(':')[1]),
            parse_mode='Markdown')
    
    
    elif(inline_query.data.split(':')[0] == 'post_cancel_query'):
        
        data.users_username.update({str(inline_query.message.chat.id) : inline_query.data.split(':')[1]})
        
        send_all_db(inline_query.message.chat.id)
        
        data.update_db(data.users_username)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Выберите пункт "Начать отправку" чтобы отправить новость.',
            reply_markup=post_menu_keyboard(inline_query.data.split(':')[1]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0] == 'post_end_record_query'):
        
        data.users_username.update({str(inline_query.message.chat.id) : inline_query.data.split(':')[1]})
        
        send_all_db(inline_query.message.chat.id)
        
        data.update_db(data.users_username)
        
        for user_chat_id in data.users_username.keys():
            
            bot.send_message(
                chat_id=user_chat_id,
                text=data.news)
            
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Ваша новость отправлена.',
            reply_markup=post_menu_keyboard(inline_query.data.split(':')[1]),
            parse_mode='Markdown')
        
        data.news = ''''''
        
    for i in range(0,37):
        
        if(inline_query.data == 'contacts_'+str(i)+'_query'):
            
            bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text=data.contacts[i],
                reply_markup=back_contacts_keyboard(),
                parse_mode='Markdown')
      
            
@bot.message_handler(content_types="text")

def text_handler(message):
    
    send_all_db(message.chat.id)
    
    if(data.users_username.get(str(message.chat.id)) == 'record'): #Проверяем записывать ли данное сообщение как часть отправляемой новости
        
        data.news += message.text
        
    elif(message.text=='пост3.16'):
        
        data.users_username.update({str(message.chat.id) : message.from_user.username})
        
        data.update_db(data.users_username)
        
        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите пункт "Начать отправку" чтобы отправить новость.', 
            reply_markup=post_menu_keyboard(message.from_user.username))
        
    else:
        
        data.users_username.update({str(message.chat.id) : message.from_user.username})
        
        data.update_db(data.users_username)

        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите интересующий пункт из меню.', 
            reply_markup=main_menu_keyboard())


if __name__ == '__main__': 
    
    
    while True:
        
        try:
            
            bot.polling(none_stop=True)
            
            time.sleep(3)
            
        except Exception as e: 
            
            print(e)
           
            time.sleep(10)