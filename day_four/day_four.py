# Day Four
# Advent of Code 2018

import re
from dateutil.parser import parse

# maybe a data structure with the line, the day, month, year, the time,
# if its a Fall/Wake or on-shift message

for line in open('input.txt'):
    words = line.split()
    date = words[0][1:]
    parsed_date = parse(date)
    year = parsed_date.year
    month = parsed_date.month
    day = parsed_date.day
    
    print (words[1][:-1])
    print (words[2]) # could be falls, wakes, Guard

# need to read in the file
# parse it and then process

# Since the entries are not in order we need to *sort* them 1st
# We might start by organising them by date, then by time

# Want to work out which guard is asleep the most and on which times
# if we have a hash table indexed by guard id inside of which is a
# hash table of a given date indexes against an array or set of minutes during
# the midnight hour when they were asleep
# [ guard_id, [ date, [int] ] ]
