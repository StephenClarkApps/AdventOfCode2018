import re
raw_input = open('input.txt').read()
raw_input_list = list(raw_input)

"""Check that two Chracters are the same, but have different cases"""
def opposites(x, y):
    if x.isupper() & y.isupper() | x.islower() & y.islower():
        return False
    else:
        return True


#look at character before target character and after it
before = []
after = ['Q']

"""pass in the input as a list and return a filtered list"""
def OnePass(list):
    the_list = list
    counter = 0
    for x in the_list:
        if counter !=0:
            if the_list[counter - 1].lower() == the_list[counter].lower():
                #check if have differnt case to each other
                if opposites(the_list[counter - 1], the_list[counter]) == True:
                    del the_list[counter]
                    del the_list[counter - 1]
        counter += 1
    return the_list


def Checks(inputx):
    before = []
    after = ['Q']
    while before != after:
        before = inputx.copy()
        after = OnePass(inputx)
        inputx = after

Checks(raw_input_list)

regex = re.compile('[^a-zA-Z]')
this = ''.join(raw_input_list)
that = regex.sub('', this)

print (len(that))


# Part 2
# cycle through the alphabet removing all a, b, c etc irregardless of cases
# then do part A on them and find the shortest
from string import ascii_lowercase
for ch in ascii_lowercase:
    print ("The character is: ")
    print (ch)
    copy_of_raw_input = raw_input
    copy_of_raw_input = copy_of_raw_input.replace(ch, "")
    copy_of_raw_input = copy_of_raw_input.replace(ch.upper(), "")
    inpu = list(copy_of_raw_input)
    Checks(inpu)
    regex = re.compile('[^a-zA-Z]')
    this = ''.join(inpu)
    that = regex.sub('', this)
    print (len(that))
