​
def max_sequence(arr):
    max_sum = 0
    current_sum = 0
​
    for num in arr:
        current_sum += num
​
        if current_sum < 0:
            current_sum = 0
​
        max_sum = max(max_sum, current_sum)
​
    return max_sum
​