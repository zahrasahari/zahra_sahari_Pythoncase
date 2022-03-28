#HW1_sinx 

x = float(input('enter a amount :     '))

x *= (3.141519 / 180)

sinus = 0

s = 1
for o in range(1 , 40 , 2):
    a = 1
    for z in range(1 , o + 1):
        a*=z
    sinus += s * (x**o) / a
    s*=-1

    
    
print('sin=', sinus)

input()
