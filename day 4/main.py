import os
import numpy as np

# Memory Complexity: O(1)
# Runtime Complexity: O(n)

if __name__ == "__main__":

    # Set working directory to file location
    path_dir = os.path.dirname(os.path.abspath(__file__))  
    os.chdir(path_dir)

    def check_value_1(line):
        line_split = [i.split("-") for i in line.split(",")]
        values = [int(line_split[0][0]),int(line_split[0][1])], [int(line_split[1][0]),int(line_split[1][1])]
        return max(is_contained(values[0],values[1]),is_contained(values[1],values[0]))

    def is_contained(first_elf,second_elf):
        if (first_elf[0] >= second_elf[0]) and (first_elf[1] <= second_elf[1]):
            return 1
        else:
            return 0

    def check_value_2(line):
        line_split = [i.split("-") for i in line.split(",")]
        values = [int(line_split[0][0]),int(line_split[0][1])], [int(line_split[1][0]),int(line_split[1][1])]
        if max(values[0][0],values[1][0]) <= min(values[0][1],values[1][1]):
            return 1
        else:
            return 0

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    num_contained = sum([check_value_1(i) for i in Lines])
    print('Number of pairs fully contained: ' + str(num_contained))

    # Problem 2
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    num_contained = sum([check_value_2(i) for i in Lines])
    print('Number of pairs overlap: ' + str(num_contained))




    





        

   
