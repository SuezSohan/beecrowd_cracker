""" #1060: Positive Numbers
j = 0
for x in range(6) :
    a = float(input())
    if a>0 :
        j+=1
print (j,"valores positivos") """



""" #1059: Even Numbers
for x in range(1, 101):
    if x%2 == 0 :
        print(x) """



""" #1052: Month
a = int(input())

if a==1 :
    month = "January"
elif a==2 :
    month = "February"
elif a==3 :
    month = "March"
elif a==4 :
    month = "April"
elif a==5 :
    month = "May"
elif a==6 :
    month = "June"
elif a==7 :
    month = "July"
elif a==8 :
    month = "August"
elif a==9 :
    month = "September"
elif a==10 :
    month = "October"
elif a==11 :
    month = "November"
elif a==12 :
    month = "December"

print(month) """



""" #1051: Taxes
a = float(input())
if a>=0 and a<=2000:
    print("Isento")
elif a>=2000.01 and a<=3000:
    tax = (a-2000)*0.08
    print(f"R$ {tax:.2f}")
elif a>=3000.01 and a<=4500:
    tax = (1000*0.08)+(a-3000)*0.18
    print(f"R$ {tax:.2f}")
elif a>4500:
    tax = (1000*0.08)+(1500*0.18)+(a-4500)*0.28
    print(f"R$ {tax:.2f}") """


""" #1050: DDD
a = int(input())
if a==61:
    print("Brasilia")
elif a==71:
    print("Salvador")
elif a==11:
    print("Sao Paulo")
elif a==21:
    print("Rio de Janeiro")
elif a==32:
    print("Juiz de Fora")
elif a==19:
    print("Campinas")
elif a==27:
    print("Vitoria")
elif a==31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado") """

""" #1049: Animal
x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    animal = 'aguia'
if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    animal = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    animal = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    animal = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    animal = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    animal = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    animal = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    animal = 'minhoca'

print(animal) """

""" #1048: Salary Increase
a = float(input())
if a>=0 and a<=400 :
    new = (115/100*a)
    b = 15
elif a>=400.01 and a<=800 :
    new = (112/100*a)
    b = 12
elif a>=800.01 and a<=1200 :
    new = (110/100*a)
    b = 10
elif a>=1200.01 and a<=2000:
    new = (107/100*a)
    b = 7
elif a>2000 :
    new = (104/100*a)
    b = 4

print(f"Novo salario: {new:.2f}")
print(f"Reajuste ganho: {(new-a):.2f}")
print(f"Em percentual: {b} %") """

""" #1047: Game Time with Minutes
a, b, c, d = map(int, input().split())

if c>a :
    if b>d:
        print(f"O JOGO DUROU {(c-a)-1} HORA(S) E {(60-b)+d} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {(c-a)} HORA(S) E {d-b} MINUTO(S)")
elif c == a:
    if b<d:
        print(f"O JOGO DUROU {0} HORA(S) E {d-b} MINUTO(S)")
    elif b==d:
        print(f"O JOGO DUROU {(24-a)+c} HORA(S) E {0} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {(24-a)+c-1} HORA(S) E {(60-b)+d} MINUTO(S)")
else :
    if b>d: 
        print(f"O JOGO DUROU {(24-a)+c-1} HORA(S) E {(60-b)+d} MINUTO(S)")
    else:
        print(f"O JOGO DUROU {(24-a)+c} HORA(S) E {d-b} MINUTO(S)") """

""" #1046: Game Time
a, b = map(int, input().split())

if a<b :
    print(f"O JOGO DUROU {b-a} HORA(S)")
else :
    print(f"O JOGO DUROU {(24-a)+b} HORA(S)") """

""" #1045: Triangle Types
x = list(map(float, input().split()))
x.sort(reverse=True)
a = x[0]
b = x[1]
c = x[2]

if a >= b+c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2 :
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2 :
    print ("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2 :
    print ("TRIANGULO ACUTANGULO")

if a == b and b == c :
    print ("TRIANGULO EQUILATERO")
elif a == b or b == c or c == a:
    print ("TRIANGULO ISOSCELES") """

""" #1044: Multiples
a, b = map(int, input().split())
if b%a==0 or a%b==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos") """

""" #1043: Triangle
a, b, c = map(float, input().split())

if a+b>c and b+c>a and c+a>b:
    print(f"Perimetro = {(a+b+c):.1f}")
else:
    area = 0.5*(a+b)*c
    print(f"Area = {area:.1f}") """

""" #1042: Simple Sort
a = list(map(int, input().split()))
b=[ 0, 0, 0]
i=0
for c in a:
    b[i]=c
    i+=1

i=0
l = len(a)

while(i<l):
    
    j=i
    while(j<l):
        if a[i]>a[j]:
            aux = a[j]
            a[j] = a[i]
            a[i]=aux
        j+=1
    i+=1

for x in a:
    print(x)
print()
for y in b:
    print(y) """

""" #1041: Coordinates of a Point
a, b = map(float, input().split())

if a == 0 and b == 0 :
    print("Origem")
elif a == 0 :
    print("Eixo Y")
elif b == 0 :
    print("Eixo X")
elif a>0 and b>0 :
    print("Q1")
elif a<0 and b>0 :
    print("Q2")
elif a<0 and b<0 :
    print("Q3")
elif a>0 and b<0 :
    print("Q4") """

""" #1040: Average
a, b, c, d = map(float, input().split())

ave = (a*2+b*3+c*4+d)/10
print("Media: %.1f"%ave)
if ave >= 7:
    print("Aluno aprovado.")
elif ave <5 :
    print("Aluno reprovado.")
elif ave>=5 and ave<=6.9:
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: %.1f"%e)
    ave = (ave+e)/2
    if ave>=5:
        print("Aluno aprovado.")
    elif ave<=4.9:
        print("Aluno reprovado.")
    print("Media final: %.1f"%ave) """

""" #1038: Snack
x, y= map(int, input().split())

if x==1:
    print(f"Total: R$ {4.0*y:.2f}")
elif x==2:
    print(f"Total: R$ {4.50*y:.2f}")
elif x==3:
    print(f"Total: R$ {5.00*y:.2f}")
elif x==4:
    print(f"Total: R$ {2.0*y:.2f}")
elif x==5:
    print(f"Total: R$ {1.5*y:.2f}") """

""" #1037: Interval
a = float(input())

if a>=0 and a<=25:
    print("Intervalo [0,25]")
elif a>25 and a<=50:
    print("Intervalo (25,50]")
elif a>50 and a<=75:
    print("Intervalo (50,75]")
elif a>75 and a<=100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo") """

""" #1036: Bhaskara's Formula
import math

a, b, c = map(float, input().split())

d = (b**2)-(4*a*c)
if d<0 or a==0:
    print("Impossivel calcular")
else:
    d = math.sqrt(d)
    r1 = (-b+d)/(2*a)
    r2 = (-b-d)/(2*a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}") """

""" #1035: Selection Test 1
values = map(int, input().split())
A, B, C, D = values

if B>C and D>A and C+D>A+B and C>0 and D>0 and A%2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
     """

""" #1021: Banknotes and Coins
value = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for i in notas:
    print(f"{int(value/i)} nota(s) de R$ {i:.2f}")
    value = round(value%i, 2)

print("MOEDAS:")
for i in moedas:
    print(f"{int(value/i)} moeda(s) de R$ {i:.2f}")
    value = round(value%i, 2) """

""" #1020: Age in Days
days = int(input())
year = int(days/365)
days = days - (year*365)
month = int(days/30)
days = days - (month*30)

print(f"{int(year)} ano(s)")
print(f"{int(month)} mes(es)")
print(f"{int(days)} dia(s)")
 """

""" #1019: Time Conversion
N = int(input())
m = N/60
s = N%60
h = m/60
m = m%60

print(f"{int(h)}:{int(m)}:{int(s)}") """

""" #1018: Banknotes
from math import remainder

number = int(input())
n = number
n100 = n/100
n = n%100
n50 = n/50
n = n%50
n20 = n/20
n = n%20
n10 = n/10 
n = n%10
n5 = n/5
n = n%5
n2 = n/2
n1 = n%2

print(number)
print (int(n100),"nota(s) de R$ 100,00")
print (int(n50),"nota(s) de R$ 50,00")
print (int(n20),"nota(s) de R$ 20,00")
print (int(n10),"nota(s) de R$ 10,00")
print (int(n5),"nota(s) de R$ 5,00")
print (int(n2),"nota(s) de R$ 2,00")
print (int(n1),"nota(s) de R$ 1,00")
 """

""" #1017: Fuel Spent
time = int(input())
speed = int(input())
fuel = (time*speed)/12
print("%0.3f"%fuel)
 """

""" #1016: Distance
distance = int(input())
time = (distance)/(3/6)
print(int(time),"minutos") """

""" #1015: Distance Between Two Points
import math

point1 = map(float,input().split())
point2 = map(float,input().split())

x1, y1 = point1
x2, y2 = point2

dist = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print("%0.4f"%dist) """

""" #1004: Consumption
X = int(input())
Y = float(input())
ave = X/Y
print("%.3f km/l"%ave) """

""" #1013: The Greatest
import math

values = map(int,input().split())
a,b,c = values

ab = (a+b+abs(a-b))/2
maior = (ab+c+abs(ab-c))/2

print("%d eh o maior"%maior) """

""" #1003: Simple Sum
A = int(input())
B = int(input())
soma = A+B
print("SOMA = %d"%soma) """

""" #1002: Area of a Circle
R = float(input())
A = 3.14159*R**2
print("A=%0.4f"%A) """

""" #1001: Extremely Basic
A = int(input())
B = int(input())
X = A+B
print("X = " + str(X)) """

""" #1000: Hello World!

print("Hello world!") 

"""