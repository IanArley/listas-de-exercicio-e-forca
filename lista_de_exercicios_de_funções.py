
# exercicio 1

def somaImposto(taxaImposto, custo):
    custo += custo * taxaImposto/100
    return custo

custo_do_item = float(input("Digite o valor do item: "))
taxa = float(input("Digite o valor da porcetagem da taxa do imposto (apenas o número sem o sinal de porcetagem!): "))
total = somaImposto(taxa, custo_do_item)
print(f"O custo final do item em questão é: {total}R$")


# exercicio 2

frase = input("Digite uma frase para saber quantos dígitos ela possui: ")

contador = 0
for caractere in frase:
        contador += 1

print(f"A quantidade de digitos que essa frase possui é: {contador}")

# exercicio 3

def inverso(x):
      contrario = x[::-1]
      return contrario

numero = str(input("Digite um número(inteiro) cujo qual deseja ver o inverso: "))
contrary = inverso(numero)
print(f"O inverso desse numero é: {contrary}")



 