#HW_21
def Q21():
    # 1st way
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 2nd way
    lst = [x for x in range(1, 11)]

    # 3rd way
    lst = list(range(1, 11))

    # 4th way
    lst = list()
    for i in range(1,11):
        lst.append(i)

    # 5th way
    lst = [0] * 10
    for i in range(1, 11):
        lst[i-1] = i
        
        
 #HW_22
def Q22(m):
    new_mat = [[0] * len(m)] * len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            new_mat[j][i] = m[i][j]
    flag = 0

    for i in range(len(m)):
        for j in range(len(m)):
            if m[i] == new_mat[j]:
                flag = 1

    if flag:
        return True
    else:
        return False
      
#HW_23
def check_winner(m):
    new_mat = [[0] * len(m)] * len(m)
    for i in range(len(m)):
        for j in range(len(m[0])):
            new_mat[j][i] = m[i][j]
    for i in m:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    for i in new_mat:
        if i[0] == i[1] == i[2] == 'X':
            return 'X'
        elif i[0] == i[1] == i[2] == 'O':
            return 'O'
    if m[0][0] == m[1][1] == m[2][2] == 'X':
        return 'X'
    elif m[0][0] == m[1][1] == m[2][2] == 'O':
        return 'O'
    if m[0][2] == m[1][1] == m[2][0] == 'X':
        return 'X'
    elif m[0][2] == m[1][1] == m[2][0] == 'X':
        return 'O'
    return ' '
