# for loops

for i in range(0, 10): # range(from_inclusive, to_exclusive, [step_size (int)]
    print i
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
for i in range(0, 10, 5):
    print i
    # 0, 5

# they are commonly used to sweep through each element of an array
items = ['a', 2, 0.2, 10]
count = 0
for i in range(0, len(items), 1):
    count += 1
    print items[i], count

# filter patern
def isEven(integer):
    if integer % 2 == 0:
        return True
    else:
        return False
# this method produces a _reduction_ of the original list
def extractEvens(items):
    evens = []
    for i in range(0, len(items)):
        if isEven(items[i]):
            evens = evens + [items[i]]
    return evens
# >>> extractEvens([1,2,3,4,5])
# [2, 4]

# the map pattern
def fun(item):
    return item**2
def map(fun, items):
    results = []
    for i in range(0, len(items)):
        transformed = fun(items[i])
        results = results + [transformed]
    return results

# calling _list_ items
listy = [1,2,3,4,5]
listy[1:]
#2,3,4,5
listy[:1]
#1
