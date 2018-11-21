# -*- coding: utf-8 -*-


import connect


news = '''
'''


def get_information():
    
    result = ''
    
    information_file = open('information.txt', 'r')
    
    for line in information_file:
        
        result += line
        
    information_file.close()

    return result

information = get_information()


contacts = []

contacts.append('''Т.8-800-500-28-13
https://vk.com/id420868047 
''')

contacts.append('''Т. +7 921 255-93-23 Сергей
https://vk.com/id320895361
''')

contacts.append('''Т. +7 927 611-91-55  Александр 
''')

contacts.append('''АНО ЦАНЗ Социальный проект «Здоровое Черноземье»
Т. 8-920-223-66-65 Георгий
https://vk.com/id410874012
''')

contacts.append('''Т.8-920-527-54-33 Артем
https://vk.com/id410874012
''')

contacts.append('''Т.8-920-080-93-11 Антон
https://vk.com/id410874012
''')

contacts.append('''Т.8-920-468-40-25 Владимир
https://vk.com/id410874012
''')

contacts.append('''Т.8-927-092-33-69 Рафаэль
https://vk.com/id410874012
''')

contacts.append('''Т.8-920-222-09-07
https://vk.com/id410874012
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард 
''')

contacts.append('''Т.8928-444-14-90
https://vk.com/prozhiznsochi
''')

contacts.append('''+7 928 215-63-54 Иван
https://vk.com/reba2018
''')

contacts.append('''Т.+7-928-301-06-01 Базров Сослан 
https://vk.com/id361427938
''')

contacts.append('''Т. +7 928 766-57-57 +7 928 766-57-57 Максим
https://vk.com/id395722415
''')

contacts.append('''Т. +7 928 497-99-82 Артем
https://vk.com/id408141585
''')


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


def get_users_name():
    
    con = connect.create_connect()

    con.set_isolation_level(connect.psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = con.cursor()

    users_name = {}
    
    cur.execute("INSERT INTO users_data VALUES (1341, 'Александр', 'Известняк')")
    
    cur.execute('SELECT * FROM users_data')
    
    users_data = cur.fetchall()
    
    for chat_id, first_name, user_name in users_data:
        
        users_name.update({chat_id : [first_name, user_name]})
    
    con.close()

    cur.close()
    
    return users_name 

users_name = get_users_name()


