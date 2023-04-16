import numpy as np
from space_calculator import IndexSpaceConverter

epsolon0 = 8.8541e-12  # escolha de unidades arbitrarias
k_elemag = 1/(4*np.pi*epsolon0)


class ElemagSpaceCalculator(IndexSpaceConverter):
    def __init__(self, N, L, d):
        '''
            Attention:  L e D devem ter a mesma unidade
        '''
        super().__init__(N, L, d)
        self.Z_matrix = None  # Mátriz de Impedância
        # Potêncial , M é o número de elemetos que temos
        self.V = np.array([0]*(self.M//2) + [1]*(self.M//2))
        print(self.V)
        # Placa de cima tem potêncial 1 e a de baixo 0
        # Ele x area = carga que tem no ponto, algo como a densidade de carga  ( verificar no slide)
        self.a_vector = None

    def Z(self, m, n):
        # se  for o mesmo elemento:
        if m == n:
            return np.log(1+np.sqrt(2))*self.delta/(np.pi*epsolon0)

        # se forem 2 elementos diferentes:
        dist = self.distancia(m, n)
        return k_elemag * (self.delta**2)/dist

    def generate_matrix_Z(self, return_matrix=False):
        self.Z_matrix = np.array([
            [self.Z(m, n) for n in range(self.M)]
            for m in range(self.M)
        ])
        if return_matrix:
            return self.Z_matrix.copy()

    def calculate_a_vector(self, recalculate=False, return_result=False):
        if recalculate:  # Se foi necessário recalcular com valores diferentes dos do contructor
            self.Z_matrix = self.generate_matrix_Z
            self.a_vector = np.linalg.solve(self.Z_matrix, self.V)

        else:
            if self.Z_matrix is None:
                self.generate_matrix_Z()
            if (self.a_vector is None):
                self.a_vector = np.linalg.solve(self.Z_matrix, self.V)

        if return_result:
            return self.a_vector.copy()

    def generate_spatial_charge_matrix(self):
        if self.a_vector is None:
            self.calculate_a_vector()

        matrix_espacial = np.zeros(shape=(self.N, self.N, 2))
        for m in range(self.M):
            i, j, k = self.get_spatial_indices(m)
            # print(f"m = {m}, i = {i}, j = {j}, k = {k}")
            matrix_espacial[self.N-1-j][i][k] = self.a_vector[m]

        return matrix_espacial


# testando
if __name__ == "__main__":
    N = 128
    calculator = ElemagSpaceCalculator(N=N, L=16, d=0.1)

    print("M:", calculator.M)
    print("N:", calculator.N)
    print("L:", calculator.L)
    print("delta:", calculator.delta)
    print()
    calculator.calculate_a_vector()
    print(calculator.a_vector)

    # [[10. 11. -1. -1.]
    # [ 8.  9.  -1. -1.]
    # [ 4.  5.   6.  7.]
    # [ 0.  1.   2.  3.]]

    # [[22. 23. -1. -1.]
    # [ 20. 21. -1. -1.]
    # [ 16. 17.  18. 19.]
    # [ 12. 13.  14. 15.]]
