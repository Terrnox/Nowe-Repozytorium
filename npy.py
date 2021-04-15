import numpy as np
import matplotlib.pyplot as plt

def GenTabGeo(x0,xp,n):
   tem = (xp - x0)/(n-1)
   TabGeo = np.array([0,0 *tem+x0])
   for i in range(n): 
          TabGeo = np.block([
              [TabGeo],
              [i, i*tem+x0],])
   TabGeo = np.delete(TabGeo,1,0)
   return TabGeo

def GeoShow(TabGeo,n):
   
   x = np.zeros((n,1))
   points = TabGeo[:,1]
   plt.plot(points,x,'|',points,x)
   plt.show()
  
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
xp=1
n=5

TabGeo = GenTabGeo(x0,xp,n) 
GeoShow(TabGeo,n) 
  
#def AloMem(n):
#    return A,b