#HW6 - Julius Caesar

def caezar( text , s ):
    result = "    "

    for Ch in text:
    
        if ( 'C '<=Ch <= 'Z'):
            result += chr((ord( Ch ) + s - 65) % 26 + 65)
 
        else:
            result += chr((ord( Ch ) + s - 97) % 26 + 97)
 
    return result
 

text = input('Enter the following text :                                      ')

s = int(input('Enter the shift count in this following field :                    ')
        
        
print ("res: " + caesar( text , s ))

input()
