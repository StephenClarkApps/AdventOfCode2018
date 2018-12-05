import re
input_file = open('input.txt').read()
#input_file = "dabAcCaCBAcCcaDA"
input = list(input_file)

def opposites(x, y):
    if x.isupper() & y.isupper() | x.islower() & y.islower():
        return False
    else:
        return True


#look at character before target character and after it
before = []
after = ['Q']
def OnePass():
    counter = 0
    for x in input:
        if counter == 0:
            print ("S")
            # if input[counter].lower() == input[counter + 1].lower():
            # #check if have differnt case to each other
            #     if opposites(input[counter], input[counter + 1]) == True:
            #         del input[counter]
            #         del input[counter + 1]
        else:
            if input[counter - 1].lower() == input[counter].lower():
                #check if have differnt case to each other
                if opposites(input[counter - 1], input[counter]) == True:
                    del input[counter]
                    del input[counter - 1]
        counter += 1

print (len(input))
    #Check that two Chracters are the same, but have different cases
while before != after:
    print ("A")
    before = input.copy()
    OnePass()
    after = input.copy()
    if before == after:
        print ("Before == After ??")

print (''.join(input))

regex = re.compile('[^a-zA-Z]')
this = ''.join(input)
that = regex.sub('', this)

print (input)
print (len(that))
