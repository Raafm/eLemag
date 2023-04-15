import numpy as np
from elemag_calculator import ElemagSpaceCalculator
from space_calculator import IndexSpaceConverter

def main():
    while True:
        if input("deseja finalizar?(s/N): ") == 's':
            break
        L = input("informe tamanho do lado (L):")
        d = input("informe distancia entre as placas (d):")
        N = input("informe n° de divisoes do lado(N):")

        calculator = ElemagSpaceCalculator(N = N, L = 16, d = 1)
        calculator.calculate_a_vector()
        print(calculator.calculate_a_vector(return_result=True))