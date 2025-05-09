#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
print(return_evens([0, 1, 3, 5, 7, 8, 9]))


def make_exclamation(sentence_list):
     return [sentence + "!" for sentence in sentence_list]

make_exclamation(["Hello","I'm doing great","Python is fun"])


#squared_minus_one = list()
# squared_minus_one.append((n**2) -1)
#print(squared_minus_one)

#squared_minus_one = [(n **2) - 1 for n in range(1, 11)]
#print(squared_minus_one)

#squared_ge = (n ** 2 for n in one_to_three)
#for n in squared_ge:
    #print(n)

    #print(squared_ge)

    #import sys

#list_comprehension = [n for n in range(100000)]
#generator_expression = (n for n in range(100000))

# Returns the size of an object in bytes
#sys.getsizeof(list_comprehension)
# 824456
#sys.getsizeof(generator_expression)