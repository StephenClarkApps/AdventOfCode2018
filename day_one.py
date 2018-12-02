# Advent of Code - Day One
#
# Haven't really optimized the efficiency of this approach, so, yeah :/

from array import array

import operator
import re
import sys

frequency_cache = []
current_frequency = 0
end = False

def get_operator(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        }[op]

def append_to_cache(value):
    global frequency_cache
    frequency_cache.append(value)

def doBinaryMath(operand_one, oper_ator, operand_two):
    somit = int(operand_one) * first_operator_was_positive_or_negative
    operand_one,operand_two = somit, int(operand_two)
    return get_operator(oper_ator)(operand_one, operand_two)

while end == False:
    # open our input file in read mode
    input_file = open("input", "r")

    first_operator_was_positive_or_negative = 1
    for line_from_input_file in input_file:
        string_value_of_current_frequency = str(current_frequency)
        evaluate = string_value_of_current_frequency + line_from_input_file
        # if an input line has a + or - operator prefix store that as a multiplier
        # but drop from the three parameters passed to our expression
        # evaluation function

        # reset first_operator_was_positive_or_negative to 1
        first_operator_was_positive_or_negative = 1

        if evaluate[0] == "+":
            first_operator_was_positive_or_negative = 1
            evaluate = evaluate[1:]
        elif evaluate[0] == "-":
            first_operator_was_positive_or_negative = -1
            evaluate = evaluate[1:]

        current_frequency = doBinaryMath(*(re.findall('[+-/*//()]|\d+',evaluate)))

        if current_frequency in frequency_cache:
            print("The first recurring frequency was: " + str(current_frequency))
            quit()
        append_to_cache(current_frequency)
        evaluate = ""
        # Comment in and out the following line to output result 1 or result 2:
        #end = True
    input_file.close()

print ("The final total is: " + str(current_frequency))
