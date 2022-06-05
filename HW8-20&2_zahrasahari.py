#HW20
the expression {} does not
 represent the empty set. In order to use the curly braces for a set, the set must contain at least one element.
The expression set() produces a set with no elements, and thus represents the empty set.
#HW21
A=set()
#HW22
immutable
#HW23
A A = {20, 19, 2, 10, 7}
B 20 in A = True 
c 20 not in A = False 
D A&B = {10,7}
E A|B = {20,19,2,10,7,4,5,9} F C < A = True 
G C <= A = True 
H C <= B = False
I A <= A = True 
J A < A = False 
K len(A) = 5
l{x + 2 for x in range(10)} = {2,3,4,5,6,7,8,9,10,11}
M {x - 2 for x in A} = {0,5,8,17,18}
N {x - 2 for x in A if x < 10} = {0,5}
