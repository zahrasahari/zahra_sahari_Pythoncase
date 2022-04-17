#HW6 
while(1):

    i=int(input("please Enter your numbers of finding following disks:       "))

    def Hanoi (desk = 1,start= 'A' ,temp= 'B' ,finish= 'C' ):
        if desk ==1:

            print(start + " go to " + finish)
        else:

            Hanoi(desk-1,start,finish,temp)

            print(start + " go to " + finish)

            Hanoi(desk-1,temp,start,finish)

        
    Hanoi(i,'A','B','C')
