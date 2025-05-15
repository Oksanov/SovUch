import random as r
import time as t

end = 0
start = 0
answer = 0
error = 0
counter = 0
fir = 0
sec = 0
a = 0

language = int(input('Установите язык/Install the language Для выбора подросткового напишите 1, для матерного 2, для стандартного русского 3. If you want to choose English type 4. '))

if language == 3:
    level = int(input('На каком уровне хотите играть? 1, 2 или 3?'))
    if level == 1:
        b = 10
    elif level == 2:
        b = 100
    elif level == 3:
        b = 1000
# while counter != 3 and error != 3:
def vopros():
    fir = r.randint(a, b)
    sec = r.randint(a, b)
    print(f'Чeмy равна сумма {fir} и {sec}?')
    start = t.time()
    answer = int(input())
    end = t.time()
    if answer == (fir + sec):
        if (end - start) <= 10:
            counter += 1
            print(f"Молодец")
        else:
            error += 1
            print()
    else:
        error += 1 
print(f'Количество верных ответов: {counter}')
print (f'Kоличество неверных ответов: {error}')
print (f'Время: {end - start}')
if counter == 5: 
    print("Воу воу воу, чувак! Дай мне выиграть!")
else:
    print('Ты проиграл! Попробуй еще раз, лох.')
if error == 3:
    print("АЗХАЗХАЗХАЗХАЗХА ЛОШАРА!")