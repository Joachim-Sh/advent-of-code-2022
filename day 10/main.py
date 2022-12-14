# Memory Complexity: O(n)
# Runtime Complexity: O(n)

import numpy as np

if __name__ == "__main__":

    def run_cycles(X,number,cycles_add, cycles,print_val):
        strength_val = []
        for i in range(cycles_add):
            if X <= cycles % 40 <= X + 2:
                print_val += "#"
            else:
                print_val += "."
            if (cycles - 20) % 40  == 0:
                strength_val.append(X*cycles)
            if cycles % 40  == 0:
                print_val += '\n'
            cycles += 1
        X += number
        return X, cycles, strength_val,print_val

    def get_signal_strength(Lines):
        X = 1
        strength_val = []
        cycles = 1
        print_val = ""
        for line in Lines:
            if line.startswith('addx'):
                number = int(line[5:])
                cycles_add = 2
            else:
                number = 0
                cycles_add = 1
            X, cycles, strength_val_i,print_val = run_cycles(X,number,cycles_add, cycles,print_val)
            if len(strength_val_i) > 0:
                strength_val += strength_val_i
        return strength_val, print_val

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    strengths,print_val = get_signal_strength(Lines)
    print('Sum signal strengths: ' + str(np.sum(strengths[:6])))
    print(print_val)
    
   


    





        

   
