#HW5 - HW book 

sum = 0
for T in range(20):
  
    w = float(input(' plese enter your value in this filed :               ')
    sum += w

    if ( T == 0 ):
        
        min = w
        max = w
        
    else:
        
        if(w < min):
            min = w
            
        if(w > max):
            max = w    

            
avg = sum / 20

print('min  is =        ' , min , 'max  is =          ' , max , 'avg is =          ' , avg )
input()              
              
