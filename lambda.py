#    lambda arguments: expression
# expression is return value
# name of function (add5) = lambda (x is the argument)
add5 = lambda x: x + 5
# print(add5(7))

square = lambda x: x * x
# print(square(8))

get_tens = lambda p: int(p / 10) % 10
# print(get_tens(749)) # 4
# print(get_tens(836.21))  # 3


# SORTING A LIST OF TUPLES USING LAMBDA

list_1 = [("eggs", 5.35), ("honey", 9.70), ("carrots", 1.10), ("peaches", 2.45)]
# sort by item x[0] , sort by cost x[1]
list_1.sort(key=lambda x: x[0])
print(list_1)
# [('carrots', 1.1), ('eggs', 5.35), ('honey', 9.7), ('peaches', 2.45)]

# SORTING A LSOT OF DICITONARIES USING LAMBDA
import pprint as pp

list1 = [
    {"make": "Ford", "model": "Focus", "year": 2013},
    {"make": "Tesla", "model": "X", "year": 1999},
    {"make": "Mercedes", "model": "C350E", "year": 2008},
]
list2 = sorted(list1, key=lambda x: x["year"])
pp.pprint(list2)


# FILTERING A LIST OF INTERGERS USING LAMBDA

list1 = [1, 2, 3, 4, 5, 6]
# list 2 is a new list that is filterd (key, from list)
list2 = list(filter(lambda x: x % 2 == 0, list1))
print(list2)
# [2,4,6]


odds = lambda x: x % 2 == 1
list1 = [1, 2, 3, 4, 5, 6]
list2 = list(filter(odds, list1))
print(list2)

# LAMBDA FUNCTION ON A LIST USING MAP

list1 = [1, 2, 3, 4, 5, 6]
list2 = list(map(lambda x: x ** 2, list1))
print(list2)


# LAMDA CONDITIONALS
# lamnbda args: a if bolean_expression else b
starts_with_J = lambda x: True if x.startswith("J") else False
print(starts_with_J("Joey"))

wordb4 = lambda s, w: s.split()[s.split().index(w) - 1] if w in s else None
sentence = "Four score and seven years ago"
print(wordb4(sentence, "seven"))

# LAMBDAS ON DATETIME OBJECTS
import datetime

now = datetime.datetime.now()
print(now)
year = lambda x: x.year
print(year(now))


def do_something(f, val):
    return f(val)


func = lambda x: x ** 3
print(func(16))
print(do_something(func, 5))


# EXTREME LAMBDAS
isnum = lambda q: q.replace(".", "", 1).isdigit()
print(isnum("25983"))
print(isnum("3.1415"))
print(isnum("T57"))
print(isnum("-16"))

is_num = lambda r: isnum(r[1:]) if r[0] == "-" else isnum(r)
print(is_num("-16.4"))

tonum = lambda s: float(s) if is_num(s) else -1
print(tonum("30y"))
print(tonum("-21.67"), type(tonum("-21.67")))
