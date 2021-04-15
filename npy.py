import numpy as np
import matplotlib.pyplot as plt

Twe = np.array([[1, 0],
               [2, 1],
               [3, 0.5],
               [4, 0.75]])

Tel = np.array([[1, 1, 3],
                [2, 4, 2],
                [3, 3, 4]])

twb_L = 'D'
twb_P = 'D'

wwb_L = 0
wwb_P = 1

x0=0
xp=2
n=100

Twe = np.zeros((n,3))
print(Twe)
#def GenTabGeo(x0,xp,n):
   # np.linspace(x0,xp,n)
    #for i in range(n):        
    #return Twe,Tel

#def GeoShow():
 #   plt.plot(Twe,Tel)
 #   plt.show()
    
#def AloMem(n):
#    return A,b