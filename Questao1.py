def valor_servico(percentual,valor_conta):  #Função para calcular o total da conta com a taxa de serviço
    valor_percentual = valor_conta * percentual
    valor_total = valor_conta+valor_percentual
    return(valor_total) #Retorna o valor total

def divisao_conta (pessoas, valor_total): #Função para calcular o valor da conta dividido   
    valor_dividido = valor_total/pessoas
    return(valor_dividido) #Retorna o valor dividido

pessoas = int(input("Informe o numero de pessoas na mesa: "))
if pessoas <= 0: #verificando se o número de pessoas é menor ou igual a 0
    print("Valor Inválido")
    exit()
percentual = float(input("Informe o percentual do serviço, entre 0 e 1: "))
if percentual < 0 or percentual > 1: #verificando se o percentual é menor que zero ou maior que 1
    print("Valor Inválido")
    exit()
valor_conta = float(input("Informe o valor total da conta: R$"))
if valor_conta <= 0: #Verificando se o valor da conta é menor ou igual a zero
    print("Valor Inválido")
    exit()

valor_total = valor_servico(percentual, valor_conta)#Recebe a função valor_servico

valor_dividido= divisao_conta(pessoas,valor_total)#Recebe a função divisao_conta

valor_dividido= str(valor_dividido).replace('.',',') #Substituindo . por ,
valor_total = str(valor_total).replace('.',',') #Substituindo . por ,

print(f"O valor total da conta, incluindo a taxa de serviço, é de: R${valor_total}")
print(f"Dividindo a conta por {pessoas} pessoa(s), cada pessoa deverá pagar: R${valor_dividido}")