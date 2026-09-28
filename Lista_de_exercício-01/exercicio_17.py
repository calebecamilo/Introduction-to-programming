#Exercício 17
#Programa que solicita o preço de uma mercadoria e o percentual de desconto e exibe o valor do desconto e o preço a pagar
#por Calebe Camilo Da Silva Santos

mercadoria = float(input("Digite o preço da mercadoria: "))
percentual_de_desconto = float(input("Digite o percentual de desconto da mercadoria: digite como um inteiro(Exemplo: 15% = 15)"))
desconto = mercadoria * (percentual_de_desconto / 100)
print("O desconto é de R$ %d " % desconto)
preco_final = mercadoria - desconto
print("O preço final é de R$ %.2f" %preco_final) 
      
