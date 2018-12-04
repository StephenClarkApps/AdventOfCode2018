# Day Four
# Advent of Code 2018

import re
from dateutil.parser import parse
import numpy as np

records = []

class Record:
    def __init__(self, date, year, month, day, hour, mins, shift_start, guard_id, falls_asleep, wakes):
        self.date = date
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.mins = mins
        self.shift_start = shift_start
        self.guard_id = guard_id
        self.falls_asleep = falls_asleep
        self.wakes = wakes

"""Function to parse a line from the input file and return a Record"""
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
        return Record(date, year, month, day, hour, mins, shift_start, guard_id, falls_asleep, wakes)

# Read in data from the input file and append records to an array of records
for line in open('input.txt'):
    record = (ParseLine(line))
    records.append(record)
    # instead of just

records = sorted(records, key=lambda record: record.date)   # sort by date

for record in records:
    print (record.date)
