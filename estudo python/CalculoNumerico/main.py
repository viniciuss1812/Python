#import matplotlib.pyplot as plt
import math
def F(i):
    P = 35.000
    A = 8.500
    n = 7

    return P * (i * (1 + i)**n / ((1 + i)**n - 1)) - A

def F2 (N):

    To = 300
    T = 1000
    uo = 1360
    q = 1.7e-19
    ni = 6.21e9
    p = 6.5e6
    formulan = 1/2*(N +(N**2 + 4*ni**2)**0.5 )
    formulau = uo*(T/To)**-2.42
    return (1/(q* formulan * formulau))-p

def F3(T):
    Cp_desejado = 1.1
    return (0.99403 + 1.671e-4*T + 9.7215e-8*T**2 - 9.5838e-11*T**3 + 1.9520e-14*T**4) - Cp_desejado

 
def F4 (h):
  V = 8
  r = 2
  L = 5
  return (r**2* math.acos((r-h)/r) - (r-h) * (2*r*h - h**2)**0.5) * L - V

  
def F5 (t):
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

def F7 (h):
    V = 30
    pi = 3.14
    R =3
    return (pi*h**2 *((3*R - h)/3)) -V

def bisseccao(f, a, b, tolerancia):
    auxiliarinteracoes = 0
    erros = []
    interacoes = []
    FA = f(a)
    FB = f(b)
    if FA * FB < 0:
        p = (a + b) / 2
        while (b - a) > tolerancia:
            if f(a) * f(p) < 0:
                b = p
            elif f(b) * f(p) < 0:
                a = p
            auxiliarinteracoes += 1
            erro = b - a

            erros.append(erro)
            interacoes.append(auxiliarinteracoes)

            p = (a + b) / 2
            print("interação:", auxiliarinteracoes)
            print("p:", p)

        print("raiz encontrada foi x = ", p)
        print("f(x) = ", f(p))
        print("numero de interações: ", auxiliarinteracoes)

        #plt.plot(interacoes, erros, marker="o")

        #plt.xlabel("Número de iterações")
       # plt.ylabel("Erro")
        #plt.title("Erro em função do número de iterações - Bisseção")

        #plt.grid()
        #plt.show()

    else:
        print("Não há raizes nesses intervalos")
    


if __name__ == "__main__":
    #str (prossiga)
    
    a = float(input("defina o intervalo A: "))
    b = float(input("defina o intervalo B: "))
    
    while a or b == float:

        tolerancia = 0.00001
        bisseccao(f=F, a=a, b=b, tolerancia=tolerancia)
        #bisseccao(f=F2, a=a, b=b, tolerancia=tolerancia)


    #bisseccao(f=F, a=a, b=b, tolerancia=tolerancia)
    
    #bisseccao(f=F3, a=a, b=b, tolerancia=tolerancia)
   # bisseccao(f=F7, a=a, b=b, tolerancia=tolerancia)
    bisseccao(f=F4, a=a, b=b, tolerancia=tolerancia)
    #bisseccao(f=F7, a=a, b=b, tolerancia=tolerancia)


#  return ((r**2* math.cos*-1*(r-h/r)) - ((r-h)((2*r*h - h**2)**0.5))) * L - V
