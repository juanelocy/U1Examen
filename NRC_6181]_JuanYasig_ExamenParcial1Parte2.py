class Calculo:
    #constructor de la clase Calculo
    def __init__ (self):
        suma=1+5
        resta=9-6

#===================================================
#2 - Crear un método llamado Factorial() que permita calcular el factorial de un entero. Pruebe el método instanciando la clase.
def Factorial():
    fac=int(input("Ingrese un numero: "))
    fac=fac*fac-1*fac-2*fac*-3*fac-4*fac-5
    print(fac)
#===================================================
#3 - Crear un método llamado Suma() que permita calcular la suma de los primeros n enteros 1 + 2 + 3 + .. + n. Pruebe este método.
def Suma():
    sumaN=int(input("Ingrese un numero para sumar desde 1: "))
    b=0
    for i in range(1,sumaN+1):
        print(i)
        b=b+1
        print("La suma de todo es : ", b)
#===================================================
#4 - Cree un método llamado testPrimo() en la clase cálculo para probar la primalidad de un entero dado. Pruebe este método.
def testPrimo():
    num=int(input("Ingres un numero: "))
    if num>1:
        for i in range (2,num):
            resto=num%i
            if resto==0:
                cont =+ 1
        if cont == 0:
            print("El {} es un numero primo ".format(num))
        else:
            print("El {} es un numero primo ". format(num))
    else:
        print("El {} no es un numero primo ". format(num))
#===================================================
#4 - Crear un método llamado testPrimos() que permita probar si dos números son primos entre ellos.
def testPrimos():
    n1 = int(input("Ingrese el primer numero"))
    n2= int (input("Ingrese el segundo numero"))
    if n1>0 and n2>0 and n1!=n2:
        if n2>n2:
            n1^=n2
            n2^=n1
            n1^=n2
        for i in range (n1,n2+1):
            print(i)
            creciente=2
            esPrimo=True
            while esPrimo and creciente<i:
                if i%creciente ==0:
                    esPrimo = False
                else: 
                    creciente+=1
            if esPrimo:
                print("El numero es primo")
    else:
        if n1==n2:
            print("Los numeros son iguales")
        else:
            print("Los numeros no son correctos")
#===================================================
#5 - Cree un método tableMult() que cree y muestre la tabla de multiplicar de un entero dado. 
# Luego cree un método TablaMultiplicar() para mostrar todas las tablas de multiplicar de enteros 1, 2, 3, ..., 9.
def tableMulti():
    numMulti=int(input("Ingrese un numero para sacar la tabla"))
    print("La tabla de multiplicar es la siguiente")
    for i in range (1,numMulti+1):
        multipli=numMulti+i
        print(str(numMulti)+ " x "+ str(i)+ " = "+ str(multipli))
        

#impresion
#Factorial()
#Suma()
#testPrimo()
#testPrimos()
tableMulti()