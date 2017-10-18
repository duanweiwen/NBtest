# -*- coding: utf-8 -*-

# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# print('''(n)
# f
# s1
# s2
# s3
# s4''')

# 04.2
# s1 = 72
# s2 = 85
# s3 = (s2-s1)/s1*100
# s4 = '百分点：%.1f%%' % s3
# print (s4)

# 04.3
# L = [
# ['Apple', 'Google', 'Microsoft'],
# ['Java', 'Python', 'Ruby', 'PHP'],
# ['Adam', 'Bart', 'Lisa']
# ]
# a = L[0][0]
# print (a)

# 04.4
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# x = float(input('体重： '))
# y = float(input('身高： '))
# bmi = x/y**2
# print(bmi)
# if bmi < 18.5:
#     print('过轻')
# elif bmi <= 25:
#     print('正常')
# elif bmi <= 28:
#     print('过重')
# elif bmi <= 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

# 04.5
# L = ['Bart', 'Lisa', 'Adam']
# for L in L:
#     print('hello', L )

# a = 1
# while a > 0:
#     a = a + 1
#     print(a)

# 05.2
# ax^2+bx+c=0
# a等于0时不是一元二次方程，与题意不相符
# import math
#
# def quadratic(a, b, c):
#     if (a == 0):
#         print('参数错误，请重新输入！')
#
# # a不等于0时是一元二次方程，通过判断delta与0的大小，确定方程是否有实根
#     else:
#         delta = b ** 2 - 4 * a * c
#     # delta大于0时，方程有两个不等的实根
#         if delta > 0:
#             x1 = (-b + math.sqrt(delta)) / (2 * a)
#             x2 = (-b - math.sqrt(delta)) / (2 * a)
#             print('此方程有两个不等实根：x1=%s x2=%s' % (x1, x2))
#     # delta等于0时，方程有两个相等的实根
#         elif delta == 0:
#             x1 = -b / (2 * a)
#             x2 = -b / (2 * a)
#             print('此方程有两个相等实根：x1=x2=%s' % (x1, x2))
#     # delta小于于0时，方程无实根
#         else:
#             print('此方程无实根')
# print(quadratic(1,1,0))

# 05.3
# 一脸蒙蔽

# 05.4
# def move(n, a, buffer, c):
#     if(n == 1):
#         print(a,"->",c)
#         return
#     move(n-1, a, c, buffer)
#     move(1, a, buffer, c)
#     move(n-1, buffer, a, c)
# move(3, "a", "b", "c")

# 06.0
# 06.5
# 这个部分有难度（花的时间要多一点）

# 08.2
# 09.2
# 提交
