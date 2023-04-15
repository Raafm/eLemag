import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from elemag_calculator import ElemagSpaceCalculator


class Visualizer:
    def __init__(self, N ,X, Y, Q):
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

if __name__ == '__main__':
    N = 4
    d = 1
    L = 16

    calculator = ElemagSpaceCalculator(N = N, L = L, d = d)
    calculator.calculate_a_vector()
    X = []
    Y = []
    Q = calculator.a_vector
    for m in range(calculator.M):
        x,y,z = calculator.get_spatial_positions(m) 
        X.append(x)
        Y.append(y)
    
    X = np.array(X)
    Y = np.array(Y)

    X, Y = np.meshgrid(X, Y)
    visualizador = Visualizer(N,X,Y,Q)
    visualizador.plot_charge_distribution()