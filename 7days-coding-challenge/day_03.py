"""
Remove the minimum --> 7kyu
"""
# def remove_smallest(numbers):
#     if not numbers:
#         return []
#     result = numbers.copy()
#     result.remove(min(numbers))
#     return result
#
# print(remove_smallest([1,2,3,4,5]))


"""
Rock Paper Scissors! ---> 8kyu
"""
# def rps(p1, p2):
#     if p1 == p2:
#         return "Draw!"
#
#     rules = {
#         "rock": "scissors",
#         "scissors": "paper",
#         "paper": "rock"
#     }
#
#     if rules[p1] == p2:
#         return "Player 1 won!"
#     else:
#         return "Player 2 won!"
