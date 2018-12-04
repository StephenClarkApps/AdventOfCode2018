from collections import Counter

input = open('input.txt').readlines()
two_counter = 0
three_counter = 0

for row in input:
    c = Counter(row)
    if 2 in c.values():
        two_counter += 1
        if 3 in c.values():
            three_counter += 1

print (two_counter * three_counter)
