# -*- coding: utf-8 -*-


news = '''
'''


def get_links():
    
    result = ''
    
    links = open('links.txt', 'r')
    
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


information = '''
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