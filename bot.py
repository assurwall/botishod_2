# -*- coding: utf-8 -*-

import time

import telebot

from telebot import types


import config

import data

bot = telebot.TeleBot(config.token, threaded=False)


def send_all_db(current_chat_id):

    con = data.connect.create_connect()

    con.set_isolation_level(data.connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute('SELECT * FROM users_data')
    
    users_data = cur.fetchall()
    
    for user_chat_id, first_name, user_name in users_data:
    
        bot.send_message(
            chat_id=current_chat_id,
            text='Chat_id:'+str(user_chat_id)+' First_name:'+first_name+' User_name:'+str(user_name)+'\n')
        
    con.close()

    cur.close()

def send_all_db_file(current_chat_id):

    con = data.connect.create_connect()

    con.set_isolation_level(data.connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute('SELECT * FROM users_data')
    
    users_data = cur.fetchall()
    
    database_file = open('database.txt', 'w')
    
    database_file.write('Здравствуйте. Здесь представлена база данных пользователей на текущий момент. \r\n')
    
    for chat_id, first_name, user_name in users_data:
        
        database_file.write('Chat_id:'+str(chat_id)+' First_name:'+first_name+' User_name:'+user_name+'\r\n')
        
    database_file.close()
        
    database_file = open('database.txt', 'rb')    
        
    bot.send_document(
        chat_id=current_chat_id,
        data=database_file
        )
    
    database_file.close()
    
    con.close()

    cur.close()


def main_menu_keyboard(chat_id, first_name='None', user_name='None'):

    buttons = [
            types.InlineKeyboardButton(text='Горячая линия', callback_data='hl_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='О нас', callback_data='in_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Контакты', callback_data='cn_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Полезные ссылки', callback_data='ln_qr:'+chat_id+':'+first_name+':'+user_name),            
            types.InlineKeyboardButton(text='Юридический уголок', callback_data='lg_qr:'+chat_id+':'+first_name+':'+user_name)
            ]

    keyboard = types.InlineKeyboardMarkup()

    for button in buttons:

        keyboard.add(button)

    return keyboard


def hotline_menu_keyboard(chat_id, first_name, user_name='None'):
        
    buttons = [
            types.InlineKeyboardButton(text='Помощь', url='https://t.me/Pomoth'),
            types.InlineKeyboardButton(text='Чат, если бан', url='https://t.me/joinchat/HUGe2kdgu8_3lkWy2qvrvA'),
            types.InlineKeyboardButton(text='Назад', callback_data='mm_qr:'+chat_id+':'+first_name+':'+user_name)
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


def contacts_menu_keyboard(chat_id, first_name, user_name='None'):
    
    buttons = [
            types.InlineKeyboardButton(text='Центр матери и ребенка "Мир"', callback_data='cn_0_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Санкт-Петербург и Ленинградская область', callback_data='cn_1_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Самара ', callback_data='cn_2_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Воронеж', callback_data='cn_3_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Липецк', callback_data='cn_4_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Орел', callback_data='cn_5_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Старый Оскол', callback_data='cn_6_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Пенза', callback_data='cn_7_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Брянск', callback_data='cn_8_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Москва и московская область, Калужская область', callback_data='cn_9_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Калининградская область, Тверь и Рязань', callback_data='cn_9_query:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Черноморское побережье', callback_data='cn_10_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Краснодарский край', callback_data='cn_11_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Ставропольский край и Астрахань', callback_data='cn_12_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Ростовская область', callback_data='cn_13_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Владикавказ ', callback_data='cn_14_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Назад', callback_data='mm_qr:'+chat_id+':'+first_name+':'+user_name)
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard
    

def legal_menu_keyboard(chat_id, first_name, user_name='None'):
        
    buttons = [
            types.InlineKeyboardButton(text='Важно знать', callback_data='lgi_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Задать вопрос', url='https://t.me/Pomoth'),
            types.InlineKeyboardButton(text='Назад', callback_data='mm_qr:'+chat_id+':'+first_name+':'+user_name)
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard
    
    
def post_menu_keyboard(chat_id, first_name, user_name='None'):
    
    buttons = [
            types.InlineKeyboardButton(text='Начать отправку', callback_data='pr_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Главное меню', callback_data='mm_qr:'+chat_id+':'+first_name+':'+user_name)
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


def post_record_menu_keyboard(chat_id, first_name, user_name='None'):
    
    buttons = [
            types.InlineKeyboardButton(text='Завершить отправку', callback_data='per_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Отмена', callback_data='pc_qr:'+chat_id+':'+first_name+':'+user_name)
            ]
    
    keyboard = types.InlineKeyboardMarkup()
    
    for button in buttons:
            
        keyboard.add(button)
        
    return keyboard


def back_main_menu_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='mm_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard


def back_contacts_menu_keyboard(chat_id, first_name, user_name):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='cn_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard

        
def back_legal_menu_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='lg_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard
    
@bot.callback_query_handler(func=lambda inline_query: True)

def inline_handler(inline_query):

    if(inline_query.data.split(':')[0]=='mm_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)

        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Выберите интересующий пункт из меню.',
            reply_markup=main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),       
            parse_mode='Markdown')
    
    elif(inline_query.data.split(':')[0]=='hl_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text=data.hotline,
            reply_markup=hotline_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='in_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text=data.information,
            reply_markup=back_main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='cn_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Выберите регион из представленных ниже',
            reply_markup=contacts_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
         
    elif(inline_query.data.split(':')[0]=='ln_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text=data.links,
            reply_markup=back_main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]))

    elif(inline_query.data.split(':')[0]=='lg_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Юридический уголок',
            reply_markup=legal_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown') 
        
    elif(inline_query.data.split(':')[0]=='lgi_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Здесь будет важная информация',
            reply_markup=back_legal_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown') 
        
    elif(inline_query.data.split(':')[0]=='pr_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : ['record', str(inline_query.data.split(':')[3])]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Отправьте вашу новость и нажмите кнопку "Завершить отправку"',
            reply_markup=post_record_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
    
    elif(inline_query.data.split(':')[0]=='pc_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Выберите пункт "Начать отправку" чтобы отправить новость.',
            reply_markup=post_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
        data.news = ''''''
        
    elif(inline_query.data.split(':')[0]=='per_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        used = []
        
        for user_chat_id in data.users_name.keys():
            
  #          flag = False
            
#            for used_id in used:
                
#                if(user_chat_id==used_id):
                    
#                    flag = True
            
#            if(flag):
                
#                continue
            
#            if (str(user_chat_id)==str(inline_query.message.chat.id)):
                
#                continue

            print('Отправка сообщения на id='+user_chat_id+'\n')
                
            try:
                
                bot.send_message(
                    chat_id=user_chat_id,
                    text=data.news)
                
                used.append(user_chat_id)
                
            except:
                
                continue


        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Ваша новость отправлена.',
            reply_markup=post_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
        data.news = ''''''
        
    for i in range(0,15):
        
        if(inline_query.data.split(':')[0]=='cn_'+str(i)+'_qr'):
            
            bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text=data.contacts[i],
                reply_markup=back_contacts_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
                parse_mode='Markdown')
      
            
@bot.message_handler(content_types="text")

def text_handler(message):

    
    if(data.users_name.get(str(message.chat.id))==['record', message.from_user.username]): #Проверяем записывать ли данное сообщение как часть отправляемой новости
        
        data.news += message.text
        
    elif(message.text=='пост3.16'):
        
        data.users_name.update({str(message.chat.id) : [message.from_user.first_name, message.from_user.username]})
        
        data.update_db(data.users_name)
        
        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите пункт "Начать отправку" чтобы отправить новость.', 
            reply_markup=post_menu_keyboard(str(message.chat.id), message.from_user.first_name, message.from_user.username))
        
    elif(message.text=='база_список3.16'):
        
        data.users_name.update({str(message.chat.id) : [message.from_user.first_name, message.from_user.username]})
        
        data.update_db(data.users_name)
        
        send_all_db(message.chat.id)
        
    elif(message.text=='база_файл3.16'):
        
        data.users_name.update({str(message.chat.id) : [message.from_user.first_name, message.from_user.username]})
        
        data.update_db(data.users_name)
        
        send_all_db_file(message.chat.id)
        
    else:
        
        data.users_name.update({str(message.chat.id) : [message.from_user.first_name, message.from_user.username]})
        
        data.update_db(data.users_name)

        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите интересующий пункт из меню.', 
            reply_markup=main_menu_keyboard(str(message.chat.id), message.from_user.first_name, message.from_user.username))


if __name__ == '__main__': 
    
    
    while True:
        
        try:
            
            bot.polling(none_stop=True)
            
            time.sleep(3)
            
        except Exception as e: 
            
            print(e)
           
            time.sleep(10)