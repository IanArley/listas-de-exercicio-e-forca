# lista de exercicios estrutura

# exercicio 1

m = float(input("digite o valor em metros para ser convertido em centimetros:"))
c = m*100
print("esse valor em centimetros é:")

# exercicio 2

r = float(input("digite o valor do raiode um circulo para saber sua area:"))
ac = 3.14* r**2
print("o valor da area do circulo é:",ac,"m2")

# exercicio 3

l = float(input("digite o valor do lado do quadrado:"))
aq = l*l
print("o dobro do vaalor da sua area é:",aq**2)

# exercicio 4

vh = float(input("digite o valor ganhado por hora:"))
ht = int(input("digite a quantidade de horas trabalhadas:"))
s = vh * ht
print("o salario mensal foi:",s*30)

# exercicio 5

f = float(input("digite um valor em graus fahrenheit:"))
C = 5 * ((f-32) / 9)
print("o valor em graus celcius é:",C)

# exercicio 6

gc = float(input("digite um valor em graus celius:"))
gf = (gc * 9/5) + 32
print("o valor em graus fahrenheit é:")

# exercicio 7

n1 = int(input("digite um numero inteiro:"))
n2 = int(input("digite outro numero inteiro:"))
n3 = float(input("digite um numero real:"))
print(n1*2 + n2/2)
print(n1*3 + n3)
print(n3**2)

# exercicio 8

al = float(input("digite a sua altura:"))
pi = (72.7*al) - 58
print("seu peso ideal é:",pi)

# exercicio 9

print("1.homem")
print("2.mulher")
g = input("digite o numero que reprenta seu genero:")
h = float(input("digite sua altura:"))
if g == 1:
    PI = (72.7*h) - 58
    print("sendo um homem seu peso ideal é:",PI)

elif g == 2:
    PI = (62.1*h) - 44.7
    print("sendo uma mulher seu peos ideal é:",PI)

else:
    print("error")
