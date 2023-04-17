from elemag_calculator import ElemagSpaceCalculator
import matplotlib.pyplot as plt
capacitance_list = []
lista_N = list(range(4,33,4)) 
for N in lista_N:
    voltage = 10
    calc = ElemagSpaceCalculator(N = N, L = 0.1, d = 2e-3, Voltage=voltage)

    calc.calculate_a_vector()

    charge = calc.a_vector[calc.M//2:].sum()*(calc.delta**2)
    capacitance = charge/voltage
    print(f"Capacitance using N={N}: ", capacitance)
    capacitance_list.append(capacitance)


plt.title("N x Capacitance")
plt.ylabel("capacitance")
plt.xlabel("N")
plt.ylim(9.26e-11, 9.27e-11)
plt.plot(lista_N,capacitance_list,'o')
plt.show()

# Capacitance using N=4:  9.266709880079397e-11
# Capacitance using N=8:  9.266709880079397e-11
# Capacitance using N=12:  9.266709880079397e-11
# Capacitance using N=16:  9.266709880079397e-11
# Capacitance using N=20:  9.266709880079397e-11
# Capacitance using N=24:  9.266709880079397e-11
# Capacitance using N=28:  9.266709880079397e-11
# Capacitance using N=32:  9.266709880079397e-11