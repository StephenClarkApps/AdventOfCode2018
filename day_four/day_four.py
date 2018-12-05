# Day Four
# Advent of Code 2018

import re
from dateutil.parser import parse
import numpy as np

track_mins = []
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
        #print (str(current_guard_id) + " Has started a shift. At: " + str(record.date))
        #print (current_guard_id)
    if record.falls_asleep:
        #print ("He/she has fallen asleep @"  + str(record.date))
        last_fall_asleep_minute = int(record.mins)
    if record.wakes:
        #print ("He/she has woken again @"  + str(record.date))
        last_wake_up_minute = int(record.mins)
        key = current_guard_id
        if current_guard_id == 499: # hard coded the guard id from the previous answer :/
            for thw in range(last_fall_asleep_minute, last_wake_up_minute, 1):
                track_mins.append(thw)

        guard_ids_by_mins_asleep[key] = guard_ids_by_mins_asleep.get(key , 0)  + (last_wake_up_minute - last_fall_asleep_minute)
        #print("They've been asleep for: " + str(last_wake_up_minute - last_fall_asleep_minute) + "mins")

previous_max_mins = 0
linked_guard = 0
for key, value in guard_ids_by_mins_asleep.items():
    # print ("Guard: ")
    # print(key)
    # print ("Mins: ")
    # print(value)
    if value > previous_max_mins:
        previous_max_mins = value
        linked_guard = key
print("Linked Guard: ")
print (linked_guard)
# print ("AT")
# print (previous_max_mins)
print("most slept at minute: ")
print(max(track_mins,key=track_mins.count))
#print (track_mins)
