# n = int(input('Введите количество парт: '))
# students_on_desk = 2
# print('Kоличество учеников: ', n*students_on_desk)

# n_pictures = int(input('Введите количество картин: '))
# yellow = 4
# red = 5
# green = 5
# blue = 6
# n_crayons = n_pictures*(yellow+red+green+blue)
# print('Нужно карандашей: ', n_crayons)

# a = int(input("Write the number of apples(s):"))
# b = int(input("Write the number of pear(s):"))
# print('The number of apples and pears: ', a + b ,'')

# print("12" == str(6+6))

# a = "12"
# b = 10
# if int(a) > 10:
#     b = b * 2
# if int(a) < 20:
#     b = b + 2
# print(b)

# a = 4
# b = 6
# if a < b:
#     b = b * 2
# if a > b:
#     b = b + 1
# if a == b:
#     b = b - 1
# print(b,)

# a = 13
# b = 12
# b = a - 1
# b = b + 1
# if a < b:
#     b = b * 2
# if a > b:
#     b = b + 5
# if a == b
#     b = b - 5
# print(b,)

# a = 1
# b = a + 1
# print(b - a == a)

# a = "10"
# b = int(a) + 1
# print(int(b) > int(a))

# a = 20
# b = int('20')
# if a > b:
#     print("Больше")
# else:
#     print("Меньше или равно")

# a = 20
# b = 15
# b = a - b
# b = b + 5
# if a > b:
#     print(f"{a} больше {b}")
# elif a < b:
#     print(f"{a} меньше {b}")
# else:
#     print("Переменные равны")

# a = int("15")
# b = 2 * a
# c = a + b
# b = c - b
# if a > b:
#     print(f"{a} больше {b}")
# elif a < b:
#     print(f"{a} меньше {b}")
# else:
#     print("Переменные равны")

# a = 0
# while a <= 10:
# #     a = a + 2
# #     print(f'{a}')

# a = 2
# b = 3
# while a < 9:
#     a = a * 2
#     b = b + 2
# print(f'{a}')

# x = 1
# y = 2
# while x+x+x < y+y+y:
#     x = x * y
#     y = y + 1
# print(x+y)

# a = 5
# b = 10
# while a != 7 and b != 11:
#     a = a + 1
#     b = b + 2
# print(a+b)

# a = 10
# i = 0
# while i < a:
#     i = i + 1
# print(i - 2)

# print(3-1 > 4 or 2 < 3)

# for i in range(4,-2,-1):
#     a = i + i
#     print(a)

# a = 5
# for i in range (0,a+1):
#     print(i)

# a = 0
# b = 2
# for i in range(0,3):
#     a = i * b
#     b = b + 1
# print(a + b)

# numbers = [-6, 3, 8, -12, 7, 5, 13, -1, -14]
# count = 0
# for c in numbers:
#     if c < 0:
#         count = count + 1
# print(count)

# for i in range(1,10):
#     print("Фоксфорд это любовь!")

# numbers = [4, 7, 1, 12, 3]
# numbers[2] = numbers[2] * 3
# numbers[0] = numbers[0] - 2
# print(numbers[0] + numbers[4] * numbers[2])

# one_hundred = ["100", 100, 100-100, "100+100"]
# one_hundred.remove(100)
# print(one_hundred)

# a = 125
# b = 5
# b = a - b * 5
# a = a - b
# print(a)

# a = int(input())
# a = a * 4 + 6 - 2
# print(a)

# print(f"7 * 7 - 7 - 7 = { 7 * 7 - 7 - 7}")

# length = 4
# width = 5
# room_area = length * width
# print(f"Итоговая площадь комнаты равна: {room_area} квадратных метров")

# a = "Привет, мир!"
# print(len(a))

# a = 5
# if a > 5 and a < 10:
#     a = a + 1
#     print(a)
# else:
#     a = a - 1
#     print(a)

# a = 5
# b = 7
# if a != 5:
#     print(a + 1)
# elif b != 7:
#     print(b - 1)
# else:
#     print(a+b)

# a = -24
# b = 3
# while a < 0:
#     a = a + b
#     print(a)

# a = 100
# while a > 1:
#     a = a - 10

# a==0
# b=int(input())
# while b != 0:
#    if b % 3 = 0:
#    a = a + 1
#    b=int(input())
# print(a)

# a = 6
# while a > 2 or a == 1:
#     print(".")
#     a = a - 1
#     print(".")

# a = 1
# b = 1
# while a < 0:
#     a = a + 1
#     b = b + a
#     if b > 10:
#         continue
#     a = a + 1
# print(a)

# colors = ["Красный","Зеленый","Оранжевый","Желтый"]
# colors[2] = "Синий"
# print(colors)

# a = [7,3,4,5]
# b = [1,2]
# a[0] = b
# print(a)

# town_list = ["Москва", "Уфа", "Екатеринбург", "Казань"]
# town_list.append("Нижний Новгород")
# print(len(town_list))

# twelve_list = ["1212", 12, "двенадцать", "12*12", 12-12]
# twelve_list.remove(twelve_list[2])
# twelve_list.remove(12)
# print(twelve_list)

# a = 2
# for i in range(1,7):
#     a = a + i
# print(a)

# for i in range(1,15,3):
#     print('*')

# a = "прапрапрапрапрапрапрапрапрапрапрадедушка"
# print(a.count("пра"))

# a = int(input("Введите неотрицательное целое число: "))
# b = 0
# while a > 0:
#     b = b + a * 2
#     a = a - 1
# print(b)

# def f(a,b):
#     a = a + 5
#     b = b - 2
#     print (a + b)
# f(-3,2)

# def f(n):
#     for i in range(2, n+1):
#         print(i)
# f(4)

# def app_list():
#    numbers = []
#    for i in range(1,9,2):
#         numbers.append(i)
#    print(numbers)
# app_list(numbers)

# def strange_number(a, b):
#     return a + b - a*b
# a = 10
# b = 11
# strange_number(a, b)

# def strange_number(a, b):
#     return a + b - a*b
# a = 10
# b = 11
# strange_number(a, b)

# import random
# random.randint(1,16)

# import random
# score = random.randint(4,5)
# print(score )

# import random
# random.randint(44,55)

# random import
# number = random.int(-100,101)
# if number > 0:
#     print(f"Случайное число {number} - положительное")
# elif number < 0:
#    print(f"Случайное число {number} - отрицательное")
# else:
#     print('Случайное число равно 0')

# a = 3
# b = 4
# if a > b:
#     print(a)
# if a < b:
#     print(b)

# a = "Мистер фокс"
# b = "Мистер Фокс"
# if a == b:
#     print("Переменные равны")
# if a != b:
#     print("Переменные не равны")

# print(2)
# a = 5
# print(2)
# b = "5"
# if a == b:
#     print(2)
# if a >= int(b):
#     print(2)
#     print(2)

# print(14=="14")

# a ='9484738194857'
# if a[3]=='4':
#     print('Равно')
# if a[3]!='4':
#     print('Не равно')

# a = 10
# b = 9
# if a > b:
#     print(a-b)
# else:
#     print(b-a)

# a = 1
# b = a + 2
# c = b + 3
# b = c - b
# if a >= b:
#     print(f"a + b = {a+b}")
# elif a >= c:
#     print(f"a + b = {a+c}")
# else:
#     print(f"c + b = {c+b}")

# import turtle
# t = turtle. Turtle()
# t.shape("turtle")
# t.lt(180)
# t.fd(130)

# import turtle
# t = turtle. Turtle()
# t.shape("turtle")
# t.lt(75)
# t.fd(130)
# t.rt(150)
# t. fd(130)
# t.penup()
# t.bk(60)
# t.pendown()
# t.rt(105)
# t. fd(40)

# import turtle
# t = turtle. Turtle()
# t.shape("turtle")
# t.circle(50)
# t.rt (90)
# t. fd(100)
# t.lt (90)
# t. fd(100)
# t.rt (90)
# t.circle(50)
# t.rt (90)
# t. fd (200)
# t.rt (90)
# t.circle(50)
# t.rt (90)
# t. fd(100)

# import turtle
# t = turtle. Turtle()
# t.shape("turtle")
# t.lt (45)
# t. fd (100)

# import turtle
# t = turtle. Turtle()
# t.shape("turtle")
# t.rt(0)

# import turtle
# t = turtle.Turtle()
# t.speed(0)
# # t.penup()
# t.goto(45, 45)

# import turtle
# t = turtle.Turtle() 
# t.shape("turtle") 
# t.penup() 
# t.rt(90) 
# t.fd(100) 
# t.pendown() 
# t.lt(90) 
# t.bk(100)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.fd(100)
# t.bk(20)
# t.rt(270)
# t.fd(40)
# t.bk(60)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# t.bk(100)
# t.lt(90)
# t.fd(30)

# import turtle
# t = turtle.Turtle() 
# t.shape("turtle") 
# t.penup() 
# t.rt(90) 
# t.fd(100) 
# t.pendown() 
# t.lt(90) 
# t.bk(100)

# import turtle
# t = turtle.Turtle()
# t.hideturtle()
# t.circle(25)

# import turtle
# t = turtle.Turtle()
# t.color('red')
# t.goto(35,100)

# import turtle
# t = turtle.Turtle()
# t.shape("сircle")
# t.shapesize(10)

# import telebot
# import my_token
# token = my_token.m_t

# bot = telebot.TeleBot('свой токен')
# @bot.message_handler(content_types=['text'])
# def start(message): 
#     if message.text == '/start':
#         bot.send_message(message.from_user.id, "Привет, как тебя зовут?")
#         bot.register_next_step_handler(message, get_name)
#     else:
#         bot.send_message(message.from_user.id, 'Напиши: /start')
 
# def get_name(message):
#     bot.send_message(message.from_user.id, 'Тебя зовут '+ message.text + '?')
#     bot.register_next_step_handler(message, answer)
# def answer(message):
#     if message.text == "Да":
#         bot.send_message(message.from_user.id, "Красивое имя!")
#     else:
#         bot.send_message(message.from_user.id, "Простите, я ошибся(")

# bot.polling(none_stop=True, interval=0)

# from tt import gTTS
# my_text = 'Привет!'
# language = ''
# result = gTTS(text=my_text, lang=language, slow=False)
# result.save("file_name.")

# print(10/2)

# storage = ()
# for i in range (3):
#     storage.append(i)
# print (storage)

# massive = int(input())
# spisok = []
# a = 0
# while massive != a:
#     a = a + 1
#     spisok.append(a)
# spisok.remove(a)
# spisok.insert(0, a)
# print(spisok)

# massive = int(input())
# spisok = []
# a = 0
# while massive != a:
#     a = a + 1
#     spisok.append(a)
# spisok.remove(a)
# spisok.insert(0, a)
# print(spisok)

# def count_dies():
#     print('fa')

# x = 7
# y = 11
# if x > y:
#    x += 1
# else:
#    if x > 6:
#        x -= 1
#    else:
#        x += 2
# print(x)

# n, m = map(int, input().split()) 
# if n * m % 2 == 0:
#     print (n * m // 2)
# else:
#     print(n * m // 2 + 1)

# x, y, z, n = map(int, input().split())
# if x == z or y==t:
#     print("yes")
# else:
#     print("no")

# a, b, c, d = map(int, input().split())
# if abs(a - c) == abs(b - d) or a == c or b == d:
#     print("yes")
# else:
#     print("no")

# print("fox\n"*10)

# for x in range(3):
#     print(100)

# for x in range(1, 51):
#     print(x, end = ' ')

# for x in range(100, -1, -2):
#     print(x, end = ' ')

# from time import *

# while True:
#     for x in range(100):
#         print(x)
#         sleep(1)

# n = int(input())
# for x in range(1, n +1):
#     print(x, end = ' ')

# n = int(input())
# for x in range(n, 0, -1):
#     print("*"*x)

# n = int(input())
# ans = 0
# for x in range(1, n + 1):
#     ans = ans + x
# print(ans)

# n = int(input())
# ans = 0
# for x in range(n):
#     tmp = int(input())
#     ans += tmp
# print(ans)

# n=int(input())
# for i in range(1,n+1):
#     print((' '*(n-i+1)+'*'*(i-1))+'*'*i)
# for j in range(1,n+1):
#     print((' '*(j-1)+('*'*(n-j+1)))+'*'*(n-j+2))
# print(' '*n+'*')
# # вот вам ромбик

# ans = 1
# n = int(input())
# for x in range(1, n + 1):
#     ans = ans*x
# print(ans)

# sum1 = 0
# for i in range(20):
#     if ((i % 2 == 0) and (i % 3 == 0)) or (i % 5 == 0):
#         sum1 += i
#         print(sum1)


# a, b, c, d, e, f, g, h, i, j = map(int, input().split())

# golov = int(input())
# srub = 0
# for x in range(10):
#     a = int(input())
#     srub = srub + a
# if golov - srub == 0 or 1:
#     print('YES')
# else:
#     print('NO')

# dz = 5
# d = 0
# while 99999 - dz >= 0:
#     d += 1
#     dz = dz * 2
# print(d)

# x = 2 ** 100
# t = 0
# while x != 0:
#     t += x % 10
#     x = x // 10
# print(t)

# ts = 1
# thr = 0
# while ts != 0:
#     if ts % 3 == 0:
#         thr += 1
#     ts = int(input())
# print(thr)

# x = str(2**1000)
# x = len(x)
# print(x)

# x = 3
# s = 3
# while x != 2015:
#     x += 4
#     s += x
# print(s)

# x1 = input()
# x2 = input()
# if 65 <= ord(x1) <= 122 and 49 <= ord(x2) <= 57:
#     print("YES")

# x1 = input()
# x2 = input()
# if x1.isalpha() and x2.isdigit() == True or x2.isalpha() and x1.isdigit() == True:
#     print("YES")
# else:
#     print("NO")

# a = 998
# b = 992
# res = a * b
# while a != -2:
#     res = res - (a - 10) * (b - 10) + (a - 20) * (b - 20)
#     a -= 20
#     b -= 20
# print(res)

# a = 99
# res = a ** 2
# while a != -1:
#     print(res)
#     res = res - (a - 2) ** 2 + (a - 4) ** 2
#     a -= 4
# print(res)

# n = 1
# n *= 4
# print(n)

# res = 1
# n = 1
# m = 2 ** n + 3 ** n
# while n != 1024:
#     res = res * m
#     n *= 2
# print((res + 2 ** 1024) / 3 ** 1024)
# print(res)

# print(ord('F')+ord('R')+ord('O')+ord('G'))

# print(len(str(31 ** 123)))

# s = '34'
# print(s[1])

# ch = input()
# stat = (ch[: :-1] == ch)
# if stat == True:
#     print('yes')
# else:
#     print('no')
# # То же самое что и
# ch = input()
# if ch[: :-1] == ch:
#     print('yes')
# else:
#     print('no')

# ch = input()
# if ch[0:6] == 'Hello!':
#     print(ch[6:])
# else:
#     print(ch)

# ch = input()
# if 95 <= ord(ch[0]) <= 122:
#     print('YES')
# else:
#     print('NO')

# ch = input()
# if 95 <= ord(ch[0]) <= 122 and 95 <= ord(ch[-1]) <= 122:
#     print('YES')
# else:
#     print('NO')

# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)

# s = input()
# ans = ''
# tmp = ''
# if len(s) % 2 == 1:
#     tmp = s[-1]
#     s = s[:-1]
# for i in range(0, len(s) - 1, 2):
#     ans = ans + s[i + 1] + s[i]
# ans += tmp
# print(ans[::-1])

# a = '04134'
# print(a.find('1'))

# alph = "abcdefghijklmnopqrstuvwxyz"
# realph = "zyxwvutsrqponmlkjihgfedcba"
# word = input()
# nom = -1
# reword = ''
# for i in range(len(word)):
#     reword += realph[alph.find(word[nom + 1])]
#     nom += 1
# print(reword)

# alph = "abcdefghijklmnopqrstuvwxyz"
# #       zyxwvutsrqponmlkjihgfedcba
# word = input()
# reword = ''
# num = -1
# for i in range(len(word)):
#     reword += alph[(alph.find(word[num + 1]) + 1) * -1]
#     num += 1
# print(reword)

# reword = ''
# num = -1
# word = 'kot'
# reword += word[num * 2]
# print(reword)

# num = -3
# print(num * -1 + (num * -1 - 1))

# print('r для расшифровать или z для зашифровать.')
# pac_il_shif = input()
# if pac_il_shif == 'z' or 'r':
#     alph = "abcdefghijklmnopqrstuvwxyz"
#     word = input()
#     reword = ''
#     key = int(input()) % 26
#     num = -1
#     if pac_il_shif == 'z':
#         for i in range(len(word)):
#             if word[num + 1]:
#                 reword += alph[alph.find(word[num + 1]) + key]
#                 num += 1
#     elif pac_il_shif == 'r':
#         for i in range(len(word)):
#             if word[num + 1]:
#                 reword += alph[alph.find(word[num + 1]) - key]
#                 num += 1
#     print(reword)

# alph = "ABCDEFGHIJKLMNOPQRSYUVWXYZ"
# word = input()
# reword = ''
# k = int(input()) % 26
# num = -1
# for i in range(len(word)):
#     if word[num + 1]:
#         reword += alph[(alph.find(word[num + 1]) - k) % 26]
#         num += 1
# print(reword)

# s = 'ФОКСФОРД'
# A = list(s)
# s = '**'.join(A)
# print(len(s))

# A = [1,2,3,4,5,6,7]
# print(A[-1:1:-1])
# print(A[::2])

# A = [1, 2, 3, 4, 5]
# print(sum(A[::2]))

# s = 'мама мыла раму'
# print('у'.join(s.split('а')))

# A = [10,2, 30, 4, 5]
# print(A[1] + A[-1])

# A = []
# A.append(1)
# A.append(2)
# A.append(3)
# A.pop(1)
# A.pop()
# print(A)

# A = []
# for i in range(5):
#     A.append(i)
# A = A * 2
# A = A * 100
# print(A.count(1))

# A = [10, 1, 20, 2, 30, 3]
# B = A[1:3] + A[2:]
# print(len(B))

# A = [1, 2, 3, 4, 5, 6]
# A[::2] = [0, 0, 0]
# print(A)

# A = [1, 2, 3, 4, 5, 6]
# A[1],A[-1] = A[-1],A[1]
# print(A)

# A = [1, 2, 3, 4, 5, 6]
# A[2:4] = []
# print(A)

# s = 'мама мыла ламу'
# A = s.split('a')
# print(A)

# s = 'crocodile'
# A = s.split('o')
# print('*'.join(A))

# s = 'молоко'
# A = s.split('о')
# print(A)

# for x in range(10):
#     for y in range(8):
#         print(y, end = ' ')
#     print()

# print('r для расшифровать или z для зашифровать.')
# pac_il_shif = input()
# if pac_il_shif == 'z' or 'r':
#     alph = "abcdefghijklmnopqrstuvwxyz"
#     word = input()
#     reword = ''
#     key = int(input()) % 26
#     num = -1
#     if pac_il_shif == 'z':
#         for i in range(len(word)):
#             if word[num + 1]:
#                 reword += alph[alph.find(word[num + 1]) + key]
#                 num += 1
#     elif pac_il_shif == 'r':
#         for i in range(len(word)):
#             if word[num + 1]:
#                 reword += alph[alph.find(word[num + 1]) - key]
#                 num += 1
#     print(reword)

# n = 7
# for i in range(n,0,-1):
#     print('*'*i)

# def getSum(n):
#     sum = 0
#     for digit in str(n): 
#       sum += int(digit)      
#     return sum
# n = 5**20
# print(getSum(n))

# s = input()
# s = s.split(' ')
# A = ''
# for i in range(len(s)):
#   if i % 2 == 1:
#     A += s[i] + ' '
# print(A)

# A = list(input().split())
# A = A[-1:] + A[:-1]
# print (' '.join(A))

# s = input()
# s = list(s.split(' '))
# A = ''
# for i in range(len(s)):
#     if i != len(s) - 1:
#         A += s[i+1] + ' '
#     else:
#         A += s[0]
# print(A)

# s = input()
# s = list(s.split(' '))
# n = len(s)
# A = ''
# for i in range(len(s)):
#     if i != len(s) - 1:
#         A += s[i+1] + ' '
#     else:
#         A += s[0]
# print(A)

# s = input()
# s = list(s.split(' '))
# N = len(s)
# A = 0
# for i in range(N-1):
#     A += abs(int(s[i]) - (int(s[i+1])))
# print(A)

# n, k = map(int, input().split())
# t = [0 for _ in range(n + 1)]
# for _ in range(k):
#     m, p, s = map(int, input().split())
#     t[m] -= s
#     t[p] += s
# print(*t[1:])


# a = 2
# for i in range(100):
#     oneortwo = input()
#     if oneortwo == "1":
#         a = a-5
#         print(a)
#     if oneortwo == "2":
#         a = 2*a
#         print(a)
#     if oneortwo == "stop":
#         print(a)
#         break

# numb = int(input("Введите целое число: "))
# print("Результат:", end = " ")
# for i in range(numb - 1, 1, -1):
#     if (numb % i == 0):
#         print(i, end = " ")

# a = - 5
# b = - 3
# a = a * a
# a = a - b
# print(a)

# a = float(input())
# b = 5.6
# print(b + a)

# print(" /)/)\n(':')\n|'||'|\nHello!\nMy name is Clever!")

# print("\"%\\\\||//%\"")

# print(":)\_____/(:\n {(@)v(@)}\n {|~- -~|}\n {/^'^'^\}\n ===m-m===")

# name = input()   
# print("Hello,", name, sep="")

# a, b = map(int, input().split())
# c = a - b
# print(a,"-", b,"=", c, sep="")

# b = int(input())
# n = int(input())
# print(b*n)

s = int(input())
h = s//3600
m = s%60
s = s%3600
print(f"{h//10}{h%10}:{m//10}{m%10}:{s//10}{s%10}")

