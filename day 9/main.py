# Memory Complexity: O(n)
# Runtime Complexity: O(n*sqrt(n))

import numpy as np

if __name__ == "__main__":

    def move_T(position_T,position_H):
        if abs(position_H[0] - position_T[0]) > 1:
            if abs(position_H[1] - position_T[1]) != 0:
                position_T[1] += np.sign(position_H[1] - position_T[1]) 
            position_T[0] += position_H[0] - position_T[0] - np.sign(position_H[0] - position_T[0]) 
        if abs(position_H[1] - position_T[1]) > 1:
            if abs(position_H[0] - position_T[0]) != 0:
                position_T[0] += np.sign(position_H[0] - position_T[0]) 
            position_T[1] += position_H[1] - position_T[1] - np.sign(position_H[1] - position_T[1]) 


    def get_positions(Lines,nmb_knots):
        positions = [set() for i in range(nmb_knots)]
        position_T = [np.array((0,0)) for i in range(nmb_knots)]
        position_H = np.array((0,0))
        for line in Lines:
            distance = int(line[line.index(" "):])
            if line.startswith('R'):
               idx = 1
               sign_move = 1
            elif line.startswith('L'):
                idx = 1
                sign_move = -1
            elif line.startswith('U'):
                idx = 0
                sign_move = 1
            elif line.startswith('D'):
                idx = 0
                sign_move = -1
            for i in range(distance):
                position_H[idx] += sign_move
                for j in range(nmb_knots):
                    if j == 0:
                        move_T(position_T[j],position_H)
                    else:
                        move_T(position_T[j],position_T[j-1])
                    positions[j].add(str(position_T[j]))
        return positions


    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    positions = get_positions(Lines,nmb_knots=9)
    print('Number of positions: ' + str(len(positions[0])))
    print('Number of positions: ' + str(len(positions[-1])))
   


    





        

   
