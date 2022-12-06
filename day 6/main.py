# Memory Complexity: O(size_marker)
# Runtime Complexity: O(n)

if __name__ == "__main__":

    def check_marker(x,size_marker=4):
        for i in range(0,len(x)-size_marker):
            x_subset = x[i:i+size_marker]
            if len(set(x_subset)) == size_marker:
                return i + size_marker
        return None

    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    print('---------- Problem 1 -------------')
    for line in Lines:
        print('Marker is found at: ' + str(check_marker(line)))  
    print('---------- Problem 2 -------------')
    for line in Lines:
        print('Marker is found at: ' + str(check_marker(line,14)))     



    





        

   
