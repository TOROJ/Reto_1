def sumatoria_sucesiva(a):         # lista de enteros
    if int(len(a))>=2:             # rango minimo requerido, 2 elementos
        primer=a[0]+a[1]           # sumatoria de los dos primeros elementos
        max=primer
        Lista=int (len(a))         # simplifico la informacion
        for i in range (1,Lista):  # rango desde el elemento 1 hasta el final
            int(a[i])              # elemento 1 *i
            int(a[i-1])            # elemento 0 *i
            x=a[i]+ a[i-1]         # sumatoria de elemento 0 *i +1 *i
            if x> max:             # posibilidad que la sumatoria actual sea mayor que la sumatoria anterior
                max=x              # si es mayor significa que por ahora es la maxima suma
#            print ( "sumatoria de elementos",a[i]," y ", a[i-1], "igual ", x)              # salida de sumatoria #opcional
        total= (f"La sumatoria Maxima es {max}") 
    else:
        total= "No se encontraron parejas validas en la lista"     
    return total

def main ():                   # poner a prueba
   a=[2,7,7,7,7,7,3,4,5,6,7,8,9,0,12,-12,-32,-6,2,1,2]
   print (sumatoria_sucesiva(a))

if __name__ == "__main__":
   main ()
   