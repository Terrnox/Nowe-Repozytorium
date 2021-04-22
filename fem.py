import numpy as np
import scipy.integrate as spint
import matplotlib.pyplot as plt
from funkcje import generujTabliceGeometrii as GenTab
from funkcje import rysuj_geometrie as rGeo
from funkcje import alokacja_pamieci_na_zmienne_globalne as Alok
from funkcje import funkcje_bazowe as FBaz
from funkcje import elementy_macierzy as ElMat
#Preprocesing

c = 0
f = lambda x:0
twb_L = 'D'
twb_R = 'D'

wwb_L = 1
wwb_R = 3

x_a = 1
x_b = 2
n = 5

wez, el = GenTab(1, x_b, n)
print(wez)
print(el)
rGeo(wez,el,[twb_L,twb_R])

#Procesing

A,b = Alok(n)
#print(A)
#print(b)

SW = 1 #stopien wielomianu
phi,dphi = FBaz(SW)
# xx = np.linspace(-1,1,101)
# plt.plot(xx,phi[0](xx),'r')
# plt.plot(xx,phi[1](xx),'g')
# plt.plot(xx,dphi[0](xx),'b')
# plt.plot(xx,dphi[1](xx),'c')

#PROCESING
liczbaElementow = np.shape(el)[0]
for ee in range(np.arrange(0,liczbaElementow)):
    EIR = ee
    EIG = el[ee,0]
    EW1 = el[ee,1]
    EW2 = el[ee,2]
    
    a = wez[EW1-1,1]
    b = wez[EW2-1,1]
    J = (b-a)/2
    
    Ml = np.zeros((SW+1,SW+1))
    
    n = 0 
    m = 0
    Ml[0,0]=J*spint.quad(ElMat(dphi[n],dphi[m],c,phi[n],phi[m]),-1,1)
    n = 0 
    m = 1
    Ml[0,1]=J*spint.quad(ElMat(dphi[n],dphi[m],c,phi[n],phi[m]),-1,1)
    n = 1
    m = 0
    Ml[0,0]=J*spint.quad(ElMat(dphi[n],dphi[m],c,phi[n],phi[m]),-1,1)
    n = 1 
    m = 1
    Ml[0,0]=J*spint.quad(ElMat(dphi[n],dphi[m],c,phi[n],phi[m]),-1,1)