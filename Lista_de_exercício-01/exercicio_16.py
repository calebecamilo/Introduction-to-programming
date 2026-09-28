#Exercício 16
#Programa que recebe dias, horas, minutos e segundos e imprime a soma convertida em segundos 
#por Calebe Camilo Da Silva Santos

print("---" * 25)
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: (de 0 até 23)"))
minutos = int(input("Digite a quantidade de minutos: (de 0 até 59)"))
segundos = int(input("Digite a quantidade de segundos: (de 0 até 59)"))

dias = dias * 86400
horas = horas * 3600
minutos = minutos * 60

total = dias + horas + minutos + segundos
print("Temos o total de %d, segundos" %total)


