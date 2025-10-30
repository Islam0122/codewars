"""01 Multiplication table for number"""
# def multi_table(number):
#     res = ""
#     for i in range(1,11):
#        res += (f"{i} * {number} = {i * number}\n")
#     return res.strip()
#
# number = int(5)
# print(multi_table(number))

"""02 Quarter of the year"""
# def quarter_of(month):
#     if 1 <= month <= 3:
#         return 1
#     elif 4 <= month <= 6:
#         return 2
#     elif 7 <= month <= 9:
#         return 3
#     elif 10 <= month <= 12:
#         return 4
#     else:
#         return "Invalid month"

"""03 Is it even?"""
# def is_even(n):
#    return n % 2 == 0

"""04 Switch it Up! """
# def switch_it_up(number):
#     db = {
#         0:"Zero",
#         1:"One",
#         2:"Two",
#         3:"Three",
#         4:"Four",
#         5:"Five",
#         6:"Six",
#         7:"Seven",
#         8:"Eight",
#         9:"Nine",
#         10:"Ten",
#     }
#     return db[number]

"""05 Beginner Series #2 Clock"""
# def past(h, m, s):
#     return (h * 3600 + m * 60 + s) * 1000

"""06 Grasshopper - Personalized Message"""
# def greet(name, owner):
#     if name == owner:
#         return "Hello " + "boss"
#     else:
#         return "Hello " + "guest"

"""07 The Feast of Many Beasts"""
# def feast(beast, dish):
#     return beast[0] == dish[0] and beast[-1] == dish[-1]

"""08 Grasshopper - Grade book"""
# def get_grade(s1, s2, s3):
#     avg = (s1 + s2 + s3) / 3
#
#     if avg >= 90:
#         return 'A'
#     elif avg >= 80:
#         return 'B'
#     elif avg >= 70:
#         return 'C'
#     elif avg >= 60:
#         return 'D'
#     else:
#         return 'F'

"""09 What is between?"""
# def between(a, b):
#     return list(range(a, b + 1))

"""10 Area or Perimeter"""
# def area_or_perimeter(l, w):
#     if l == w:
#         return l * w          # квадрат → площадь
#     else:
#         return 2 * (l + w)    # прямоугольник → периметр

