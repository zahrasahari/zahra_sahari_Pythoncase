#HW2- enter 2 number


def bmm(A , B):
    if(A == 0):
        return B
    return bmm(A , B % A)



A = int(input('Please write a number in the field :    '))
B = int(input('Please write a number in the field :    '))

print('Bmm =    ' ,  bmm(A , B))

input()
