# Memory Complexity: O(n)
# Runtime Complexity: O(n*sqrt(n))

import numpy as np

if __name__ == "__main__":

    def return_visible(grid):
        nmb_visible = 0 
        for i in range(1,grid.shape[0]-1):
            for j in range(1,grid.shape[1]-1):
                if (grid[i][j] > grid[i,:j]).all() or (grid[i][j] > grid[i,j+1:]).all() or (grid[i][j] > grid[:i,j]).all() or (grid[i][j] > grid[i+1:,j]).all():
                    nmb_visible += 1
        return nmb_visible

    def get_score(a):
        score = 0
        for val in a:
            score += 1
            if not val:
                break        
        return score 

    def return_scenic_score(grid):
        best_score = 0 
        for i in range(1,grid.shape[0]-1):
            for j in range(1,grid.shape[1]-1):
                current_score = 1
                current_score *= get_score((grid[i][j] > grid[i,:j])[::-1]) 
                current_score *= get_score(grid[i][j] > grid[i,j+1:]) 
                current_score *= get_score((grid[i][j] > grid[:i,j])[::-1]) 
                current_score *= get_score(grid[i][j] > grid[i+1:,j]) 
                if current_score > best_score:
                    best_score = current_score
        return best_score

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    grid = np.array([np.array([i for i in line]).astype(int) for line in Lines])
    nmb_visible = grid.shape[0]*2 + grid.shape[1]*2 - 4
    nmb_visible += return_visible(grid)
    print('The number of visible trees: ' + str(nmb_visible))
    max_scenic_score = return_scenic_score(grid)
    print('The most scenic score: ' + str(max_scenic_score))


    





        

   
