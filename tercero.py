def lista_primos(a):
    c=[]                       # lista donde se almacenera los datos
    p="no es valido"           # caso el cual se encuentre un error
    for j in range (len(a)):   
        numero= int(a[j])           # enteros de cada lista
        if numero>2:                # selecion de primos o no
            for i in range (2,numero):
                sol= numero % i
                #print (f" {x} % {i } = {sol}", si sol = 0 =no primo  formula para hayar primos
                if sol == 0:
                    p= "no es primo" 
                    break

                else :
                    
                    p= "es primo"
            # print (b)
        elif numero==1 or numero==0:
            p= "no es primo"
        elif numero==2:
            p= "es primo"
        else:
            p= "es negativo"

        #print ("El elemento " ,numero, b)  #opcional  indica dato a dato cual es o cual no
        if p == "es primo":
            p=numero
            c.append (p)

#    ordenado=sorted (c)   #lo ordena de mayor a menor numero de primos aunque es opcional
#    c= ordenado 
    return c 

def main ():                   # poner a prueba
   a=[2,7,7,7,7,7,3,4,5,6,7,8,9,0,12,-12,-32,-6,2,1,2846]
   print (lista_primos(a))

if __name__ == "__main__":
   main ()



    



