# Nice pythonic solution
# Source:
# https://old.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/eaujws7/?context=2

input = open('input.txt').read()

changes = [int(n.strip()) for n in input.split() if n.strip()]

print(sum(changes))

from itertools import accumulate, cycle

# Part 2
seen = {0}
print(next(f for f in accumulate(cycle(changes)) if f in seen or seen.add(f)))
