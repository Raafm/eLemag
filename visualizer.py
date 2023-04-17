import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from elemag_calculator import ElemagSpaceCalculator


class Visualizer:
    def __init__(self, N ,X = None, Y = None, Q = None):
        self.N = N
        self.X = X, 
        self.Y = Y
        self.Q = Q
    
    def plot_charge_distribution(self):
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        # Plot the surface.
        surf = ax.plot_surface(self.X, self.Y, self.Q, cmap=cm.coolwarm,
                                linewidth=0, antialiased=False)

        # Customize the z axis.
        #ax.set_zlim(-1.01, 1.01)
        #ax.zaxis.set_major_locator(LinearLocator(10))
        # A StrMethodFormatter is used automatically
        #ax.zaxis.set_major_formatter('{x:.02f}')

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()
    
    def plot_color_charge_distribution(self, charge_distribution_matrix, show_image=False, cmap=cm.coolwarm, tamanho_figura = None):
        
        # media = charge_distribution_matrix.mean()
        plt.imshow(charge_distribution_matrix, cmap= cmap)#, interpolation='nearest')
        plt.colorbar()
        if show_image: plt.show()

    def plot3D_charge_distribution(self, charge_distribution, show_image=False):
        m, n, = charge_distribution.shape
        X = np.arange(m)
        Y = np.arange(n)
        X,Y = np.meshgrid(X,Y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        ax.plot_surface(X, Y, charge_distribution,cmap=cm.coolwarm)
        if show_image: plt.show()

if __name__ == '__main__':
    N = 16
    d = 16
    L = 16

    # calculator = ElemagSpaceCalculator(N = N, L = L, d = d)
    # calculator.calculate_a_vector()
    # visualizador = Visualizer(N = N)

    # charge_distribution = calculator.generate_spatial_charge_matrix()

    # # plt.subplot(1,2,1)
    # plt.title("placa inferior")
    # visualizador.plot3D_charge_distribution(charge_distribution[:,:,0],show_image=True)

    # plt.title("placa superior")
    # visualizador.plot3D_charge_distribution(charge_distribution[:,:,1],show_image=True)

    plt.figure(figsize = (10,10))
    lista_N = [4,8,16,32]
    for i,N in enumerate(lista_N):
        print("N =",N)
        calculator = ElemagSpaceCalculator(N = N, L = L, d = d)
        calculator.calculate_a_vector()
        visualizador = Visualizer(N = N)

        charge_distribution = calculator.generate_spatial_charge_matrix()

        # plt.subplot(1,2,1)
        # plt.title("placa inferior")
        # visualizador.plot_color_charge_distribution(charge_distribution[:,:,0])

        plt.subplot(1,len(lista_N),i+1)
        plt.title("placa superior")
        visualizador.plot_color_charge_distribution(charge_distribution[:,:,1], cmap = 'hot_r')
        
    plt.show()
    
    

        
    # X = []
    # Y = []
    # Q = calculator.a_vector
    # for m in range(calculator.M):
    #     x,y,z = calculator.get_spatial_positions(m) 
    #     X.append(x)
    #     Y.append(y)
    
    # X = np.array(X)
    # Y = np.array(Y)

    # X, Y = np.meshgrid(X, Y)
    # visualizador = Visualizer(N,X,Y,Q)
    # visualizador.plot_charge_distribution()