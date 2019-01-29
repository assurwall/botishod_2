# -*- coding: utf-8 -*-

import telebot

from telebot import types


import config

import data


bot = telebot.TeleBot(config.token, threaded=False)


def main_menu_keyboard(chat_id, first_name='None', user_name='None'):

    buttons = [
            types.InlineKeyboardButton(text='Горячая линия', callback_data='hl_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='О нас', callback_data='in_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Контакты', callback_data='cn_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Полезные ссылки', callback_data='ln_qr:'+chat_id+':'+first_name+':'+user_name),            
            types.InlineKeyboardButton(text='Юридический уголок', callback_data='lg_qr:'+chat_id+':'+first_name+':'+user_name),
#            types.InlineKeyboardButton(text='Фото', callback_data='ph_qr:'+chat_id+':'+first_name+':'+user_name)
            ]

    keyboard = types.InlineKeyboardMarkup()

    for button in buttons:

        keyboard.add(button)

    return keyboard


def hotline_menu_keyboard(chat_id, first_name, user_name='None'):
        
    buttons = [
            types.InlineKeyboardButton(text='Помощь', url='https://t.me/Pomoth'),
            types.InlineKeyboardButton(text='Чат', url='https://t.me/joinchat/HUGe2kdgu8_3lkWy2qvrvA'),
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
            types.InlineKeyboardButton(text='Калининградская область, Тверь и Рязань', callback_data='cn_10_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Черноморское побережье', callback_data='cn_11_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Краснодарский край', callback_data='cn_12_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Ставропольский край и Астрахань', callback_data='cn_13_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Ростовская область', callback_data='cn_14_qr:'+chat_id+':'+first_name+':'+user_name),
            types.InlineKeyboardButton(text='Владикавказ ', callback_data='cn_15_qr:'+chat_id+':'+first_name+':'+user_name),
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
            types.InlineKeyboardButton(text='Главное меню', callback_data='mmcs_qr:'+chat_id+':'+first_name+':'+user_name)
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

def goto_main_menu_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Главное меню', callback_data='mm_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard

def back_main_menu_and_clear_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='mmc_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard

def goto_main_menu_and_clear_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Главное меню', callback_data='mmc_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard

def back_contacts_menu_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='cn_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard

        
def back_legal_menu_and_clear_keyboard(chat_id, first_name, user_name='None'):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(types.InlineKeyboardButton(text='Назад', callback_data='lgc_qr:'+chat_id+':'+first_name+':'+user_name))
    
    return keyboard



def parse_and_send(post, user_chat_id):
    
    if(post.entities):
        
        print('Есть следующие сущности в тексте: ' + str(post.entities))
    
    if(post.document):
                
        bot.send_document(
            chat_id = user_chat_id, 
            data = post.document.file_id, 
            caption = post.caption)
                    
    elif(post.video):
                    
        bot.send_video(chat_id = user_chat_id, 
            data = post.video.file_id, 
            caption = post.caption)
                    
    elif(post.photo):
                    
        bot.send_photo(chat_id = user_chat_id, 
            photo = post.photo[0].file_id,
            caption = post.caption)
        
    elif(post.text):
        
        bot.send_message(chat_id = user_chat_id,
            text = post.text)


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
        
    elif(inline_query.data.split(':')[0]=='mmc_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)

        data.delete_recorded(inline_query.data.split(':')[2], bot)

        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Выберите интересующий пункт из меню.',
            reply_markup=main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),       
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='mmcs_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.delete_recorded(inline_query.data.split(':')[2], bot)
        
        bot.send_message(
            chat_id=inline_query.message.chat.id,
            text='Выберите интересующий пункт из меню.',
            reply_markup=main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),       
            parse_mode='Markdown')
    
    elif(inline_query.data.split(':')[0]=='hl_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.increment_buttons_db(1)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text=data.hotline,
            reply_markup=hotline_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='in_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.increment_buttons_db(2)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text=data.information,
            reply_markup=back_main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='cn_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.increment_buttons_db(3)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Выберите регион из представленных ниже',
            reply_markup=contacts_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
         
    elif(inline_query.data.split(':')[0]=='ln_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.increment_buttons_db(4)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text=data.links,
            reply_markup=back_main_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')

    elif(inline_query.data.split(':')[0]=='lg_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.increment_buttons_db(5)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Юридический уголок',
            reply_markup=legal_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
        
    elif(inline_query.data.split(':')[0]=='lgc_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.delete_recorded(inline_query.data.split(':')[2], bot)
        
        bot.edit_message_text(
            chat_id=inline_query.message.chat.id,
            message_id=inline_query.message.message_id,
            text='Юридический уголок',
            reply_markup=legal_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='lgi_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        sended_message = bot.edit_message_text(
                            chat_id=inline_query.message.chat.id,
                            message_id=inline_query.message.message_id,
                            text=data.legal,
                            parse_mode='Markdown')
        
        data.record_id(sended_message.message_id, sended_message.chat.id, inline_query.data.split(':')[2])
        
        photos = data.get_photos(2)
        
        for caption in photos.keys():
            
            sended_message = bot.send_photo(
                                chat_id=inline_query.message.chat.id,
                                photo=photos.get(caption),
                                caption=caption)
            
            data.record_id(sended_message.message_id, sended_message.chat.id, inline_query.data.split(':')[2])
            
            photos.get(caption).close()
            
        bot.send_message(
            chat_id=inline_query.message.chat.id,
            text='Вы также можете ознакомиться с [уставом](http://www.reabcentr.ru/images/stories/Chernozemie_/Ustav.docx) нашей организации.',
            reply_markup=back_legal_menu_and_clear_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
            parse_mode='Markdown')
        
    elif(inline_query.data.split(':')[0]=='ph_qr'):
    
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        data.increment_buttons_db(6)
        
        photos = data.get_photos(1)
        
        data.record_id(inline_query.message.message_id, inline_query.message.chat.id, inline_query.data.split(':')[2])
        
        for caption in photos.keys():
            
            sended_message = bot.send_photo(
                                chat_id=inline_query.message.chat.id,
                                photo=photos.get(caption),
                                caption=caption)
            
            data.record_id(sended_message.message_id, sended_message.chat.id, inline_query.data.split(':')[2])
            
            photos.get(caption).close()
            
        bot.send_message(
            chat_id=inline_query.message.chat.id,
            text='Вы сможете посмотреть другие фотографии в [https://vk.com/reabcentr](нашей группе Вконтакте)',
            reply_markup=back_main_menu_and_clear_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
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
        
        data.post = None
        
    elif(inline_query.data.split(':')[0]=='per_qr'):
        
        data.users_name.update({inline_query.data.split(':')[1] : [inline_query.data.split(':')[2], inline_query.data.split(':')[3]]})
        
        data.update_db(data.users_name)
        
        used_chat_id = []
        
        if(data.post):
            
            for user_chat_id in data.users_name.keys():
    
                if (str(user_chat_id)==str(inline_query.message.chat.id)):
    
                    continue
    
                if int(user_chat_id) in used_chat_id:
                    
                    continue
                    
                print('Отправка сообщения на id='+str(user_chat_id)+'\n')
    
                try:
            
                    parse_and_send(data.post, user_chat_id)
            
                except Exception as e: 
            
                    print(e)
                
                used_chat_id.append(user_chat_id)
                    
            bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text='Ваша новость отправлена.',
                reply_markup=post_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
                parse_mode='Markdown')
            
            data.post = None  

        else:
            
            bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text='Вами не было прислано никакой новости.',
                reply_markup=post_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
                parse_mode='Markdown')
                
              
    for i in range(0,16):
        
        if(inline_query.data.split(':')[0]=='cn_'+str(i)+'_qr'):
            
            bot.edit_message_text(
                chat_id=inline_query.message.chat.id,
                message_id=inline_query.message.message_id,
                text=data.contacts[i],
                reply_markup=back_contacts_menu_keyboard(inline_query.data.split(':')[1], inline_query.data.split(':')[2], inline_query.data.split(':')[3]),
                parse_mode='Markdown')
      

@bot.message_handler(content_types=['photo', 'audio', 'video', 'document', 'location', 'contact', 'sticker'])

def content_handler(message):

    if(data.users_name.get(str(message.chat.id))==['record', str(message.from_user.username)]):
        
        data.post = message
        
    else:
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)

        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите интересующий пункт из меню.', 
            reply_markup=main_menu_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))
        
    
@bot.message_handler(content_types="text")

def text_handler(message):

    if(data.users_name.get(str(message.chat.id))==['record', str(message.from_user.username)]):
        
        data.post = message
        
    elif(message.text=='пост3.16'):
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)
        
        sended_message = bot.send_message(
                            chat_id=message.chat.id, 
                            text='Выберите пункт "Начать отправку" чтобы отправить новость.', 
                            reply_markup=post_menu_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))
        
        data.record_id(sended_message.message_id, sended_message.chat.id, message.from_user.first_name)
        
    elif(message.text=='база_список3.16'):
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)
        
        cut_index = 0
        step = 4096
        
        while(data.all_db()[cut_index : cut_index+step]):
        
            sended_message = bot.send_message(
                                chat_id=message.chat.id, 
                                text=data.all_db()[cut_index : cut_index+step])
            
            data.record_id(sended_message.message_id, sended_message.chat.id, message.from_user.first_name)
            
            cut_index += step
            
        bot.send_message(
            chat_id=message.chat.id, 
            text="Конец базы данных.",
            reply_markup=goto_main_menu_and_clear_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))
         
         
    elif(message.text=='база_файл3.16'):
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)
        
        db_file = data.all_db_file()
        
        sended_message = bot.send_document(
                            chat_id=message.chat.id, 
                            data=db_file)
        
        data.record_id(sended_message.message_id, sended_message.chat.id, message.from_user.first_name)
        
        bot.send_message(
            chat_id=message.chat.id,
            text="Файл с базой данных отправлен.",
            reply_markup=goto_main_menu_and_clear_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))
        
        db_file.close()
        
    elif(message.text=='статистика3.16'):
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)
        
        bot.send_message(
            chat_id=message.chat.id,
            text=data.all_buttons_statistics(),
            reply_markup=goto_main_menu_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))
        
    elif(message.text=='статистика_сегодня3.16'):
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)
        
        bot.send_message(
            chat_id=message.chat.id, 
            text=data.today_buttons_statistics(),
            reply_markup=goto_main_menu_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))
        
    else:
        
        data.users_name.update({str(message.chat.id) : [str(message.from_user.first_name), str(message.from_user.username)]})
        
        data.update_db(data.users_name)

        bot.send_message(
            chat_id=message.chat.id, 
            text='Выберите интересующий пункт из меню.', 
            reply_markup=main_menu_keyboard(str(message.chat.id), str(message.from_user.first_name), str(message.from_user.username)))


if __name__ == '__main__': 
    
    
    while True:
        
        try:
            
            bot.polling(none_stop=True)
            
        except Exception as e: 
            
            print(e)