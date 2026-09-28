#'Exercício 18
#programa feito para calcular o preço a se pagar de um carro alugado pelo usuário
#por Calebe Camilo Da Silva Santos

km_percorrido = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

preco_final = 155.00 * dias + 0.65 * km_percorrido


print("O preço total a se pagar será de R$ %.2f" % preco_final)

