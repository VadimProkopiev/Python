# print('a', 'b', 'c', sep='*')
# print('d', 'e', 'f', sep='**', end='')
# print('g', 'h', 'num', sep='+', end='%')
# print('j', 'k', 'l', sep='-', end='\n')
# print('m', 'n', 'o', sep='/', end='!')
# print('p', 'q', 'r', sep='1', end='%')
# print('s', 't', 'u', sep='&', end='\n')
# print('v', 'w', 'x', sep='%')
# print('y', 'z', sep='/', end='!')
# ____________________________________________
# a = int(input())
# print(a)
# print(a+1)
# print(a+2)
# _____________________________________________
# a = int(input())
# b = int(input())
# print(3*(a+b)*(a+b)*(a+b)+275*b*b-127*a-41)
# _________________________________________________
#  a = int(input())
# print('Следующее за числом', a, 'число: ', a+1)
# print('Для числа', a, 'предыдущее число: ', a-1)
# ______________________________________________________
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print((a+b+c+d)*3)
# _______________________________________________________
# a = int(input())
# b = int(input())
# print(a, "+", b, "=", a+b)
# print(a, "-", b, "=", a-b)
# print(a, "*", b, "=", a*b)
# _____________________________________________
# a1 = int(input())
# d = int(input())
# n = int(input())
# print(a1+d*(n-1))
# ____________________________________________
# x = int(input())
# print(x, 2*x, 3*x, 4*x, 5*x, sep="---")
# ____________________________________________________________________________________________________________
# x = int(input())
# print(x, end="...")
# print(2*x, end="...")
# print(3*x, end="...")
# print(4*x, end="...")
# print(5*x)
# print("*******************")
# print("*                 *")
# print("*                 *")
# print("*******************")
# a = int(input())
# b = int(input())
# print('Квадрат суммы', a, 'и', b, "равен", ((a+b)**2))
# print('Сумма квадратов', a, 'и', b, "равен", (a**2+b**2))
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# print(a**b+c**d)
# n = int(input())
# print(n*100+(n+n)*10+(n+n+n))
# n = int(input())
# if n >= 2:
#     for num in range(n):
#         print("*" * (n-num))
# ____________________________________________________________________________________________________________
# num = int(input())
# count = 0
# while num > 0:
#     if num >= 25 and num % 25 >= 0:
#         count += 1
#         num = num-25
#     if 25 > num >= 10 and num % 10 >= 0:
#         count += 1
#         num = num - 10
#     if 10 > num >= 5 and num % 5 >= 0:
#         count += 1
#         num = num-5
#     if 5 > num >= 1 and num % 1 >= 0:
#         count += 1
#         num = num - 1
# print(count)
# ____________________________________________________________________________________________________________
# total = 0
# count = 0
# for a in range(26, 28):
#     for b in range(83, 85):
#         for c in range(110, 111):
#             for d in range(100, 140):
#                 for e in range(140, 150):
#                     if a**5+b**5+c**5+d**5 == e**5:
#                         total += 1
#                         count += 1
#                         f = a+b+c+d+e
#                         print(f)
#                         break
#                     count += 1
# print('Общее количество натуральных решений =', total)
# print(count)
# ____________________________________________________________________________________________________________
# e = 0
# count = 0
# for a in range(1, 33):
#     for b in range(1, 33):
#         for c in range(1, 33):
#             for d in range(1, 33):
#                 if a**3+b**3 == c**3+d**3 and a != b and a != c and a != d and b != c and b != d and c != d:
#                     print(a**3+b**3)
#                 count += 1

# print(count)
# ______________________Числовая Угадайка________________________________________________________________________
# import random
# a = 0
# b = 0
# n = "y"
# while n == "y" or n == "Y":
#     def ugadaika(a, b):
#         count = 1
#         print('Добро пожаловать в числовую угадайку')
#         m = int(input('Введите предел выбора случайного числа: '))
#         a = random.randint(1, m)
#         print("Введите число от 1 до", m)

#         def is_valid(num):
#             if 0 < num <= m:
#                 return True
#             else:
#                 return False
#         while a != b:
#             b = int(input('Введите ваше число: '))
#             is_valid(b)
#             if is_valid(b) == False:
#                 print('Может быть все-таки введем число от 1 до', m, '?')
#             if is_valid(b) == True:
#                 if a > b:
#                     print('Ваше число меньше загаданного, попробуйте еще разок')
#                 if a < b:
#                     print('Ваше число больше загаданного, поробуйте еще разок')
#             if a == b:
#                 return print('Вы угодали, поздравляем!'), print('Колличество попыток =', count)
#             count += 1
#     ugadaika(a, b)
#     print('Хотите ли Вы сыграть еще раз? введите Y/N')
#     n = input()
#     if n == 'Y' or n == "y":
#         ugadaika(a, b)
#     if n == 'N' or n == 'n':
#         print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
# __________________________________________Магический шар 8__________________________________________________________________
# import random
# answers = ["Беспорно", "Предрешено", "Никаких сомнений", "Определенно да", "Можешь быть уверен в этом", "Мне кажется да", "Вероятнее всего", "Хорошие перспективы", "Знатоки говорят да", "Да", "Пока неясно, попробуй снова",
#            "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

# print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# name = input('Как Вас зовут: ')
# print('Привет', name, "!")
# s = 'y'
# while s == "Y" or s == "y" or s == "ДА" or s == "Да" or s == "дА" or s == "да":

#     def choice(answers):
#         m = input('Введите свой вопрос:  ')
#         n = random.randint(0, 20)
#         print()
#         print(answers[n])
#         print()

#     choice(answers)
#     print("Хотите ли Вы задать еще вопрос, Y/N, Да/Нет")
#     s = input()
#     if s == "Y" or s == "y" or s == "ДА" or s == "Да" or s == "дА" or s == "да":
#         choice(answers)
#     else:
#         print("Возвращайся если возникнут вопросы")
# ___________________________________Генератор безопасных паролей____________________________________________________
# from random import *
# digits = "0123456789"
# lowercase_letters = "qwertyuiopasdfghjklzxcvbnm"
# uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
# punctuation = "!#@$%^&*-_+=?"
# neodn = "iI1L0oO"
# chars = ""
# otvetda = "y, Y, Да, да, ДА, дА"
# otvetnet = "n, N, Нет, нЕт, неТ, НеТ, нЕТ, НЕт"
# colpass = int(input('Введите количество паролей:  '))
# lenpass = int(input('Введите длину пароля: '))
# digitsOn = input('Включать ли в генерацию пароля цифры? (Y/N): ')
# upletters = input(
#     'Включать ли в генерацию пароля прописные буквы(QWERTY)? (Y/N): ')
# lowletters = input(
#     'Включать ли в генерацию пароля строчные буквы(qwerty)? (Y/N): ')
# punctua = input(
#     'Включать ли в генерацию пароля символы пунктуации(!#@$%^&*-_+=?)? (Y/N): ')
# neod = ''
# if upletters in otvetda or lowletters in otvetda:
#     neod = input(
#         'Исключить ли из генерацию пароля неоднозначные символы (iI1L0oO)? (Y/N): ')
# if digitsOn in otvetda:
#     chars += digits
# if upletters in otvetda:
#     chars += uppercase_letters
# if lowletters in otvetda:
#     chars += lowercase_letters
# if punctua in otvetda:
#     chars += punctuation
# if neod in otvetda:

#     for c in neodn:
#         chars = chars.replace(c, '')


# def generate_password(lenpass, chars):
#     password = ''
#     for _ in range(lenpass):
#         password += choice(chars)  # [random.randint(1, len(chars))]
#     return password


# for _ in range(colpass):
#     print(generate_password(lenpass, chars))
# ___________________________________________Шифр Цезаря_____________________________________________________
# s = input().split(' ')
# s1 = ""

# for i in range(len(s)):
#     count = 0
#     count1 = 0
#     if len(s[i]) != 0:
#         count1 = int(count1 + len(s[i]))
#         s1 = s1+' '
#     for j in range(len(s[i])):
#         if s[i][j].isalpha() == True:
#             count += 1
#     for letter in s[i]:
#         if letter.isupper():
#             s12 = chr(
#                 (ord(letter) - ord("A") + count) % 26 + ord("A"))
#         elif letter.islower():
#             s12 = chr(
#                 (ord(letter) - ord("a") + count) % 26 + ord("a"))
#         else:
#             s12 = letter
#         s1 += s12
# s1 = s1.strip()
# print(s1)
# ____________________________________________________Калькулятор систем счисления___________________________________________
# for i in range(9, 17):

#     if int('88', i) == int('32', i) + int('22', i) + int('16', i) + int('17', i):

#         print(i)
# _________________________________________________________________________________________________________________
# a = int(input())
# print(bin(a)[2:])
# print(oct(a)[2:])
# print(hex(a)[2:].upper())
# _________________________________________________________________________________________________________________
