​
def disemvowel(string):
    vowels = "aeiouAEIOU"
    result = ""
​
    for char in string:
        if char not in vowels:
            result += char
​
    return result
​