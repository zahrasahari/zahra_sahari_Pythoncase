#Hw3 

def number_len( N ):
    D = 0
    while(N != 0):
        N//=10
        D+= 1
    return D

  
  
def power_ digits (N , Q ):
    S = 0
    while( N != 0 ):
        
        U = N % 10
        S += U ** Q
        N//=10
        
    return S

  
for Y in range(1 , 1000 + 1):
  
    l = number_len( Y )
    
    S = power_digits(Y , l)
    
    if( S ==  Y ):
        print( S  , end = ',')


input()

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#HW4 -  x**3-x*2+2
def func(x): 
    return x**3-x**2+2
  
def derivFunc( x ): 
    return 3 * x**2 - 2 * x 
  

def newtonRaphson(x): 
    d = func(x) / derivFunc(x) 
    
    for e in range(10): 
        d = func(x) / derivFunc(x) 
          
        ''''''' x(e+1) = x(e) - f(x) / f'(x) 
        x = x - d       
    print("The number's root that you have entered is :   ", 
                             "%.4f"% x) 
  
x0 = -20
newtonRaphson( x0 ) 



input()
  
