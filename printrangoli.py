# -*- coding: utf-8 -*-
##prints a ‘rangoli’ basically a letter pattern
##input is size output is picture
##example:
##print_rangoli(7)
'''
------------g------------
----------g-f-g----------
--------g-f-e-f-g--------
------g-f-e-d-e-f-g------
----g-f-e-d-c-d-e-f-g----
--g-f-e-d-c-b-c-d-e-f-g--
g-f-e-d-c-b-a-b-c-d-e-f-g
--g-f-e-d-c-b-c-d-e-f-g--
----g-f-e-d-c-d-e-f-g----
------g-f-e-d-e-f-g------
--------g-f-e-f-g--------
----------g-f-g----------
------------g------------
'''



def print_rangoli(size):
    
    abet='abcdefghijklmnopqrstuvwxyz'
    
    def rangoli_str(n,m):
        half=[abet[n-i-1] for i in range(m)]
        half='-'.join(half)
        if n-m-1==-1:
            if n==2:
                return 'b-a-b'
            else:
                return half+'-'+half[:-2][::-1]
        else:
            return half+'-'+abet[n-m-1]+'-'+half[::-1]
    
    width=len(rangoli_str(size,size))
    
    for i in range(size-1):
        print(rangoli_str(size,i).center(width,'-'))
    
    print(rangoli_str(size,size))
    
    for i in reversed(range(size-1)):
        print(rangoli_str(size,i).center(width,'-'))
