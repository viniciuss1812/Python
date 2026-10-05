def checarprimo (numero):
    try:
      resultado = numero%2

      if resultado == 0:
       return print ("O numero é primo")
      else:
       return print("Não é primo")
      
    except ValueError:
      
      print("Digite apenas números!")



def imc(peso, altura):
  try: 
   calculoimc = (altura*altura)/ peso
   return print("O IMC é",calculoimc)
  except:
    print ("ERRO", Exception)


   
def calculardesconto(oreco):
  return 0


def convertertemp(temp):
  return 0



def main():
 
 numero = int(input("Escolha um numero do menu"))
 if numero> 4:
   print ("Error")

 else:
   resposta = "Sim"
   while resposta == "Sim":
     
    if numero == 1:
     print ("Função checar se número é primo")
     num = int(input("Digite o número"))
     checarprimo(num)
     resposta = input("Deseja contunuar?")
     continue

    if numero == 2:
     print ("Função IMC")
     num = int(input("Digite o peso e altura"))
     checarprimo(num)
     resposta = input("Deseja contunuar?")
     continue

    if numero == 3:
     print ("Função calcular desconto dado o preço e uma porcentagem.")
     num = int(input("Digite o número"))
     checarprimo(num)
     resposta = input("Deseja contunuar?")
     continue

  
    if numero == 4:
     print ("Função converter_temperatura")
     num = int(input("Digite o número"))
     checarprimo(num)
     resposta = input("Deseja contunuar?")
     continue


if __name__ =="__main__":
  main()
   

     
   


  
  
  
  

