#HW_9
A = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] ==> A[0:5] ==> [2, 4, 6, 8, 10]
A = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10] ==> A[6:11] ==> [2, 4, 6, 8, 10]
A = [2, 3, 4, 5, 6, 7, 8, 10] ==> A[0:7:2] + A[7:] ==>! [2, 4, 6, 8, 10]
A = [2, 4, 6, 'a', 'b', 'c', 8, 10] ==> A[0:3] + A[6:] ==> [2, 4, 6, 8, 10]
A = [2, 4, 6, 8, 10] ==> A[0:5] ==> [2, 4, 6, 8, 10]
A = [] ==> IMPOSSIBLE !! HOWEVER => A[0:] + [2, 4, 6, 8, 10] ==> [2, 4, 6, 8, 10]
A = [10, 8, 6, 4, 2] ==> A[-1:-6:-1] ==> [2, 4, 6, 8, 10]
A = [2, 4, 6] ==> IMPOSSIBLE !! HOWEVER => A[0:4] + [8, 10] ==> [2, 4, 6, 8, 10]
A = [6, 8, 10] ==> IMPOSSIBLE !! HOWEVER => [2, 4] + A[0:4] ==> [2, 4, 6, 8, 10]
A = [2, 10] ==> IMPOSSIBLE !! HOWEVER => A[0:1] + [4, 6, 8] + A[1:2] ==> [2, 4, 6, 8, 10]
A = [4, 6, 8] ==> IMPOSSIBLE !! HOWEVER => [2] + A[0:3] + [10] ==> [2, 4, 6, 8, 10]

#HW_10
a [8,8,8,8]     ///// b [2,7,2,7,2,7,2,7,2,7,2,7]  /////  c [1,2,3,'a','b','c','d']
d [1,2,1,2,1,2,4,2]
e [1,2,4,2,1,2,4,2,1,2,4,2]
#HW_11
a [3,5,7,9]
b [50,60,70,80,90]
c [12,15,18]
d [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)]
e [(0,0),(0,2),(1,1),(1,3),(2,0),(2,2)]
#HW_12
(a) [x**2 for x in range (1,6)]
(b) [x/4 for x in range (1,7)]
(c) [(x,y) for x in ['B','b'] for y in [0,1,2]]
#HW_13
x in lst (show existence)
x not in lst (show not existence)
#HW_14
reverse()function is used to reverse the order of objects in a list data structure in place.
