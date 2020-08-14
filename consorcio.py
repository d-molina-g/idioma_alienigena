#Autor: David Molina Garrido
#Algoritmo Alienigenas

def prueba():
    print("Hola a todos!")

def analizar_palabra(palabra, largo):
    #Si la palabra es de largo l, si está escrita en minúsculas y es alfabética; está correcta.
    if len(palabra) == largo and palabra.islower() and palabra.isalpha(): 
        return True
    else:
        return False

def solicitar_palabra():
    palabra = input() #Solicitamos la palabra
    
    if analizar_palabra(palabra,l): #Analizamos si la palabra cumple las condiciones
        #print("Cumple!... es de longitud l y está en  minúsculas")
        return palabra
    else:
        print("Ingrese correctamente la palabra en el idioma alienígena")
        solicitar_palabra()  #Solicitamos de nuevo la palabra (recursión)

#Con esta función colocamos en una lista los caracteres del patron que debe tener la palabra
def lista_patron(patron, iter, patron_list):    
    i=iter #Recibe el indice del patrón
    conjunto="" #Almacenar el conjunto de caracteres que está dentro de los parentesis
    
    #Si no está entre parentesis, agregamos ese caracter a la lista
    while i<len(patron) and patron[i]!='(' : 
        
        patron_list.append(patron[i])
        #print("Parentesis")
        #print(patron_list)
        i=i+1
    
    #Añadimos los caracteres que están dentro del parentesis
    if (i<len(patron) and patron[i]=='('): 
        i=i+1
        
        while(i<len(patron) and patron[i]!=')'):
            conjunto = conjunto + patron[i]
            i=i+1

        i=i+1 #Para añadir el caracter ')'
        patron_list.append(conjunto) #Añadimos el bloque de caracteres a la lista
        #print(patron_list)

    #Si tiene más de un bloque de parentesis, se vuelve a llamar a la función (recursividad)
    if i < len(patron):
        lista_patron(patron, i, patron_list)



    #retornamos la lista de patrones ... que contiene una lista de los caracteres válidos
    return patron_list






#Realizamos el conteo de palabras correctas dado los patrones ingresados
def conteo(lista_palabras, lista_patrones):
    lista_aux = [] #Contendrá las apariciones de una palabra según un patron


    #Rellenamos nuestra lista auxiliar con 0's (aquí colocaremos el número de ocurrencias según su indice)
    for i in range(len(lista_patrones)):
        lista_aux.append(0)

    #print(lista_aux)
    #print(lista_patrones)
    
    for patron in lista_patrones:
        for palabra in lista_palabras:
            cont=0 #Cuenta las coincidencias de caracteres (debe ser igual al largo de la palabra, siempre que el patrón ya esté en su ultima posición)

            for (ind,i) in enumerate(palabra, start=0): #Iteramos sobre los caracteres de las palabras y su indice

                #Coincidencia de caracter
                if len(patron[ind])==1 and patron[ind] == i:  
                    cont=cont+1
                
                #Coincidencia de conjunto de caracteres
                elif conjunto(i, patron[ind]): 
                    cont=cont+1

                #No hay coincidencia
                else:
                    break #Si no cumple, sale del ciclo (se itera con otra palabra)
        
            #Si los caracteres coincidieron segun el largo de la palabra y el patron llegó a su fin
            if (cont==len(palabra) and cont == len(patron)): 
                #print(len(patron), ind) #Si las coincidencias fueron igual que el tamaño de la palabra
                #print("Coinciden !!: ",palabra, patron)
                
                if patron in lista_patrones:
                    indice = lista_patrones.index(patron)
                    lista_aux[indice] = lista_aux[indice] + 1   #Colocamos las veces que el patron coincide con la palabra alienigena en la lista auxiliar

    #Retornamos la lista auxiliar que tiene el número de coincidencias por patrón
    return lista_aux
                    
                
    
    #print("Palabras (función conteo): ",lista_palabras)
    #print("Patrones (función conteo):", lista_patrones)



#Veriicar si un caracter está en un conjunto de caracteres ejem: (abc)
def conjunto(letra, conjunto):

    if conjunto.find(letra)>=0: #Si está la letra en el conjunto
        return True
    else:
        return False
        



####Principal#####


try:
        
    l,d,n = input().split() #Se separan por espacio y se asignan las variables
    
    #Cambiamos el tipo de dato a las variables 
    l=int(l) #Longitud de la palabra
    d=int(d) #Cantidad de palabras de longitud l
    n=int(n) #N casos de prueba

except:
    print("Ingrese el formato correcto (3 números enteros separados por espacio)")



if isinstance(l, int) and isinstance(d, int) and isinstance(n, int):
    
    lista_palabras = []
    lista_patrones=[]

    for i in range(d):  #solicitamos d palabras de longitud l

        palabra = solicitar_palabra()  #Solicitamos la palabra
        lista_palabras.append(palabra) #Agregamos la palabra a una lista

    #print("---Patron---")
    for i in range(n):  #solicitamos n patrones
        patron_list=[] #Lista donde se almacenan los patrones dado su posición
        
        patron=input()
        lista_patrones.append(lista_patron(patron,0, patron_list)) #Añadimos la lista generada por la funcion en una lista (lista de listas)


else:
    print("Ingrese el formato correcto (3 números enteros separados por espacio)")

#Mandamos la lista de palabras y patrones para realizar el conteo 
lista_respuesta = conteo(lista_palabras, lista_patrones) 

#Mostramos la respuesta por pantalla
for i in range(len(lista_respuesta)):
    print("Case #",i+1,":",lista_respuesta[i])    



#print("Lista de patrones: ",lista_patrones)
#print("La lista de palabras es: ", lista_palabras)

