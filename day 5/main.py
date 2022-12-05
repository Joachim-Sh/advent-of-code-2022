import os
import numpy as np

# Memory Complexity: O(1)
# Runtime Complexity: O(n)

if __name__ == "__main__":

    # Set working directory to file location
    path_dir = os.path.dirname(os.path.abspath(__file__))  
    os.chdir(path_dir)

    def parse_crates(Lines,nmb_crates):
        stacks = [[] for i in range(nmb_crates)]
        idx_crate = list(range(1,nmb_crates*4+1,4))
        for line in Lines:
            for i in range(len(idx_crate)):
                crate = line[idx_crate[i]]
                if crate != ' ':
                    stacks[i].insert(0,crate)
        return stacks

    def parse_moves_1(line,stacks):
        line_split = line.split()
        nmb_move = int(line_split[1])
        from_stack = int(line_split[3])-1
        to_stack = int(line_split[5])-1
        for i in range(nmb_move):
            removed_element = stacks[from_stack].pop()
            stacks[to_stack].append(removed_element)
        return stacks

    def parse_moves_2(line,stacks):
        line_split = line.split()
        nmb_move = int(line_split[1])
        from_stack = int(line_split[3])-1
        to_stack = int(line_split[5])-1
        stacks[to_stack] += stacks[from_stack][len(stacks[from_stack])-nmb_move:]
        del stacks[from_stack][len(stacks[from_stack])-nmb_move:]
        return stacks

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    idx_split = Lines.index("")
    nmb_crates = max([int(i) for i in Lines[idx_split-1].split()])
    stacks = parse_crates(Lines[:idx_split-1],nmb_crates)
    for line in Lines[idx_split+1:]:
        stacks = parse_moves_1(line,stacks)
    crates_top =[i[-1] for i in  stacks]
    print('Crates on top: ' + ''.join(crates_top))

    # Problem 2
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    idx_split = Lines.index("")
    nmb_crates = max([int(i) for i in Lines[idx_split-1].split()])
    stacks = parse_crates(Lines[:idx_split-1],nmb_crates)
    for line in Lines[idx_split+1:]:
        stacks = parse_moves_2(line,stacks)
    crates_top =[i[-1] for i in  stacks]
    print('Crates on top: ' + ''.join(crates_top))



    





        

   
