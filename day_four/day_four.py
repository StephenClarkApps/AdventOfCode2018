# Day Four
# Advent of Code 2018

import re
from dateutil.parser import parse
import numpy as np

track_mins = {}
records = []
guard_ids_by_mins_asleep = {}

# Somehow have to track number of occurances of sleeping in a given minute
# indexed by guard ??
# {Guard : (min, count)}

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
        guard_id = 0
        falls_asleep = False
        wakes = False
        if (words[2] == "Guard"):
            shift_start = True
            guard_id = int(words[3][1:])
        elif (words[2] == "wakes"):
            wakes = True
            guard_id = 0
        elif (words[2] == "falls"):
            falls_asleep = True
            guard_id = 0
        return Record(date, year, month, day, hour, mins, shift_start, guard_id, falls_asleep, wakes)

# Read in data from the input file and append records to an array of records
for line in open('input.txt'):
    record = (ParseLine(line))
    records.append(record)

# sort the records by date
records = sorted(records, key=lambda record: record.date)   # sort by date

#some how work out the guard with the most mins time used
current_guard_id = 0
last_fall_asleep_minute = 0
last_wake_up_minute = 0
for record in records:
    #current_guard_id = record.guard_id
    if record.shift_start == True:
        current_guard_id = record.guard_id
    if record.falls_asleep:
        last_fall_asleep_minute = int(record.mins)
    if record.wakes:
        last_wake_up_minute = int(record.mins)
        key = current_guard_id
        for thw in range(last_fall_asleep_minute, last_wake_up_minute, 1):
            if current_guard_id in track_mins:
                track_mins[current_guard_id].append(thw)
            else:
                track_mins[current_guard_id] = [thw]

        guard_ids_by_mins_asleep[key] = guard_ids_by_mins_asleep.get(key , 0)  + (last_wake_up_minute - last_fall_asleep_minute)

previous_max_mins = 0
linked_guard = 0
for key, value in guard_ids_by_mins_asleep.items():
    if value > previous_max_mins:
        previous_max_mins = value
        linked_guard = key

print("Linked Guard: ")
print (linked_guard)
print ("")

from itertools import groupby as g
def most_common_oneliner(L):
    return max(g(sorted(L)), key=lambda(x, v):(len(list(v)),-L.index(x)))[0]

# PART II - "Of all guards, which guard is most frequently asleep on the same minute?"
# To know this we need to know frequency of sleeping, by minute, by guard
# but we already know that the minutes will be in the range 1..59 which are within that one hour window
# so we just need to record the frequency, get the max using a method like max for each guard, and find the
# highest frquency and the associated guard.
for element in track_mins.items():
    # print (element)
    x, y = element
    print ("Guard: " + str(x))
    print ("Most common minute: " + str(most_common_oneliner(y)))
    count = 0
    for x in y:
        if x == (most_common_oneliner(y)):
            count += 1
    print ("The number of times the guard was asleep at this min is: " + str(count))
    print ("")
