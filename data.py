# -*- coding: utf-8 -*-


news = '''
'''


def get_information():
    
    result = ''
    
    links = open('information.txt', 'r')
    
    for line in links:
        
        result += line

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
    
    links = open('links_test.txt', 'r')
    
    for line in links:
        
        result += line

    return result

links = get_links()


def update_db(users_username):
    
    database = open('database.txt', 'w')
    
    for chat_id, username in users_username.items():
        
        database.write(chat_id+' '+username)
    
    database.close()

def get_users_username():
    
    users_username = {}
    
    database = open('database.txt', 'r')
    
    for line in database:

        users_username.update({line.split(' ')[0] : line.split(' ')[1]})

    database.close()   
    
    return users_username 

users_username = get_users_username()


