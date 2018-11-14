# -*- coding: utf-8 -*-


news = '''
'''


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


links = '''
Наш основной сайт посвященный программе исход: 
www.reabcentr.ru 

Наша страница в соц сет 
https://vk.com/reabcentr 
https://www.facebook.com/profile.php?id=100022533604301

Центр матери и ребёнка «Мир» 
https://vk.com/id420868047 

АНО СЗОЖ «Здоровый регион»
Москва и московская область, Калининградская область, Калужская область, Тверь и Рязань:
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361

АНО ЦАНЗ "Социальный проект Здоровое Черноземье"
Центральное черноземье: 
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber 
https://vk.com/reabvrn 
https://www.instagram.com/reabcentrvoronezh/ 
https://www.facebook.com/groups/2107970306153588/?ref=group_header

АНОСП "Здоровый город"
Краснодарский край и республика Адыгея 
https://anti-narko.ru 
https://vk.com/club_zdoroviy_gorod_krasnodar 
https://www.instagram.com/zdorovyi_gorod_krasnodar/ 

СРБОО"РЕМАР"
Поволжье: 
https://vk.com/remar.samara 
https://vk.com/club160641988 
https://www.youtube.com/channel/UCteNh6vjfRJR-wow7r3CjVw 
https://instagram.com/reabcentr_remar?utm_source=ig_profile_share&igshid=j6p0m13iq6co 
https://m.ok.ru/dk?st.cmd=newRegProfile&tkn=5884&_prevCmd=fbAuth#_=_ 
https://www.facebook.com/remar.reabcentr.samara/ 

АНО СЗОЖ "СТРЕМЛЕНИЕ ЖИТЬ"
Ростовская область: 
https://ok.ru/group/54484228898942 
https://vk.com/stremleniezity 
https://www.facebook.com/anoszh/?ref=bookmarks 
https://www.instagram.com/anoszh/ 

АНОСП "Хорошие Люди"
Ставропольский Край и Астрахань: 
https://vk.com/club39201093 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67

КРОо Сркис «Про-жизнь»
Черноморское Побережье: 
https://vk.com/prozhiznsochi 
https://www.instagram.com/pro_life_sochi/ 

АНО «Здоровая Абхазия»
Владикавказ: 
https://vk.com/id408141585 
https://www.instagram.com/p/Bp91hIcHZ1J/?utm_source=ig_share_sheet&igshid=1ma9yic0ggtze
'''

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