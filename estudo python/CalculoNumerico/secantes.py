import matplotlib.pyplot as plt
import math

def F(i):
    P = 35.000
    A = 8.500
    n = 7
    return P * (i * (1 + i)**n / ((1 + i)**n - 1)) - A

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

def F3(T):
    Cp_desejado = 1.1
    return (0.99403 + 1.671e-4*T + 9.7215e-8*T**2 - 9.5838e-11*T**3 + 1.9520e-14*T**4) - Cp_desejado

def F4(h):
    V = 8
    r = 2
    L = 5
    return (r**2* math.acos((r-h)/r) - (r-h) * (2*r*h - h**2)**0.5) * L - V

def F5(t):
    I = 3.5
    pi = 3.14159
    e = 2.718281828
    return (9*e**-t * math.sin(2*pi*t))-I

def F6(theta0):
    g = 9.81
    v0 = 30
    x = 90
    y0 = 1.8
    y = 1
    return (math.tan(theta0)*x - (g/(2*v0**2 * math.cos(theta0)**2))*x**2 + y0) - y

def F7(h):
    V = 30
    pi = 3.14
    R = 3
    return (pi*h**2 *((3*R - h)/3)) -V

def secante(f, x0, x1, tolerancia):
    auxiliarinteracoes = 0
    erros = []
    interacoes = []

    while True:
        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            print("Não é possível continuar, pois a divisão por zero ocorreria.")
            break

        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        erro = abs(x2 - x1)

        auxiliarinteracoes += 1
        erros.append(erro)
        interacoes.append(auxiliarinteracoes)

        print("interação:", auxiliarinteracoes)
        print("x:", x2)
        print("erro:", erro)

        x0 = x1
        x1 = x2

        if erro <= tolerancia:
            break

    print("raiz encontrada foi x =", x1)
    print("f(x) =", f(x1))
    print("numero de interações:", auxiliarinteracoes)

    plt.plot(interacoes, erros, marker="o")
    plt.xlabel("Número de iterações")
    plt.ylabel("Erro")
    plt.title("Erro em função do número de iterações - Secante")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    # para acessar a resolução de cada questão basta descomentar a linha da respectiva função

    x0 = float(input("defina o primeiro chute: "))
    x1 = float(input("defina o segundo chute: "))
    tolerancia = 0.00001

    secante(f=F, x0=x0, x1=x1, tolerancia=tolerancia)
    #secante(f=F2, x0=x0, x1=x1, tolerancia=tolerancia)
    #secante(f=F3, x0=x0, x1=x1, tolerancia=tolerancia)
    #secante(f=F4, x0=x0, x1=x1, tolerancia=tolerancia)
    #secante(f=F5, x0=x0, x1=x1, tolerancia=tolerancia)
    #secante(f=F6, x0=x0, x1=x1, tolerancia=tolerancia)
    #secante(f=F7, x0=x0, x1=x1, tolerancia=tolerancia)