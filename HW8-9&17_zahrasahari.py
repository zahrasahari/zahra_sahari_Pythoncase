#HW9
def zero_sum(num):
    z = 0
    for i in num:
        z += i
    if z == 0 :
        return True
    elif z!= 0 :
        return False
    else:
        return True
num =(4,7,9,10,-1)
x = zero_sum(num)
print(x)
#HW10
A Python dictionary is an associative container which permits access based on a key, rather than an  index. 
Unlike an index, a key is not restricted to an integer expression.
#HW11
d = {}
#HW12
d['Fred'] = 44
#HW13
If the key within the square brackets does not 
exist in the dictionary, the statement adds the key and pairs it with the value on the right of the assignment 
operator. If the key already exists in the dictionary, the statement replaces the value previously associated 
with the key with the new value on the right of the assignment operator.
Or The get method retrieves a value from the dictionary. Returns the default value if there is no requested value
#HW14
must be a valid key in dictionary , or the program will raise an exception. A valid key is a key that 
is present in the dictionary.  We see the interpreter’s reaction when we attempt to use an invalid key: the interpreter an generates 
KeyError exception.
#HW15
immutable
#HW16
(a){3: 0, 5: 1, 10: 1, 8: 2, 15: 4}
(b) 3
    5
    10
    8
    15
(c) 3
    5
    10
    8
    15
(d) 0
    1
    1
    2
    4
#HW17    
unordered
