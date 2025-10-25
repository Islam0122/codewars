"""
Who likes it? --> 6kyu
"""
# def likes(names):
#     if len(names) == 1:
#         return  names[0] + " likes this"
#     elif len(names) == 2:
#         return names[0]+ " and " + names[1] + " like this"
#     elif len(names) == 3:
#         return names[0]+ ", " + names[1]+ " and " + names[2] + " like this"
#     elif len(names) >= 4:
#         return names[0] + ", " + names[1]+ " and "+str(len(names)-2) +  " others like this"
#     else :
#         return 'no one likes this'
#
# print(likes(["A", "B"]))

"""
Sentence Smash --> 8kyu
"""
# def smash(words):
#     result = ""
#     for word in words:
#         result += " " + word
#     return result.strip()
#
# print(smash(["hello", "world"]))

"""
Convert number to reversed array of digits --> 8kyu
"""
# def digitize(n):
#     result = []
#     if n == 0:
#         result.append(0)
#     for digit in str(n):
#         result.append(int(digit))
#     return result[::-1]
# print(digitize(63277342))

"""
Recover a secret string from random triplets --> 4kyu
"""
# from collections import defaultdict, deque
#
# def recover_secret(triplets):
#     graph = defaultdict(set)
#     in_degree = defaultdict(int)
#     nodes = set()
#
#     # 1. Build the graph
#     for triplet in triplets:
#         a, b, c = triplet
#         nodes.update(triplet)
#
#         if b not in graph[a]:
#             graph[a].add(b)
#             in_degree[b] += 1
#         if c not in graph[b]:
#             graph[b].add(c)
#             in_degree[c] += 1
#
#         # Ensure all characters are in the in-degree dict
#         if a not in in_degree:
#             in_degree[a] = 0
#         if b not in in_degree:
#             in_degree[b] = 0
#         if c not in in_degree:
#             in_degree[c] = 0
#
#     # 2. Topological sort (Kahn’s algorithm)
#     queue = deque([node for node in nodes if in_degree[node] == 0])
#     result = []
#
#     while queue:
#         node = queue.popleft()
#         result.append(node)
#         for neighbor in graph[node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#
#     return ''.join(result)

"""
Even or Odd --> 8kyu
"""
# def even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

"""
Square Every Digit --> 7kyu
"""
# def square_digits(num):
#     return int(''.join(str(int(d)**2) for d in str(num)))