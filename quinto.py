def lista_letras_iguales(a): 
    b=[]                                 # lista donde se almacenaran los datos
    for i in range (len (a)):            # elemtos A
        a1= str(a[i])                    # combierte los datos en strings
        for j in range (i+1, len(a)):    # elementos A'
            a2= str(a[j])                # combierte los datos en strings
#           print (p,a[j])   
            d= sorted (a1)                # orden de letras A
            d1= sorted (a2)              # orden de letras A'
            if d== d1 :                  # si ambas letras son iguales 
                print ("son iguales ", a1, a2)
                b.append(a1)
                b.append (a2)            #las almacena en b

                break
    return (list(set(b)))                # elimina los datos repetidos (si existen)

def main ():                   # poner a prueba
   a=["en ", "roma ", "me ", "comi ", "una ", "mora " ]
   print (lista_letras_iguales(a))

if __name__ == "__main__":
   main ()

            