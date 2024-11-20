def operaciones_basicas(): # a y b son numeros, n es el operando
    a= float(input("numero a: "))
    b= float(input ("numero b "))
    n= input ("operación ")

    if n =="+":          # accion de n segun su resultado
       return a + b 
    elif n == "-":
       return a-b
    elif n == "*":
       return(a*b)
    elif n == "/":
       return(a/b)
    else:
       return("Seleccione validamente el operando:\n(+(suma),-(resta),/(division),*(multiplicacion))")
    
    
def main ():                   # poner a prueba
   print (operaciones_basicas())

if __name__ == "__main__":
   main ()






