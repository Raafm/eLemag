import numpy as np

# Criando a matriz de coeficientes
A = np.array([  [2, 3],
                [0, 1]
            ])

# Criando o vetor de constantes
b = np.array([1, 2])

# Resolvendo o sistema de equações lineares
x = np.linalg.solve(A, b)

# Imprimindo a solução
print(x)
