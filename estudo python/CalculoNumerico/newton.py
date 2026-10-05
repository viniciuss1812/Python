import matplotlib.pyplot as plt
import math

def F(i):
    P = 35.000
    A = 8.500
    n = 7
    return P * (i * (1 + i)**n / ((1 + i)**n - 1)) - A

def F_derivada(i):
    P = 35.000
    n = 7
    return P * (((1 + i)**n - 1) - i * n * (1 + i)**(n - 1)) / ((1 + i)**n - 1)**2 + P * n * (1 + i)**(n - 1) / ((1 + i)**n - 1)

def F2(N):
    To = 300
    T = 1000
    uo = 1360
    q = 1.7e-19
    ni = 6.21e9
    p = 6.5e6
    formulan = 1/2*(N +(N**2 + 4*ni**2)**0.5)
    formulau = uo*(T/To)**-2.42
    return (1/(q* formulan * formulau))-p

def F2_derivada(N):
    To = 300
    T = 1000
    uo = 1360
    q = 1.7e-19
    ni = 6.21e9
    raiz = (N**2 + 4*ni**2)**0.5
    formulan = 1/2 * (N + raiz)
    derivada_formulan = 1/2 * (1 + N / raiz)
    formulau = uo * (T/To)**-2.42
    return -derivada_formulan / (q * formulau * formulan**2)

def F3(T):
    Cp_desejado = 1.1
    return (0.99403 + 1.671e-4*T + 9.7215e-8*T**2 - 9.5838e-11*T**3 + 1.9520e-14*T**4) - Cp_desejado

def F3_derivada(T):
    return 1.671e-4 + 2 * 9.7215e-8*T - 3 * 9.5838e-11*T**2 + 4 * 1.9520e-14*T**3

def F4(h):
    V = 8
    r = 2
    L = 5
    return (r**2* math.acos((r-h)/r) - (r-h) * (2*r*h - h**2)**0.5) * L - V

def F4_derivada(h):
    r = 2
    L = 5
    return 2 * L * (2*r*h - h**2)**0.5

def F5(t):
    I = 3.5
    pi = 3.14159
    e = 2.718281828
    return (9*e**-t * math.sin(2*pi*t))-I

def F5_derivada(t):
    pi = 3.14159
    e = 2.718281828
    return 9 * e**-t * (2*pi*math.cos(2*pi*t) - math.sin(2*pi*t))

def F6(theta0):
    g = 9.81
    v0 = 30
    x = 90
    y0 = 1.8
    y = 1
    return (math.tan(theta0)*x - (g/(2*v0**2 * math.cos(theta0)**2))*x**2 + y0) - y

def F6_derivada(theta0):
    g = 9.81
    v0 = 30
    x = 90
    return x / math.cos(theta0)**2 - (g * x**2 / v0**2) * math.tan(theta0) / math.cos(theta0)**2

def F7(h):
    V = 30
    pi = 3.14
    R = 3
    return (pi*h**2 *((3*R - h)/3)) -V

def F7_derivada(h):
    pi = 3.14
    R = 3
    return pi * (2*R*h - h**2)

def newton(f, fderivada, x, tolerancia):
    auxiliarinteracoes = 0
    erros = []
    interacoes = []

    while True:
        fx = f(x)
        fdx = fderivada(x)

        if fdx == 0:
            print("A derivada é zero.")
            break

        novo_x = x - (fx / fdx)
        erro = abs(novo_x - x)

        auxiliarinteracoes += 1
        erros.append(erro)
        interacoes.append(auxiliarinteracoes)

        print("interação:", auxiliarinteracoes)
        print("x:", novo_x)
        print("erro:", erro)

        x = novo_x

        if erro <= tolerancia:
            break

    print("raiz encontrada foi x =", x)
    print("f(x) =", f(x))
    print("numero de interações:", auxiliarinteracoes)

    plt.plot(interacoes, erros, marker="o")
    plt.xlabel("Número de iterações")
    plt.ylabel("Erro")
    plt.title("Erro em função do número de iterações - Newton")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # para acessar a resolução de cada questão basta descomentar a linha da respectiva função

    x = float(input("defina o chute inicial: "))
    tolerancia = 0.00001

    newton(f=F, fderivada=F_derivada, x=x, tolerancia=tolerancia)
    #newton(f=F2, fderivada=F2_derivada, x=x, tolerancia=tolerancia)
    #newton(f=F3, fderivada=F3_derivada, x=x, tolerancia=tolerancia)
    #newton(f=F4, fderivada=F4_derivada, x=x, tolerancia=tolerancia)
    #newton(f=F5, fderivada=F5_derivada, x=x, tolerancia=tolerancia)
    #newton(f=F6, fderivada=F6_derivada, x=x, tolerancia=tolerancia)
    #newton(f=F7, fderivada=F7_derivada, x=x, tolerancia=tolerancia)