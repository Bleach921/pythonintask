# Задача 4, Вариант 12 
# Напишите программу, которая выводит имя, под которым скрывается Лариса Петровна Косач-Квитка. Дополнительно необходимо вывести область интересов
# указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти).
# Для хранения всех необходимых данных требуется использовать переменные. После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

# Мамедов Р.А.
# 16.03.2016


print("Лариса Петровна Косач-Квитка более известена, как  украинская писательница Леся Украинка")

born = 1871 
death = 1913
age = 1913 - 1871
place = "Новоград-Волынский,Волынская губерния,Российская империя"
interess = "литература"

print("Место рождения:",place)
print("Год рождения:",born)
print("Год смерти:",death)
print("Возраст:",age)
print("Область интересов:",interess)

input("Нажмите Enter для выхода")