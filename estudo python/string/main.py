s = "programa"

print(s[0])
print (s[-1])

print (s[0:3])
print (s[3:])
print(len(s))
print("gram" in s)
print(s + "ção")
print(s[::-1])
#Deixa cada palavra com a inicial maiúscula.
#3. Conta quantas palavras tem o nome.
#4. Mostra só o primeiro nome.
#5. Mostra as iniciais (ex.: M.D.S.)#
print ("Segunda Parte")
print ("")
nome = " maria DA silva "
print(nome.split())

palavras = nome.split()
print(len(palavras))
print (palavras[0])
print (nome.title())


iniciais = ""
for palavra in palavras:
    iniciais += palavra[0].upper()+"."

print (iniciais)

cpf = input(str("Digite um cpf"))
if len(cpf) == 11:
    print(f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")
else: 
    print ("CPF INVÁLIDO")



#print (palavra[0].upper(), end="")





