# Advent of Code 2018
# Day 2

# I've gone back and fixed and corrected this code for clarity

count_two = 0
count_three = 0
box_ids = []

for line in open('input.txt'):
    striped_line = line.strip()
    box_ids.append(striped_line)
    # dictionary of character by count
    count = {}
    for character in striped_line:
        if character not in count:
            count[character] = 0
        # add one to the count for the particular character in the line
        count[character] += 1
    # declare two Bools to track for instances of two given characters a line
    # or three given charcters a line
    has_two = False
    has_three = False
    for key,value in count.items():
        if value == 2:
            has_two = True
        if value == 3:
            has_three = True
    if has_two:
        count_two += 1
    if has_three:
        count_three += 1

# print the multiple of the two counts we made
print (count_two * count_three)

answer_printed = False # Stop working when we have an answer
for x in box_ids:
    for y in box_ids:
        if answer_printed:
            break
        different_characters = 0
        # compare characters of two lines by charcters at the same index
        for index in range(len(x)):
            if x[index] != y[index]:
                # append one to diff for each differnce identified
                different_characters += 1
        #If there is exactly one differt character then we have our pair
        if different_characters == 1:
            answer = []
            for index in range (len(x)):
                # now find those common characters and append then to answer
                if x[index] == y[index]:
                    answer.append(x[index])
            # print the array of common characters found as a single string
            print''.join(answer)
            answer_printed = True
