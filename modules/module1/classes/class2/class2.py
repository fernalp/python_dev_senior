var1 = 100
var2 = 200

var = var1 + var2


print(f"The value var: {var} is the sum of var1 and var2")

width = 1203
height = 8760
area = width * height

print(f"Being the width {width} and the height {height} the area is: {area}")

# variable of type int

a = 30
b = 30

# variable of type float
d = 30.0

c = a ** b

# variable of type str
f = "3.0"
g = "30"

# variable of type bool from a relational operation
x = a == b

#Logical Operators and, or, not
# y = True  and  False (&& || !)
y = x and a == c
z = not y

#Operadores logicos y relacionales
y = (a == b and d < a) or (f == g) 

z = a*b == b*d and a*d < b*a

print(f"Resultado directo de operacion relacional y logica:{(a == b and d < a)}")

# variable tipo int
altura = 80
# variable tipo str
peso = "80"

# Conversion de str a int
# str = "80"
pesoNumEnt = int(peso)

# Conversion de str a float
# str = "80.0"
pesoNumFloat = float(peso) + 0.1
# str = "80.1"

# str value of 80
peso2 = str(pesoNumFloat)

# "80" == "80.0"
# print(peso == peso2)

# 80 == 80.0
# print(pesoNumEnt == pesoNumFloat)

xy = (a == b and d < a)
y = xy or (f == g) 


# Ejercicio 1

# print(F"El text es numero: {isNumeric or isDecimal}")

#(a == b, a != b, a > b, a < b, a >= b, a <= b)
# booleanValue = true1
# if logic booleanValue

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

inputUsuario = input("Ingresa el primer número: ")

isFloat = is_float(inputUsuario)

# if logic operation:
#    action
if not isFloat:
    inputUsuario = input("El numero no es valido, Ingresa el primer número nuevamente: ")

numero1 = float(inputUsuario)

numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# Suma: {suma}
# Suma: 100.0
# print("Suma: ", suma)
# print("Suma: " + str(suma))
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")