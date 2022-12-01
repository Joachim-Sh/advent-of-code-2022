import os

# Memory Complexity: O(nmb_max)
# Runtime Complexity: O(n)

if __name__ == "__main__":

    # Set working directory to file location
    path_dir = os.path.dirname(os.path.abspath(__file__))  
    os.chdir(path_dir)

    # Read file
    file = open('input.txt', 'r')
    nmb_max = 3 # The number of top elves we want to calculate the calories of
    Lines = file.readlines()
    if Lines[-1] != '\n': Lines.append('\n') # newline at end for consistency
    calories_current = 0
    elf_current = 1
    calories_max = []
    elf_max = []
    for line in Lines:
        if len(line.strip()) == 0:
            for i in range(len(calories_max)):
                if calories_current > calories_max[i]:
                    calories_max.insert(i,calories_current)
                    elf_max.insert(i,elf_current)
                    break
            if len(calories_max) < nmb_max:
                calories_max.append(calories_current)
                elf_max.append(elf_current)
            calories_max = calories_max[:min(len(calories_max),nmb_max)]
            elf_max = elf_max[:min(len(elf_max),nmb_max)]
            calories_current = 0
            elf_current += 1
        else:
            calories_current += int(line.strip())
    for i in range(len(calories_max)):
        print('Elf ' + str(elf_max[i]) + ' has ' + str(calories_max[i]) + ' calories')
    print('The total number of calories is ' + str(sum(calories_max)))

        

   
