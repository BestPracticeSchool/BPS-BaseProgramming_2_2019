# Задание 2. Уровень - если их не поздравить, они не займут сотку.
# Условие : Всем мы знаем, как важно поздравлять друзей и коллег с Днем Рождения.
# Именно в этот день человек приближается к увяданию и забвению. Но Вы очень хитрый.
# Вы знаете, что если не поздравить человека вовремя, то в момент, когда Вашему бизнесу понадобится добавочный капитал,
# огорченные друзья не помогут вам небольшим займом. Поэтому Вы решили создать программу, которая помнит дни рождения,
# всех ваших друзей.

# Входные данные: в первой строке записано натуральное число N - количество ваших коллег и друзей.
# Затем, в N строках записана информация о днях рождениях. Каждая строчка состоит из трёх частей, разделенных
# пробелом - имя, месяц и день.
# Имя - строка русских букв, месяц - "декабрь","январь","февраль","март",....,"октябрь","ноябрь", день - число от 1 до 31
# Считаем, что в каждом месяце у Вас ровно 31 день.
# Имена всех ваших коллег различны.


# В следующей строчке записано натуральное число M — количество вопросов, на которое надо ответить.
# В следующих M строках содержатся сами вопросы. 
# Вопрос — это название месяца в том же формате, в котором они задаются выше.



# Выходные данные: для каждого вопроса в отельной строчке через пробел вывеите имена всех коллег и их дни рождения,
# которые родились в данном месяце. Информацию необходимо упорядочить по дню рождения. Если два человека родились в один день 
# одного месяца - выведите информацию о них в лексикографическом порядке имен.


# Если в заданном месяце никто не родился, выведите "ФУХ НИКОГО НЕТ"


# Пример:
# Ввод                                                      Вывод
# 4
# Ваня 20 январь
# Петя 15 июнь
# Вася 10 январь
# Рикардо 20 июля
# 3
# июнь
# декабрь
# январь                                                   Петя 15
#                                                          ФУХ НИКОГО НЕТ
#                                                          Вася 10 Ваня 20 