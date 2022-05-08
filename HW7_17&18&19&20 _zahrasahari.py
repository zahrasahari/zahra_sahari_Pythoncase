#HW_17
def print_big_enough(lst, x):
    for i in lst:
        if i >= x:
            print(i)
    
/////////////////////////////////////////////////////////////////////////////////    
#HW_18
def next_number(lst):
    positive_int = 1
    while 1:
        if positive_int not in lst:
            return positive_int
        positive_int += 1
//////////////////////////////////////////////////////////////////////////////////
#HW_19
def reverse(lst):
    reversed_list = [0 for i in range(len(lst))]

    for i in range(len(lst)):
        reversed_list[len(lst) - i - 1] = lst[i]

    return reversed_list
//////////////////////////////////////////////////////////////////////////////////
#HW_20
 m = [[1 for i in range(9)] for j in range(6)]
    
    for i in range(6):
        for j in range(9):
            print(m[i][j], end='  ')
        print('\n')
    print('\n\n')
    m[2][4] = 0

    for i in range(6):
        for j in range(9):
            print(m[i][j], end='  ')
        print('\n')

