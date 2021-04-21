import numpy as np
from funkcje import generujTabliceGeometrii as GenTab
from funkcje import rysuj_geometrie as rGeo
from funkcje import alokacja_pamieci_na_zmienne_globalne as alok

wezly = np.array([[1, 0],
                  [2, 1],
                  [3, 0.5],
                  [4, 0.75]])

elementy = np.array([[1, 1, 3],
                     [2, 4, 2],
                     [3, 3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 1
wwb_R = 3

wez, el = GenTab(1, 2, 5)

rGeo(wez,el,[twb_L,twb_R])