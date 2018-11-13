# -*- coding: utf-8 -*-


news = '''
'''


def update_db(users_chat_id):
    
    database = open('database.txt', 'w')
    
    for username, chat_id in users_chat_id.items():
        
        database.write(username+' '+chat_id)
    
    database.close()
    
def get_username(line):
    
    return line.split(' ')[0]

def get_chat_id(line):

    return line.split(' ')[1]      

def get_users_chat_id():
    
    users_chat_id = {}
    
    database = open('database.txt', 'r')
    
    for line in database:

        users_chat_id.update({get_username(line) : get_chat_id(line)})
        
    database.close()

    return users_chat_id

users_chat_id = get_users_chat_id()




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


contacts = []

contacts.append('''https://vk.com/id420868047 ''')

contacts.append('''�. +7 921 255-93-23 Сергей
https://vk.com/id320895361''')

contacts.append('''Т. +7 927 611-91-55  Александр 
https://vk.com/remar.samara
https://vk.com/club160641988
https://www.youtube.com/channel/UCteNh6vjfRJR-wow7r3CjVw
https://instagram.com/reabcentr_remar?utm_source=ig_profile_share&igshid=j6p0m13iq6co
https://m.ok.ru/dk?st.cmd=newRegProfile&tkn=5884&_prevCmd=fbAuth#_=_
https://www.facebook.com/remar.reabcentr.samara/
''')

contacts.append('''АНО ЦАНЗ Социальный проект «Здоровое Черноземье»
Т. 8-920-223-66-65 Георгий
https://vk.com/id410874012
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber
https://vk.com/reabvrn
https://www.instagram.com/reabcentrvoronezh/
''')

contacts.append('''Т.8-920-527-54-33 Артем
https://vk.com/id410874012
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber
https://vk.com/reabvrn
https://www.instagram.com/reabcentrvoronezh/
''')

contacts.append('''Т.8-920-080-93-11 Антон
https://vk.com/id410874012
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber
https://vk.com/reabvrn
https://www.instagram.com/reabcentrvoronezh/
''')

contacts.append('''Т.8-920-468-40-25 Владимир
https://vk.com/id410874012
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber
https://vk.com/reabvrn
https://www.instagram.com/reabcentrvoronezh/
''')

contacts.append('''Т.8-927-092-33-69 Рафаэль
https://vk.com/id410874012
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber
https://vk.com/reabvrn
https://www.instagram.com/reabcentrvoronezh/
''')

contacts.append('''Т.8-920-222-09-07
https://vk.com/id410874012
https://www.youtube.com/channel/UCwMiaCxpht6c0Kk7BfGjObw?view_as=subscriber
https://vk.com/reabvrn
https://www.instagram.com/reabcentrvoronezh/
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т. +7 926 612-36-33 Эдуард Лебедев
Вк:  https://vk.com/zdregion
Инстаграм:  https://instagram.com/zdregion 
Фейсбук : https://m.facebook.com/groups/209013159681361
''')

contacts.append('''Т.8928-444-14-90
https://www.instagram.com/pro_life_sochi/
https://vk.com/prozhiznsochi
''')

contacts.append('''https://vk.com/reba2018''')

contacts.append('''АНОСП "ХОРОШИЕ ЛЮДИ"
Т.+7-928-301-06-01 Базров Сослан 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67
''')

contacts.append('''АНОСП "ХОРОШИЕ ЛЮДИ"
Т.+7-928-301-06-01 Базров Сослан 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67
''')

contacts.append('''АНОСП "ХОРОШИЕ ЛЮДИ"
Т.+7-928-301-06-01 Базров Сослан 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67
''')

contacts.append('''АНОСП "ХОРОШИЕ ЛЮДИ"
Т.+7-928-301-06-01 Базров Сослан 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67
''')

contacts.append('''АНОСП "ХОРОШИЕ ЛЮДИ"
Т.+7-928-301-06-01 Базров Сослан 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67
''')

contacts.append('''АНОСП "ХОРОШИЕ ЛЮДИ"
Т.+7-928-301-06-01 Базров Сослан 
https://instagram.com/horoshielydi777?utm_source=ig_profile_share&igshid=1p2s1ly961c67
''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
 ''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
''')

contacts.append('''АНО СЗОЖ "Стремление жить"
Т. +7 928 766-57-57 +7 928 766-57-57 Максим
 https://ok.ru/group/54484228898942
 https://vk.com/stremleniezity
 https://www.facebook.com/anoszh/?ref=bookmarks
 https://instagram.com/p/Boleo6HhsWr/
''')
 
contacts.append('''АНО 
Т. +7 928 497-99-82 Артем
https://vk.com/id408141585
https://www.instagram.com/p/Bp91hIcHZ1J/?utm_source=ig_share_sheet&igshid=1ma9yic0ggtze
''')