def algebraic_division(F, D):
    Q = None  # Quotient
    qq=[]
    for d in D:
        # Find all cubes in F that contain the product term d
        C = [cube for cube in F if all(literal in cube for literal in d)]
        # If no such cubes exist, return quotient 0 and the remainder F
        if not C:
            return [], F
        for f in C:
            if d in f:
                q = f.replace(d, "")
                qq.append(q)
        C=qq
        # If Q is empty, initialize Q with C
        if not Q:
            Q = C
            qq=[]
        else:
            # Intersection of Q and C
            Q = [cube for cube in Q if cube in C]
    # Calculate the remainder R
    QxD = combine_lists(Q, D)
    F=sort_strings_in_list(F)
    R=create_new_list(QxD,F)
    return Q, R
#===================================================
def combine_lists(list1, list2):
    result = []
    for element1 in list1:
        for element2 in list2:
            combined = element1 + element2
            sorted_combined = ''.join(sorted(combined))
            result.append(sorted_combined)
    return result
#===================================================
def create_new_list(list1, list2):
    new_list = []
    
    # Add strings from list1 that are not in list2
    for string1 in list1:
        if string1 not in list2:
            new_list.append(string1)
    
    # Add strings from list2 that are not in list1
    for string2 in list2:
        if string2 not in list1:
            new_list.append(string2)
    
    return new_list
#===================================================
def sort_strings_in_list(input_list):
    sorted_list = []
    for string in input_list:
        sorted_string = ''.join(sorted(string))
        sorted_list.append(sorted_string)
    return sorted_list
#===================================================
def read_boolean_function(file_path):
    with open(file_path, 'r') as file:
        cubes = [line.strip().replace(' ', '') for line in file]
    return cubes
#===================================================
def write_output_to_file(quotient, remainder, output_file):
    with open(output_file, 'w') as file:
        if quotient:
            file.write("Quotient:\n")
            for cube in quotient:
                file.write(' '.join(cube) + '\n')
        else:
            file.write("Quotient: 0\n")
        
        if remainder:
            file.write("\nRemainder:\n")
            for cube in remainder:
                file.write(' '.join(cube) + '\n')
        else:
            file.write("Remainder: 0\n")
#===================================================
def main():
    file_path_F_function = 'C:\\Users\\hp\\Desktop\\VLSI\\input.txt'
    file_path_D_function = 'C:\\Users\\hp\\Desktop\\VLSI\\divisor.txt'
    file_path_output = 'C:\\Users\\hp\\Desktop\\VLSI\\algoutput.txt'
    F = read_boolean_function(file_path_F_function)
    D = read_boolean_function(file_path_D_function)
    if F and D:
        Q, R = algebraic_division(F, D)
        write_output_to_file(Q, R, file_path_output)

if __name__ == "__main__":
    main()
