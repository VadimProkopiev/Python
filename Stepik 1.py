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
# put your python code here
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
e = 0
count = 0
for a in range(1, 33):
    for b in range(1, 33):
        for c in range(1, 33):
            for d in range(1, 33):
                if a**3+b**3 == c**3+d**3 and a != b and a != c and a != d and b != c and b != d and c != d:
                    print(a**3+b**3)
                count += 1

print(count)
