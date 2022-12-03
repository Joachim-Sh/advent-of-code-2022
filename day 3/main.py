import os
import string
import numpy as np

# Memory Complexity: O(n)
# Runtime Complexity: O(n*size_word)

if __name__ == "__main__":

    # Set working directory to file location
    path_dir = os.path.dirname(os.path.abspath(__file__))  
    os.chdir(path_dir)

    alphabet=string.ascii_lowercase + string.ascii_uppercase

    def calc_priority_1(line):
        firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
        res = set(firstpart).intersection(secondpart)
        sum_priority = sum([alphabet.index(i) + 1 for i in res])
        return sum_priority

    def calc_priority_2(line):
        a, b, c = line[0],line[1],line[2]
        res = set(a).intersection(b, c)
        sum_priority = sum([alphabet.index(i) + 1 for i in res])
        return sum_priority

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    sum_priority = sum([calc_priority_1(i) for i in Lines])
    print('Sum of the priorities: ' + str(sum_priority))

    # Problem 2
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    sum_priority = sum([calc_priority_2(Lines[i:i+3]) for i in np.arange(0,len(Lines),3)])
    print('Sum of the priorities: ' + str(sum_priority))





        

   
