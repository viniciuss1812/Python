
def gaussJacobi(A, b, vetorSolucao, precisao, iteracoes):
    iteracao = 0

    while iteracao < iteracoes:
        vetorAuxiliar = []

        for i in range(len(A)):
            x = b[i]

            for j in range(len(A)):
                if i != j:
                    x -= A[i][j] * vetorSolucao[j]

            x = x / A[i][i]
            vetorAuxiliar.append(x)

        erro = max(
            abs(vetorAuxiliar[i] - vetorSolucao[i])
            for i in range(len(A))
        )

        iteracao += 1

        print("Iteração:", iteracao)
        print("Valores:", vetorAuxiliar)
        print("Erro:", erro)
        print()

        vetorSolucao = vetorAuxiliar.copy()

        if erro < precisao:
            break

    print("Solução final:", vetorSolucao)
    print("Número de iterações:", iteracao)

    if erro < precisao:
        print("O método convergiu.")
    else:
        print("O método atingiu o limite de iterações.")

    return vetorSolucao




if __name__ == "__main__":

    precisao = 0.00001
    iteracoes = 1000

    # QUESTÃO 2
    A2 = [
        [18, 3, 2, 2],
        [3, 14, 2, 5],
        [2, 4, 16, 6],
        [2, 3, 6, 24]
    ]
    b2 = [650, 720, 750, 990]
    chute2 = [0, 0, 0, 0]
    

    # QUESTÃO 3
    A3 = [
        [22, 8, 10],
        [0.12, 0.33, 0.20],
        [0.6, 1, 2.6]
    ]
    b3 = [2120, 34, 164]
    chute3 = [0, 0, 0]

    # QUESTÃO 4
    A4 = [
        [6, 2, 3],
        [2, 5, 2],
        [1, 3, 5]
    ]
    b4 = [80, 60, 95]
    chute4 = [0, 0, 0]

    # QUESTÃO 6
    A6 = [
                [18, 3, 2, 2],
                [3, 14, 2, 5],
                [2, 4, 16, 6],
                [2, 3, 6, 24]
            ]
    b6 = [650, 720, 750, 990]
    chute6 = [0, 0, 0, 0]

    # Para resolver uma questão, descomente somente a linha desejada.

    #gaussJacobi(A2, b2, chute2, precisao, iteracoes)  # Questão 2
    # gaussJacobi(A3, b3, chute3, precisao, iteracoes)  # Questão 3
    # gaussJacobi(A4, b4, chute4, precisao, iteracoes)  # Questão 4 
    gaussJacobi(A6, b6, chute6, precisao, iteracoes)  # Questão 6 da prova
