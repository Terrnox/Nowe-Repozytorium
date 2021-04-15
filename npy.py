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

x0=1
xp=2
n=5

def GenTabGeo(x0,xp,n):
   tem = (xp - x0)/(n-1)
   TabGeo = np.array([0,0 *tem+x0])
   for i in range(n): 
          TabGeo = np.block([
              [TabGeo],
              [i, i*tem+x0],])
   TabGeo = np.delete(TabGeo,1,0)
   return TabGeo

print(GenTabGeo(x0,xp,n))


def GeoShow(TabGeo):
   np.array(TabGeo)
   np.array(TabGeo)
   plt.plot()
   plt.show()
    
#def AloMem(n):
#    return A,b