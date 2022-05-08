#HW_15
def sumlist(L):
    sum=0
    for n in L:
        if n>0:
            sum+=n
    return sum 
    
L=[]
for i in range (0,4):
    n=int(input("Enter a number of list:"))
    L+=[n]
    
z= sumlist(L) 
print(z,"the sum of positive numbers")
if len(L)==0:
    print("the list is empty")
    
///////////////////////////////////////////////////////////////////////////////    
#HW_16
def count_evens(nums):
    count = 0
    for n in nums:
        if  n%2==0:
            count += 1
    return count
    
nums=[]
for i in range (0,4):
    n=int(input("Enter a number of list:"))
    nums+=[n]
        
print (count_evens(nums))
    
    
