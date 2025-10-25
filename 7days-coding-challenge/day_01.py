"""
ever sed Strings --> 8kyu
"""
# def solution(string):
#     return string[::-1]
#
# print(solution("word"))    #'word'   =>  'drow'

""" 
Opposites Attract --> 8kyu
"""
# def lovefunc( flower1, flower2 ):
#     if (flower1 % 2 == 1 and flower2 % 2 == 0
#             or flower1 % 2 == 0 and flower2 % 2 == 1):
#         return True
#     return False
#
# print(lovefunc(1, 4))

"""
Friend or Foe? --> 7kyu
"""
# def friend(x:list):
#     my_friend = []
#     for i in x:
#         if len(i) == 4:
#             my_friend.append(i)
#     return my_friend
#
# print(friend(["Ryan", "Kieran", "Jason", "Yous"]))

"""
Sum of positive --> 8kyu
"""
# def positive_sum(arr):
#     n = 0
#     for num in arr:
#         if num > 0:
#             n += num
#     return n
# print(positive_sum([-1, 2, 3, -4, 5]))

"""
Counting Change Combinations --> 4kyu
"""
# def count_change(money, coins):
#     dp = [0] * (money + 1)
#     dp[0] = 1
#     for coin in coins:
#         for amount in range(coin, money + 1):
#             dp[amount] += dp[amount - coin]
#     return dp[money]
#
# print(count_change(10, [5,2,3]))  # 4

"""
Roman Numerals Helper --> 4kyu
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
"""
# romanNumerals = {
#     "M": 1000,
#     "CM": 900,
#     "D": 500,
#     "CD": 400,
#     "C": 100,
#     "XC": 90,
#     "L": 50,
#     "XL": 40,
#     "X": 10,
#     "IX": 9,
#     "V": 5,
#     "IV": 4,
#     "I": 1,
# }
#
# class RomanNumerals:
#     @staticmethod
#     def to_roman(val: int) -> str:
#         result = ""
#         for roman, arabic in romanNumerals.items():
#             while val >= arabic:
#                 result += roman
#                 val -= arabic
#         return result
#
#     @staticmethod
#     def from_roman(roman_str: str) -> int:
#         i = 0
#         result = 0
#         roman_keys = list(romanNumerals.keys())
#         while i < len(roman_str):
#             if i + 1 < len(roman_str) and roman_str[i:i+2] in romanNumerals:
#                 result += romanNumerals[roman_str[i:i+2]]
#                 i += 2
#             else:
#                 result += romanNumerals[roman_str[i]]
#                 i += 1
#         return result

"""
8kyu --> Sum Mixed Array
"""
# def sum_mix(arr):
#     result = 0
#     for i in arr:
#         result += int(i)
#     return result

