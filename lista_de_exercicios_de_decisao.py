# lista de exercicios de decisao

# exercicio 1

n = int(input("digite um valor numerico:"))
if n > 10:
    print("o valor é maior que dez")
    
elif n == 10:
    print("o valor é igual a dez")
    
else:
    print("o valor é menor que dez")
    
    
# exercio 2

n2 = int(input("digite um numero:"))
if n2 >= 0 :
    print("o valor é positivo")
 
else:
    print("o valor é negativo")
    
# exercico 3

m = int(input("digite o número de maçãs compradas: "))
if m > 12:
    valor = m*1
    print("o valor de sua compra é:",valor)
    
else:
    valor = m*1.30
    print("o valor de sua compra é:",valor)
    
    
# exercicio 4

nota1 = float(input("digite a primeira nota:"))
nota2 = float(input("digite a segunda nota:"))
media =((nota1 + nota2)/2)
if media >= 6:
    print("aluno aprovado!")
    print("a média do aluno fo:",media)
    
else:
    print("aluno reprovado")
    print("a média do aluno foi:",media)
    
# exercicio 5

v1 = int(input("digite um valor:"))
v2 = int(input("digite outro valor:"))
if v1 > v2:
    print("o primeiro valor digitado é maior")
    
elif v1 < v2:
    print("o segundo valor é menor")
    
else:
    print("os valores devem ser diferentes")
    
# exercicio 6

va1 = int(input("digite um valor:"))
va2 = int(input("digite outro valor:"))
if va1 > va2 :
    print(va1, va2)
    
elif va1 == va2 :
    print(va1, va2)
    
else:
    print(va2,va1)
    
# exercicio 7

nc = input("digite o numero da conta:")
s = float(input("o saldo em conta é:"))
d = float(input("o valor do débito em conta é:"))
c = float(input("o valor do crédito em conta é"))
sa = s - ( d + c )
if sa > 0 :
    print("o saldo atual da conta:",sa ,"está positivo")
    
elif sa == 0 :
    print("o saldo atual da conta é:",sa)

else:
    print("o saldo atual da conta:",sa , "é negativo")
    
# exercicio 8

qa = int(input("digite a quantidade atual em estoque:"))
qmax = 100
qmin = 50
qme = ((qmax + qmin)/2)     
if qa >= qme :
    print("Não efetuar a compra!")

else :
    print("Efetuar a compra!")  
    
# exercicio 9

N1 = float(input("Digite o valor da nota 1:"))
N2 = float(input("digite oo valor da nota 2:"))
ME = ((N1 + N2)/2)
if ME >= 9.0 :
    MEC = "A"
 
elif ME >= 7.5 :
    MEC = "B"
    
elif  ME >= 6.0 :
    MEC = "C"
    
elif ME >= 4.0 :
    MEC = "D"
    
else:
    MEC = "E"
    
if ME >= 6.0 :
    print("Aprovado")
    print("o conceito da média é:",MEC)
    
else:
    print("Reprovado")
    print("o conceito é da média é:",MEC)
