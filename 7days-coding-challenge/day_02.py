"""
Fake Binary --> 8kyu
"""
# def fake_bin(x):
#     return ''.join('0' if int(ch) < 5 else '1' for ch in x)
#
# print(fake_bin("01011110001100111"))

"""
Beginner - Lost Without a Map --> 8kyu
"""
# def maps(a:list):
#     result = []
#     for x in a:
#         result.append(x+x)
#     return result
# print(maps([1, 2, 3]))

"""
Sort the odd --> 6kyu
"""
# def sort_array(source_array):
#     odds = sorted([x for x in source_array if x % 2 != 0])
#     result = []
#     odd_index = 0
#     for x in source_array:
#         if x % 2 == 0:
#             result.append(x)
#         else:
#             result.append(odds[odd_index])
#             odd_index += 1
#     return result
#
# print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) #[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""
Opposite number --> 8kyu
"""
# def opposite(n):
#   res = ""
#   if n < 1:
#       for i in str(n):
#           if i != "-":
#               res += i
#   else:
#       res += "-"
#       for i in str(n):
#           res += i
#   return float(res)

"""
Convert a string to an array --> 8kyu
"""
# def string_to_array(s):
#     if s == "":
#         return [""]
#     return s.split()

"""
Odd or Even? --> 8kyu
"""
# def odd_or_even(arr:list):
#     if sum(arr) % 2 == 0:
#         return "even"
#     return "odd"
# print(odd_or_even([0, 1, 2]))

"""
Convert boolean values to strings 'Yes' or 'No'. --> 8kyu
"""
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"
#
# print(bool_to_word(True))

"""
Count by X --> 8kyu
"""
# def count_by(x, n):
#     res = []
#     while len(res) < n:
#         if len(res) == 0:
#             res.append(x)
#         else:
#             res.append(res[-1] + x)
#     return res
# print(count_by(2, 5))
"""
Sum Arrays --> 8kyu
"""
# def sum_array(a):
#     return sum(a) if a else 0
"""
Create Phone Number --> 6kyu
"""
# def create_phone_number(n):
#     n1 = n[0:3]
#     n1_r = ""
#     for i in n1:
#         n1_r += str(i)
#     n2 = n[3:6]
#     n2_r = ""
#     for i in n2:
#             n2_r += str(i)
#     n3 = n[6:]
#     n3_r = ""
#     for i in n3:
#         n3_r += str(i)
#     return f"({n1_r}) {n2_r}-{n3_r}"

"""
Descending Order --> 7kyu
"""
# def descending_order(num):
#     res = ""
#     my_list = []
#     for i in str(num):
#         my_list.append(int(i))
#     for i in sorted(my_list,reverse=True):
#         res += str(i)
#     return int(res)
#
# print(descending_order(42145))

"""
Highest and Lowest --> 7kyu
"""
# def high_and_low(numbers:str):
#     res =  []
#     for i in numbers.split(" "):
#         res.append(int(i))
#     return str( max(res)) + " " + str(min(res))
# print(high_and_low("1 2 3 4 5 6 7 8 9"))
"""
Is he gonna survive? --> 8kyu
"""
# def hero(bullets: int, dragons: int) -> bool:
#     return bullets >= dragons * 2

"""
Function 1 - hello world --> 8kyu
"""
# def greet() -> str:
#     return "".join([chr(c) for c in [104,101,108,108,111,32,119,111,114,108,100,33]])
