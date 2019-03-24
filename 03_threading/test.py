import random

sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



result = []

for i in range(10000000):
    result.append(random.choice(sample))

for i in sample:
    print(result.count(i))