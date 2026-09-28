#Exercício 20
#Programa para calcular o percentual de desconto de acordo com a categoria do cliente
#por Calebe Camilo Da Silva Santos

nome_do_cliente = input("Digite o seu nome: ")
categoria = input("Digite a sua categoria(A, B, C ou D) em letra MAIÚSCULA: ")
total_comprado= float(input("Digite o total comprado R$ "))
percentual_desconto = 0

if(categoria == "A"):
    percentual_desconto = 0.08

else:
    if(categoria == "B"):
        percentual_desconto = 0.06
    else:
        if (categoria == "C"):
            percentual_desconto = 0.04
        else:
             if (categoria == "D"):
                percentual_desconto = 0.02
             else:
                 print("Digite uma categoria existente!(A, B, C ou D)")
        
preco_final = total_comprado - (total_comprado * percentual_desconto)

if(categoria == "A" or categoria == "B" or categoria == "C" or categoria == "D"):
    print("Olá,", nome_do_cliente, " Sua categoria é:", categoria, ",O preço final é de R$ %.3f " % preco_final )
else:
    print("Não foi informado uma categoria existente, fim do programa!")
