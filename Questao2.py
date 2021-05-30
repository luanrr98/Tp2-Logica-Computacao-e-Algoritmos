def obrigatoriedade_voto (idade): #Função para validar idade
    if idade > 0 : #apenas prossegue se a idade for maior que 0
        if idade >= 18 and idade < 70:
            print("Tem obrigação de votar!")
        elif idade >=16 and idade < 18 or idade >= 70 :
            print("Não tem obrigação de votar!")
        else:
            print("Não tem direito a voto!")
    else: #Caso a idade seja 0 ou menor
        print("Idade inválida, tente novamente!")
#É uma função sem retorno.
        
        
print("-------Verificador de obrigatoriedade de voto-------")
idade = int(input("Digite a Idade: ")) #Input da idade
obrigatoriedade_voto(idade) #Chamada da função
print("-------Fim do Programa-------")
