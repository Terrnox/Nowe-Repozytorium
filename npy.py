import numpy as np
import matplotlib
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
   fig = plt.figure()
   ax = fig.add_subplot()
   ax.plot(points,x,'|',points,x)
   # Wezel poczatkowy
   ax.text(0,-0.005,'x0')
   # Wezel koncowy
   ax.text(1,-0.005,'xp')
   # Numery globalne wezlow
   ax.text(0,-0.015,'1',color='green')
   ax.text(0.25,-0.015,'5',color='green')
   ax.text(0.5,-0.015,'2',color='green')
   ax.text(0.75,-0.015,'3',color='green')
   ax.text(1,-0.015,'4',color='green')
   # Elementy
   ax.text(0.125,0.015,'1',color='blue')
   ax.text(0.375,0.015,'3',color='blue')
   ax.text(0.625,0.015,'2',color='blue')
   ax.text(0.875,0.015,'4',color='blue')
   #
   ax.text(0.01,0.005,'1',color='red')
   ax.text(0.20,0.005,'2',color='red')
   ax.text(0.27,0.005,'1',color='red')
   ax.text(0.45,0.005,'2',color='red')
   ax.text(0.52,0.005,'1',color='red')
   ax.text(0.70,0.005,'2',color='red')
   ax.text(0.77,0.005,'1',color='red')
   ax.text(0.99,0.005,'2',color='red')
   plt.show()

#def AloMem(n):
#    return A,b
    
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
  