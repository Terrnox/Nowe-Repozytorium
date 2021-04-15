import numpy as np
import matplotlib.pyplot as plt

#Twe = np.array([[1, 0],
#               [2, 1],
#               [3, 0.5],
#               [4, 0.75]])

#Tel = np.array([[1, 1, 3],
#                [2, 4, 2],
#                [3, 3, 4]])

#twb_L = 'D'
#twb_P = 'D'

#wwb_L = 0
#wwb_P = 1

def GenTabGeo(x0,xp,n):
    
    val = (xp - x0)/(n-1)
    T1 = np.array([x0])
    
    for ind_T1 in range (1,n-1,1):
        T1 = np.block([T1, ind_T1 * val + x0])
        
    T2 = np.zeros((n-1,2))
    
    for ind_T2 in range (0,n-1,1):
        T2[ind_T2][0] = ind_T2 + 1
        T2[ind_T2][1] = ind_T2 + 2
        
    return ind_T1,T1,T2


def GeoShow(T1,T2,n):
    T = np.zeros((n))
    plt.plot(T1,T)
    for i in range(0,n,1):
        plt.text(T1[i],-0.01, str(i+1),color='green')
        plt.text(T1[i],0,'|')
        plt.text(T1[i+1]/2+T1[i]/2, 0.005,str(i+1),color='blue')

#def AloMem(n):
#    return A,b    

x0=0
xp=1
n=100

Nodes, T1, T2 = GenTabGeo(0, 1, 4)
GeoShow(T1,T2,Nodes+1)
 
  