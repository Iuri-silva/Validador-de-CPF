cpf = input("Informe seu CPF no formato: xxx.xxx.xxx-xx ").replace('.','').replace('-','')

numeros = cpf[:9]
contador = 10
soma1 = 0
soma2 = 0

for digito in numeros:
    soma1 += int(digito) * contador
    contador -= 1     
resto1 = 11-(soma1 % 11)
if resto1 >= 10:
    resto1 = 0

numeros += str(resto1)
contador = 11
for digito2 in numeros:
    soma2 += int(digito2) * contador
    contador -= 1
resto2 = 11-(soma2 % 11)

digitos_verificadores = cpf[-2:]
if digitos_verificadores == f"{resto1}{resto2}":
    print("Esse é um CPF válido!")
else:
    print("Esse não é um CPF válido!")