import numpy as np
import matplotlib.pyplot as plt

def generujTabliceGeometrii(x_0, x_p, n):
    temp = (x_p - x_0) / (n - 1)
    matrix = np.array([1, 0 * temp + x_0])

    for i in range(1, n, 1):
        matrix = np.block([
            [matrix],
            [i + 1, i * temp + x_0],
        ])

    matrix2 = np.array([1, 1, 2])

    for i in range(1, n - 1, 1):
        matrix2 = np.block([
            [matrix2],
            [i + 1, i + 1, i + 2],
        ])

    return matrix, matrix2

def alokacja_pamieci_na_zmienne_globalne(n):
    A = np.zeros((n, n))
    b = np.zeros((n, 1))
    return A, b

def rysuj_geometrie(WEZLY, ELEMENTY, WAR_BRZEGOWE):
    plt.plot(WEZLY[:, 1], np.zeros((np.shape(WEZLY)[0], 1)), 'black')
    plt.plot(WEZLY[:, 1], np.zeros((np.shape(WEZLY)[0], 1)), 'ro')
    for i in range(np.shape(WEZLY)[0]):
        plt.text(WEZLY[i, 1] - 0.02, -0.01, "x" + str(int(WEZLY[i, 0])))
        plt.text(WEZLY[i, 1] - 0.02, -0.02, str(int(WEZLY[i, 0])), color='green', fontsize=15)

    for i in range(np.shape(ELEMENTY)[0]):
        a = ELEMENTY[i, 1]
        b = ELEMENTY[i, 2]
        plt.text(WEZLY[a - 1, 1] + 0.01, 0.005, "1", color='red', fontsize=12)
        plt.text(WEZLY[b - 1, 1] - 0.05, 0.005, "2", color='red', fontsize=12)
        plt.text((WEZLY[b - 1, 1] - WEZLY[a - 1, 1]) / 2 + WEZLY[a - 1, 1], 0.010, str(ELEMENTY[i, 0]), color='blue',
                 fontsize=15)

    plt.arrow(np.min(WEZLY[:,1]), 0, -0.4, 0, width=0.001)
    plt.text(np.min(WEZLY[:,1]) - 0.25, 0.003, WAR_BRZEGOWE[0], color='black', fontsize=12)
    plt.arrow(np.max(WEZLY[:,1]), 0, 0.4, 0, width=0.001)
    plt.text(np.max(WEZLY[:, 1]) + 0.25, 0.003, WAR_BRZEGOWE[0], color='black', fontsize=12)

    axes = plt.gca()
    axes.set_ylim([-0.05, 0.05])

    plt.grid()
    plt.show()
    
def funkcje_bazowe(n):
    if n==0:
        f = lambda x: x*0 + 1
        df = lambda x: x*0
    elif n==1:
        f = (lambda x: -1/2*x+1/2, lambda x: 1/2*x+1/2)
        df = (lambda x: -1/2+x*0, lambda x: 1/2+x*0)
    else:
        raise Exception("Nioebsulgiwany wielomian")
    return f,df

def elementy_macierzy(dphi1,dphi2,c,phi1,phi2):
    Aij = lambda -dph1(x)*dphi2(x)+ c *phi1(x)*phi2(x)
    return Aij