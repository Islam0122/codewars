"""
 Partial Word Searching --> 7kyu
"""
# def word_search(query, seq):
#     result = []
#     for word in seq:
#         if query.lower() in word.lower():
#             result.append(word)
#     return result or ["None"]
#
# print(word_search("ab", ["za", "ab", "abc", "zab", "zbc"]))

"""
Function 2 - squaring an argument --> 8kyu
"""
# def square(n):
#     return n ** 2
# print(square(5))

"""
Grasshopper - Messi goals function --> kyu
"""
# def goals(laLiga, copaDelRey, championsLeague):
#     return laLiga + copaDelRey + championsLeague

""" 
Sum of odd numbers --> 7kyu
"""
# def row_sum_odd_numbers(n):
#     num = 1
#     result = []
#     for i in range(1, n + 1):
#         row = []
#         for j in range(i):
#             row.append(num)
#             num += 2
#         result.append(row)
#     return sum(result[n-1])
#
# print(row_sum_odd_numbers(2))

"""
Duplicate Arguments --> 6kyu
 """
# def solution(*args):
#     return len(args) != len(set(args))
#
# print(solution(1, 2, 3,))

"""
Sum of array singles --> 7kyu
"""
# def repeats(arr):
#     unique = []
#     for i in arr:
#         if arr.count(i) == 1:
#             unique.append(i)
#     return sum(unique)
#
# print(repeats([4,5,7,5,4,8]))


""" 
altERnaTIng cAsE <=> ALTerNAtiNG CaSe -->  8kyu
 """
# def to_alternating_case(string: str) -> str:
#     res = list(map(lambda x: x.upper() if x.islower() else x.lower(), string))
#     return "".join(res)


"""
Write Number in Expanded Form --> 6kyu
12 --> "10 + 2"

"""
# def expanded_form(num: int) -> str:
#     num_str = str(num)
#     length = len(num_str)
#     parts = [
#         str(int(digit) * 10 ** (length - i - 1))
#         for i, digit in enumerate(num_str)
#         if digit != "0"
#     ]
#     return " + ".join(parts)
