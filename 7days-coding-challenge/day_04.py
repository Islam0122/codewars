"""
Calculate BMI --> 8kyu
"""
# def bmi(weight, height):
#     value = weight / (height ** 2)
#     if value <= 18.5:
#         return "Underweight"
#     elif value <= 25.0:
#         return "Normal"
#     elif value <= 30.0:
#         return "Overweight"
#     else:
#         return "Obese"

"""
Beginner - Reduce but Grow --> 8kyu
"""
# def grow(arr):
#     res = 0
#     for i in arr:
#         res = i * res
#     return res

"""
Square(n) Sum --> 8kyu
"""
# def square_sum(numbers):
#     res = 0
#     for num in numbers:
#         res += num**2
#     return res
#
# print(square_sum([1, 2, 2]))

"""
Break camelCase --> 6kyu
"""
# def solution(s):
#     result = ""
#     for char in s:
#         if char.isupper():
#             result += " " + char
#         else:
#             result += char
#     return result
#
# print(solution("cmmalCammelRose"))

"""
Is this a triangle? --> 7kyu
"""
# def is_triangle(a, b, c):
#     return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

"""
Directions Reduction --> 5kyu
"""
# def dir_reduc(arr):
#     opposite = {
#         "NORTH": "SOUTH",
#         "SOUTH": "NORTH",
#         "EAST": "WEST",
#         "WEST": "EAST"
#     }
#
#     stack = []
#
#     for direction in arr:
#         if stack and stack[-1] == opposite[direction]:
#             stack.pop()
#         else:
#             stack.append(direction)
#
#     return stack