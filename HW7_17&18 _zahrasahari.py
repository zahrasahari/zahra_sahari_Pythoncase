#HW_17
def bigenough(lis):
    x = int(input("Enter a number as acompare:"))
    jadid=[]
    for i in lis:
        if  i>=x:
            jadid += [i]
    return jadid
    
lis=[]
for i in range (0,4):
    n=int(input("Enter a number of list:"))
    lis+=[n]
    
/////////////////////////////////////////////////////////////////////////////////    
#HW_18
def next_number(lst):
    mymax = 0
    num = 0
    for i in lst:
        if i > mymax:
            mymax = i

    for i in range(1, mymax + 1):
        if i not in lst:
            return i

    return mymax + 1


print(next_number(lst))
//////////////////////////////////////////////////////////////////////////////////
#HW_19
def reverse(lis):
    jadid=[]
    for i in lis[ ::-1]:
            jadid += [i]
    return jadid
//////////////////////////////////////////////////////////////////////////////////
#HW_20


