# Leetcode question number 217: contains duplicate
def return_true(numbers: list):
    if numbers == []:
        return f"You cannot use an empty list"
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
        if count[num] > 1:
            return True
    return False
    

result = return_true([1, 2, 3, 1])
print(result)
result = return_true([1, 2, 3, 4])
print(result)


def check(nums: list):
    if nums == []:
        return "cannot use an empty list"
    new = set()
    for num in nums:
        if num in new:
            return True
        else:
            new.add(num)
    return False

another = [5, 5, 6, 7]
print()
print(check(another))



# Leetcode question number 242: Valid anagram
def check(a: str, b: str):
    if a == "" or b == "":
        return "please provide actual words"
    if len(a) != len(b):
        return False
        
    result_a = {}
    result_b = {}
    for char in a:
        result_a[char] = result_a.get(char, 0) + 1
    for char in b:
        result_b[char] = result_b.get(char, 0) +  1
    if result_a == result_b:
        return True
    return False

a = "abb"
b = "aab"
result = check(a, b)
print(result)