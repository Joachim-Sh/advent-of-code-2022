# Memory Complexity: O(n)
# Runtime Complexity: O(n)

if __name__ == "__main__":

    def get_dir_structure(Lines):
        dict_content = {}
        current_dict = dict_content
        levels = []
        for line in Lines:
            if line.startswith('$ cd'):
                if line.endswith('..'):
                    levels.pop()
                    current_dict = dict_content
                    for level in levels:
                        current_dict = current_dict[level]
                else:
                    name = line[5:]
                    if name not in current_dict:
                        current_dict[name] = {}
                    current_dict = current_dict[name]
                    levels.append(name)
            elif line.startswith('dir'):
                name = line[4:]
                current_dict[name] = {}
            elif line.startswith('$ ls'):
                continue
            else:
                size, name = line.split(" ")
                current_dict[name] = size  
        return dict_content

    def get_size_dir(dict_content,sum_values):
        if type(dict_content) is dict:
            sum = 0
            for name, value in dict_content.items():
                sum += get_size_dir(value,sum_values)
            sum_values.append(sum)
            return sum
        else:
            return float(dict_content)


    # Problem 1 
    file = open('input.txt', 'r')
    Lines = file.read().splitlines() 
    dict_content = get_dir_structure(Lines)
    sum_values = []
    total_size = get_size_dir(dict_content,sum_values)
    print('Total size: ' + str(sum([i for i in sum_values if i <= 100000])))
    # Problem 2
    min_required = 30000000 - (70000000 - total_size)
    print('Total size: ' + str(min([i for i in sum_values if i >= min_required])))


    





        

   
