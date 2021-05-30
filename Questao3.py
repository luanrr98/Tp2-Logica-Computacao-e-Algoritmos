def vencedor (): #Definição da função
    for contador in range(5): #loop
        nome = input(f"Nome do {contador+1}º candidato: ")
        nota = int(input(f"Nota do {contador+1}º candidato:"))
        if nota <0 or nota >10: #Validação da nota
            print("Nota Inválida!")
            exit()
        if contador == 0 or nota >= nota_vencedor:
            nome_vencedor = nome
            nota_vencedor = nota
    input(f"O(a) vencedor(a) foi {nome_vencedor} e sua nota foi {nota_vencedor}!")

        
input(vencedor())

#Achei um pouco confuso ter que colocar tudo dentro da função.

