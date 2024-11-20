def palabra_palíndromo(a):
    for i in range (len(a)):
        letra=a[i]      # letra por letra adelante
        i-=-1 
        detras= a[-i]        #letra por letra para atras
        i+=1

        if letra==detras:       #si ambas son iguales
            print (letra)
            z="si es palindromo"
        else:                   #si no
            z= "no es palindromo"
            break
    return z

def main ():                   # poner a prueba
   a=input ("Escribe UNA palabra, y te dire si es palindromo:\n")
   print (palabra_palíndromo(a))

if __name__ == "__main__":
   main ()



