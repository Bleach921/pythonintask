# Задача 9. Вариант 22.
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен
# его отгадать. Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток
# узнать, есть ли какая-либо буква в слове, причем программа может отвечать только
# "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Щербаков Р.А.
# 22.05.2016

import random

words="Сессия","Питон","Автомат","РГСУ","Расписание"
rand=random.randint(0,4)
massiv=list(words[rand].lower())
print("Ты попал на поле чудес, только тут мы не говорим где находится буква которую \
угадаешь.\nТема: Учеба\nБукв: "+str(len(massiv)))
popitka=5
inp=""
text="Угадали"
while popitka!=0:
     if input("У тебя "+str(popitka)+" попыток\nВведите букву: ") in massiv:
	     print("Да")
     else:
	     print("Нет")
     popitka-=1
while inp.lower()!=words[rand].lower():
     inp=input("Введите слово: ")
     if(inp.lower()=="я слабак"):
	     inp=words[rand]
	     text="Слабак"
     elif(inp.lower()==words[rand].lower()):
	      text="Угадали"
     else:
	     print("Попытайтесь еще раз\nНаберите 'Я слабак' для выхода")
input("\nВы "+text)
