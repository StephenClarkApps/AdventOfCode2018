# Day Four
# Advent of Code 2018

import re
from dateutil.parser import parse


class Record:
    def __init__(self, year, month, day, hour, mins, shift_start, guard_id, falls_asleep, wakes):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.mins = mins
        self.shift_start = shift_start
        self.guard_id = guard_id
        self.falls_asleep = falls_asleep
        self.wakes = wakes


def ParseLine(line):
        words = line.split()
        date = words[0][1:] + " " + words[1][:-1]
        parsed_date = parse(date)
        year = parsed_date.year
        month = parsed_date.month
        day = parsed_date.day
        hour = parsed_date.hour
        mins = parsed_date.minute

        #print (year, month, day, hour, mins)
        shift_start = False
        guard_id = ""
        falls_asleep = False
        wakes = False

        if (words[2] == "Guard"):
            shift_start = True
            guard_id = words[3]
        elif (words[2] == "wakes"):
            wakes = True
        elif (words[2] == "falls"):
            falls_asleep = True
        return Record(year, month, day, hour, mins, shift_start, guard_id, falls_asleep, wakes)

# maybe a data structure with the line, the day, month, year, the time,
# if its a Fall/Wake or on-shift message

for line in open('input.txt'):
    record = (ParseLine(line))
    print record.year

# need to read in the file
# parse it and then process

# Since the entries are not in order we need to *sort* them 1st
# We might start by organising them by date, then by time

# Want to work out which guard is asleep the most and on which times
# if we have a hash table indexed by guard id inside of which is a
# hash table of a given date indexes against an array or set of minutes during
# the midnight hour when they were asleep
# [ guard_id, [ date, [int] ] ]
