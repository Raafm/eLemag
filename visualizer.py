import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from elemag_calculator import ElemagSpaceCalculator


class Visualizer:
    def __init__(self, N, X=None, Y=None, Q=None):
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
        # ax.set_zlim(-1.01, 1.01)
        # ax.zaxis.set_major_locator(LinearLocator(10))
        # A StrMethodFormatter is used automatically
        # ax.zaxis.set_major_formatter('{x:.02f}')

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()

    def plot_color_charge_distribution(self, charge_distribution_matrix, show_image=False):
        # media = charge_distribution_matrix.mean()
        # , interpolation='nearest')
        plt.imshow(charge_distribution_matrix, cmap='hot_r')
        plt.colorbar()
        if show_image:
            plt.show()

    def plot3D_charge_distribution(self, charge_distribution, show_image=False, title=""):
        m, n, = charge_distribution.shape
        X = np.arange(m)
        Y = np.arange(n)
        X, Y = np.meshgrid(X, Y)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        plt.title(title)
        ax.plot_surface(X, Y, charge_distribution, cmap=cm.coolwarm)
        if show_image:
            plt.show()


def write_file(N, L, V0, charge_distribution, filename="Q2.txt"):
    f = open(filename, "w")
    f.write("========== VALUES =======\n")
    f.write(f"N = {N} ")
    f.write(f"\nL = {L} ")
    f.write(f"\nL = {L} ")
    f.write(f"\nV0 = {V0} ")
    f.write("========== RESULT =======\n")

    f.write("\nCharge Distribuition on inferior board:")
    f.write('\n')
    f.write(str(charge_distribution[:, :, 0]))

    f.write("\nCharge Distribuition on superior board:")
    f.write('\n')
    f.write(str(charge_distribution[:, :, 1]))


if __name__ == '__main__':
    N = 30
    d = 10e-2
    L = 2e-3
    V0 = 10
    calculator = ElemagSpaceCalculator(N=N, L=L, d=d, V0=V0)
    calculator.calculate_a_vector()
    visualizador = Visualizer(N=N)

    charge_distribution = calculator.generate_spatial_charge_matrix()

    # plt.subplot(1,2,1)
    write_file(N, L, V0, charge_distribution)

    visualizador.plot3D_charge_distribution(
        charge_distribution[:, :, 0], show_image=True, title="Placa Inferior")

    visualizador.plot3D_charge_distribution(
        charge_distribution[:, :, 1], show_image=True, title="Placa Superior")

    # for N in [4,8,16,32,64]:
    #     print("N =",N)
    #     calculator = ElemagSpaceCalculator(N = N, L = L, d = d)
    #     calculator.calculate_a_vector()
    #     visualizador = Visualizer(N = N)

    #     charge_distribution = calculator.generate_spatial_charge_matrix()

    #     plt.subplot(1,2,1)
    #     plt.title("placa inferior")
    #     visualizador.plot_color_charge_distribution(charge_distribution[:,:,0])

    #     plt.subplot(1,2,2)
    #     plt.title("placa superior")
    #     visualizador.plot_color_charge_distribution(charge_distribution[:,:,1])

    #     plt.show()

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
