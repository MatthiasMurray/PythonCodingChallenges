# -*- coding: utf-8 -*-
## input an integer, output an array of spiral numbers i.e. input 3, output:
##	123
##	894
##	765


def spiralNumbers(n):
    N=[[0 for i in range(n)] for j in range(n)]
    Q=[[[0,k] for k in range(n)]]
    d=0
    t=n-1
    u=Q[-1][-1][0]
    v=Q[-1][-1][1]
    while t>0:
        if d%2==0:
            Q.append([[j,v] for j in range(u+1,u+1+t)])
            u=Q[-1][-1][0]
            Q.append([[u,i] for i in range(v-1,v-1-t,-1)])
            v=Q[-1][-1][1]
        if d%2==1:
            Q.append([[j,v] for j in range(u-1,u-1-t,-1)])
            u=Q[-1][-1][0]
            Q.append([[u,i] for i in range(v+1,v+1+t)])
            v=Q[-1][-1][1]
        t-=1
        d+=1
    
    Q=[x for y in Q for x in y]
    c=1
    for i in Q:
        N[i[0]][i[1]]=c
        c+=1
    
    return N
