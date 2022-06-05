#HW1
A)Tuples and lists are two similar sequences. Tuples are immutable, and they cannot be changed once they are created.
While, it is a sequential list that can be changed. 
B) Shows the literal syntax of tuples by parentheses, while how literally lists are represented by square brackets. 
C)Tuples are heterogeneous and  lists are homogeneous.
D)Tuples show the structure and lists show the order.
#HW2
Similar to lists or strings that have indexes for access to their members, we use indexes to access Tupel elements in Python.
To access the nth member, all you have to do is write the name of the tuple and write the index number of the desired house in parentheses ([]).
#HW3
immutable

#HW4
ordered
#HW5
a = 1, 2, 3, 4, 5, 6, 7, 8 
a 
(1, 2, 3, 4, 5, 6, 7, 8) 
s=-,-,*s,-,-= a
s = tuple(s)
print(tuple(s))
#HW6
a = 1, 2, 3, 4, 5, 6, 7, 8 / a (1, 2, 3, 4, 5, 6, 7, 8)
s = a[3:7] 
s = tuple(s) 
print(tuple(s))
#HW7
a=7, 10, -3, 18, 6, 10 / a (7, 10, -3, 18, 6, 10)
s = x,y = t[0],t[5]
s = tuple(s)
print(tuple(s))
#HW8
def mul_tuple(tuple) : 
    product = 1
    for i in tuple:
        product = product * i 
    return product 

tuple1 = (11, 12, 4, 3)
print(tuple1) 
print("product:",mul_tuple(tuple1))



