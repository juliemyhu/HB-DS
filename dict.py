from collections import Counter


def animal_counter():

    animals = {}
    animals["cat"] = 1
    animals["dog"] = 5

    print(animals)


s = "leetcode"
count = Counter(s)

print(count)
print(count['e'])

nums = [1, 24, 54, 5, 6, 7, 3, 3, 7, 4, 47, 5, 75]
numbers = Counter(nums)
print(numbers)


# counting numner of times each word comes up in a list of words
def wordcount(word_list):

    d = {}

    for word in word_list:
        d[word] = d.get(word, 0) + 1

    return d


print(wordcount(["hello", "hello", "name", "hello", "name"]))

stations = {}
stations["Paradise"] = [23]

stations["Paradise"].extend([24])

if "Paradise" in stations.keys():
    print("yes")
print("stations:", stations)


# .get("value", "defualt_value")