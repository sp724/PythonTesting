import os
import time
import heapq

# Recipe 0.0
print("Recipe 0.0: Heelo World.")

# Recipe 0.1
print("Recipe 0.1:",time.asctime())
print("Recipe 0.1:",os.curdir)

# Recipe 1.0
data = ['abc', '123', 'xyz', '456', '789']
aa, bb, cc, *dd = data
print("Recipe 1.0:", aa, bb, cc, dd)

# Recipe 1.1
data = ('ACME', 50, 123.45, (12, 8, 2018))
name, *_, (*_, year) = data
print("Recipe 1.1:", year)

# Recipe 1.2
data = [1, 10, 7, 4, 59]
head, *tail = data
print("Recipe 1.2:", tail)


def sum(items):
    myhead, *mytail = items
    return myhead + sum(mytail) if mytail else myhead


print("Recipe 1.2:", sum(data))

# Recipe 1.3 Keeping the Last N Items
from collections import deque


q = deque(maxlen=5)
q.append(1)
q.append(2)
q.append(3)
print("Recipe 1.3:", q)
q.pop()
print("Recipe 1.3:", q)

# Recipe 1.4 Finding the largest/smallest N items
nums = [444, 1, 4, 6, 8, 11, 15, 2, 67, 99]
print("Recipe 1.4:", heapq.nlargest(2, nums))
print("Recipe 1.4:", heapq.nsmallest(4, nums))
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 33, 'price': 31.71},
    {'name': 'YHOO', 'shares': 433, 'price': 1.71}
]

expensive = heapq.nlargest(2, portfolio, key=lambda s: s['price'])
print("Recipe 1.4:", expensive)


# Recipe Classes
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def sayname(self):
        print("Recipe 1.4:", self.first, self.last)


p = Person("Suresh", "Patel")
p.sayname()

# Recipe 1.5 Implementing a Priority Queue
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '"Recipe 1.5: Item({!r})'.format(self.name)


q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),2)
print("Recipe 1.5:", q.pop())


# Recipe 1.6 Mapping Keys to Multiple Value in Dictionary
from collections import defaultdict


d = defaultdict(list)
d['a'].append("first")
d['b'].append("second")
d['c'].append("third")


print("Recipe 1.6:", d['b'])

# Recipe 1.7 Keeping Dictionaries in Order
import json
from collections import OrderedDict


d = OrderedDict()
d['one'] = 1
d['two'] = 2
d['three'] = 3
d['four'] = 4

ee = defaultdict(list)
ee['a'].append("first")
ee['b'].append("second")
ee['c'].append("third")

d['five'] = ee

for k in d:
    print("Recipe 1.7:", d[k])

print("Recipe 1.7:", json.dumps(d))

# Recipe 1.8 Calculating with Dictonaries

prices = {
    'fb': 12.34,
    'aapl': 23.35,
    'rbc': 44.45,
    'ibm': 5.55
}


print("Recipe 1.8:", min(zip(prices.values(),prices.keys())))
print("Recipe 1.8:", max(zip(prices.values(),prices.keys())))


# Recipe 1.9 Calculating with Dictonaries

a = {
    'x':123,
    'y':456,
    'zz':789
}

b = {
    'w':1,
    'y':4,
    'zz':789
}

# find keys in both
print("Recipe 1.9:",a.keys() & b.keys())

# find keys in a not in b
print("Recipe 1.9:",a.keys() - b.keys())

# find keys and values in both
x = a.items() & b.items()

print("Recipe 1.9:",len(x))


# Recipe 1.10 Removing duplicates from a sequence while maintaining order

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10, 3]
print("Recipe 1.10:",list(dedupe(a)))

# Recipe 1.11 Slices
mylist = [2**x for x in range(5)]
shares = slice(1,2)
print("Recipe 1.11: Mylist before deletion:", mylist)
del mylist[shares]
print("Recipe 1.11: MyList after deletion:", mylist)

# Recipe 1.12 Determining the most frequent occurences
words = ['look','into','my','eyes','and','look','into']
from collections import Counter
words.append('look')
word_count = Counter(words)
top_three_words = word_count.most_common(3)
print("Recipe 1.12:",top_three_words)

# Recipe 1.13 Sorting a list of dictionary by a common key
print("Recipe 1.13 Testing Testing")