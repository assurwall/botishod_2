# -*- coding: utf-8 -*-

import datetime

import connect

import os


def get_information():
    
    result = ''
    
    information_file = open('information.txt', 'r')
    
    for line in information_file:
        
        result += line
        
    information_file.close()

    return result

information = get_information()


contacts = []

contacts.append('''8-800-500-28-13
[Вконтакте](https://vk.com/id420868047)
''')

contacts.append('''*Сергей*:8-921-255-93-23 
[Вконтакте](https://vk.com/id320895361)
''')

contacts.append('''*Александр*:8-927-611-91-55   
''')

contacts.append('''*Георгий*:8-920-223-66-65
[Вконтакте](https://vk.com/id410874012)
''')

contacts.append('''*Артем*:8-920-527-54-33 
[Вконтакте](https://vk.com/id410874012)
''')

contacts.append('''*Антон*:8-920-080-93-11 
[Вконтакте](https://vk.com/id410874012)
''')

contacts.append('''*Владимир*:8-920-468-40-25 
[Вконтакте](https://vk.com/id410874012)
''')

contacts.append('''*Рафаэль*:8-927-092-33-69 
[Вконтакте](https://vk.com/id410874012)
''')

contacts.append('''8-920-222-09-07
[Вконтакте](https://vk.com/id410874012)
''')

contacts.append('''*Эдуард*:8-926-612-36-33 
''')

contacts.append('''*Эдуард*:8-926-612-36-33  
''')

contacts.append('''8-928-444-14-90
[Вконтакте](https://vk.com/prozhiznsochi)
''')

contacts.append('''*Иван*:8-928-215-63-54 
[Вконтакте](https://vk.com/reba2018)
''')

contacts.append('''*Сослан*:8-928-301-06-01
[Вконтакте](https://vk.com/id361427938)
''')

contacts.append('''*Максим*:8-928-766-57-57 
[Вконтакте](https://vk.com/id395722415)
''')

contacts.append('''*Артем*:8-928-497-99-82 
[Вконтакте](https://vk.com/id408141585)
''')


def get_photos(number):
    
    result = {}
    
    if(number == 1):
    
        for filename in os.listdir(os.getcwd()+'/images/menu_photos'):
            
            result.update({str(filename).split('.')[0] : open('images/menu_photos/' + str(filename), 'rb')})
            
    elif(number == 2):
    
        result.update({'Свидетельство о государственной некомерческой организации"': open('images/Свидетельство 1.jpg', 'rb')})
        
        result.update({'Свидетельство о постановке на учёт в налогом органе': open('images/Свидетельство 2.jpg', 'rb')})
    

    return result


def get_links():
    
    result = ''
    
    links_file = open('links.txt', 'r')
    
    for line in links_file:
        
        result += line
        
    links_file.close()

    return result

links = get_links()


def get_hotline():
    
    result = ''
    
    hotline_file = open('hotline.txt', 'r')
    
    for line in hotline_file:
        
        result += line
        
    hotline_file.close()

    return result

hotline = get_hotline()


def get_legal():
    
    result = ''
    
    hotline_file = open('legal.txt', 'r')
    
    for line in hotline_file:
        
        result += line
        
    hotline_file.close()

    return result

legal = get_legal()


def all_db():

    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute('SELECT * FROM users_data')
    
    users_data = cur.fetchall()
    
    result_text = ''
    
    count = 0
    
    for user_chat_id, first_name, user_name in users_data:
        
        count += 1
    
        result_text +='Chat_id:'+str(user_chat_id)+' First_name:'+first_name+' User_name:'+str(user_name)+'\n'
        
    result_text += 'Всего в базе '+str(count)+' пользователей.\n'
        
    con.close()

    cur.close()
    
    return result_text
    
    
def all_db_file():

    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute('SELECT * FROM users_data')
    
    users_data = cur.fetchall()
    
    result_file = open('database.txt', 'w')
    
    result_file.write('Здравствуйте. Здесь представлена база данных пользователей на текущий момент. \r\n')
    
    count = 0
    
    for chat_id, first_name, user_name in users_data:
        
        count += 1
        
        result_file.write('Chat_id:'+str(chat_id)+' First_name:'+first_name+' User_name:'+user_name+'\r\n')
        
    result_file.write('Всего в базе '+str(count)+' пользователей.\r\n')
        
    result_file.close()
        
    result_file = open('database.txt', 'rb')    
    
    con.close()

    cur.close()
    
    return result_file
    
    
def all_buttons_statistics():
    
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute('SELECT * FROM statistics_buttons')
    
    statistics_buttons = cur.fetchall()
    
    result = [0, 0, 0, 0, 0, 0]
    
    for date, hotline, information, contacts, links, legal, photo in statistics_buttons:
            
        result[0] += hotline
        
        result[1] += information
        
        result[2] += contacts
        
        result[3] += links
        
        result[4] += legal
        
        result[5] += photo
    
    result_text = 'Нажатий на кнопку "Горячая линия":'+str(result[0])+'\n'
    result_text += 'На кнопку "О нас":'+str(result[1])+'\n'
    result_text += 'На кнопку "Контакты":'+str(result[2])+'\n'
    result_text += 'На кнопку "Полезные ссылки":'+str(result[3])+'\n'
    result_text += 'На кнопку "Юридический уголок":'+str(result[4])+'\n'
    result_text += 'На кнопку "Фото:"'+str(result[5])+'\n'
    
    con.close()

    cur.close()
        
    return result_text
    
    
def today_buttons_statistics():

    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute("SELECT * FROM statistics_buttons WHERE date='"+str(datetime.date.today())+"'")
    
    statistics_buttons = list(cur.fetchall()[0])
    
    if(statistics_buttons):
        
        result_text = 'Нажатий на кнопку "Горячая линия":'+str(statistics_buttons[1])+'\n'
        result_text += 'На кнопку "О нас":'+str(statistics_buttons[2])+'\n'
        result_text += 'На кнопку "Контакты":'+str(statistics_buttons[3])+'\n'
        result_text += 'На кнопку "Полезные ссылки":'+str(statistics_buttons[4])+'\n'
        result_text += 'На кнопку "Юридический уголок":'+str(statistics_buttons[5])+'\n'
        result_text += 'На кнопку "Фото":'+str(statistics_buttons[6])+'\n'
        
    else:
        
        result_text = 'Нет нажатий за сегодняшний день. \n'
    
    con.close()

    cur.close()    
    
    return result_text
    

def update_db(users_name):
     
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    for chat_id in users_name.keys():
        
        first_name = str(users_name.get(chat_id)[0])

        user_name = str(users_name.get(chat_id)[1])
        
        cur.execute("INSERT INTO users_data (chat_id, first_name, user_name) VALUES ("+str(chat_id)+",'"+first_name+"','"+user_name+"') ON CONFLICT (chat_id) DO UPDATE SET first_name='"+first_name+"', user_name='"+user_name+"'")
        
    con.close()

    cur.close()


def record_id(message_id, chat_id, first_name):
    
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    
    cur = con.cursor()
    
    cur.execute("CREATE TABLE IF NOT EXISTS messages_for_delete_"+first_name+" (message_id integer, chat_id integer)")
        
    cur.execute("INSERT INTO messages_for_delete_"+first_name+" (message_id, chat_id) VALUES ("+str(message_id)+","+str(chat_id)+")")
        
    con.close()

    cur.close()
    
    
def delete_recorded(first_name, bot):
    
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    
    cur = con.cursor()

    cur.execute("SELECT * FROM messages_for_delete_"+str(first_name)+"")
    
    messages_for_delete = cur.fetchall()
    
    try:
        
        for message in messages_for_delete:
        
            bot.delete_message(
                chat_id=message[1],
                message_id=message[0])
    
    except Exception as e:

        cur.execute("DROP TABLE messages_for_delete_"+str(first_name))
        
        
    cur.execute("DROP TABLE messages_for_delete_"+str(first_name))
    
    con.close()

    cur.close()
    

def increment_buttons_db(button_id):
    
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()
    
    cur.execute("SELECT * FROM statistics_buttons WHERE date='"+str(datetime.date.today())+"'")
    
    value = cur.fetchall()
    
    array_value = []
    
    if not value:
        
        array_value = [0, 0, 0, 0, 0, 0, 0]
        
    else:
        
        array_value = list(value[0])
        
    array_value[button_id] += 1
    
    value_str = "'"+str(datetime.date.today())+"',"+str(array_value[1])+","+str(array_value[2])+","+str(array_value[3])+","+str(array_value[4])+","+str(array_value[5])+","+str(array_value[6])
    
    set_value_str="hl="+str(array_value[1])+", inf="+str(array_value[2])+", cn="+str(array_value[3])+", ln="+str(array_value[4])+",lg="+str(array_value[5])+",ph="+str(array_value[6])

    cur.execute("INSERT INTO statistics_buttons (date, hl, inf, cn, ln, lg, ph) VALUES ("+value_str+") ON CONFLICT (date) DO UPDATE SET "+set_value_str)
    
    con.close()

    cur.close()
        

def get_users_name():
    
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()

    users_name = {}
    
    cur.execute('SELECT * FROM users_data')
    
    users_data = cur.fetchall()
    
    for chat_id, first_name, user_name in users_data:
        
        users_name.update({chat_id : [first_name, user_name]})
    
    con.close()

    cur.close()
    
    return users_name 

users_name = get_users_name()


post = ""