input = open('input.txt').readlines()
two_counter = 0
three_counter = 0

def get_char_counts_from_string(line):
    listOfCharac={}
    for charx in line:
        if charx in listOfCharac.keys():
            listOfCharac[charx] += 1
        else:
            listOfCharac[charx] = 1
    return listOfCharac

for line in input:
    extracted = get_char_counts_from_string(line)
    for key,val in extracted.items():
        if val == 2:
            two_counter += 1
        elif val == 3:
            three_counter += 1

print ("Two Counter: ")
print (two_counter)
print ("Three Counter: ")
print (three_counter)

print("MULTIPLIED = ")
print (two_counter * three_counter)
