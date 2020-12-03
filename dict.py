from collections import Counter

animals = {}
animals["cat"] = 1 
animals["dog"] = 5 

print(animals)
s = "leetcode"
count = Counter(s)

print(count)
print(count['e'])

nums = [1,24,54,5,6,7,3,3,7,4,47,5,75]
numbrs = Counter(nums)
print(numbrs)