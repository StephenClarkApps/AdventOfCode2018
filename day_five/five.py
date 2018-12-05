input = open('input.txt').read()




def opposites(x, y):
    if x.isupper() & y.isupper() | x.islower() & y.islower():
        return False
    else:
        return True


#look at character before target character and after it

counter = 0
for x in input:
    if counter == 0:
        print ("A")
    else:
        if input[counter - 1].lower() == input[counter].lower():
            #check if have differnt case to each other
            if opposites(input[counter - 1], input[counter]) == True:
                del input[counter - 1]
                del input[counter]
        else:
            print ("else")

    counter += 1


    #Check that two Chracters are the same, but have different cases
