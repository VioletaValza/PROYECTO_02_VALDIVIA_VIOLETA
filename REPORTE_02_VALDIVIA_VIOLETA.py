# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:11:46 2020

@author: Violeta
"""

# //////////////////////////////////////////////////////////////////////////////

# #Descripción del problema

# La Dirección de Synergy Logistics ha solicitado al equipo operativo, realizar
# una propuesta que permita enfocar las prioridades de la estrategia operativa
# 2021; para ello, se plantea analizar la viabilidad de 3 opciones de enfoque:
# rutas de importación y exportación, medio de transporte utilizado y valor total
# de importaciones y exportaciones.

# Es por ello, que se solicita realizar un análisis detallado que permita
# identificar cuál de las opciones es más viable como base de estrategia.


# Autora: Violeta Gpe. Valdivia Zaragoza
#///////////////////////////////////////////////////////////////////////////////



# #Declaración de variables globales
# Variables que se utilizarán para validar el menú
# Bandera inicializada en falso
validar_menu_prin = 0

# creación de lista vacia la cual almacenará durante cada iteración una nueva lista es decir, sera una lista anidada.
# contendra los valores del archivo csv
lista_datos = []





# importar archivo csv
import csv


# Permitirá importar  o abrir el archivo synergy_logistics_database.csv en modo lectura
with open("synergy_logistics_database.csv", "r")as archivo_database:


    # permitira iterar linea por linea la información y crear una lista de lista
    reader1 = csv.reader(archivo_database)

    # Se hará una iteración de la lista reader para obtener los datos que se encuentran en cada línea del archivo
    for linea in reader1:


        # Cada que se haga la iteración se iran guardando los datos encontrados en lista_datos
        lista_datos.append(linea)




#///////////////////////////////////Parte 1 //////////////////////////////////////////////////

#Creacion de la función rutas_origen
def rutas_origen(destino_ruta):


    #lista vacia que al final contendra los valores ordenados de nombre de ruta, veces que se repitio y el valor monerario
    lista_rutas=[]

    #contendrá los valores de país origen y país destino
    celda_rutas=" "

    #contendrá la suma que se valla generando en el valor total de la lista
    celda_total=0


    #Se hará una iteración en lista_datos
    for ruta in lista_datos:

        #Si ruta en la posicion 1 es igual a destino_ruta entonces...
        if ruta[1]==destino_ruta:


            #celda_ruta es igual a ruta en la posicion 2 y 3
            celda_ruta = [ruta[2],ruta[3]]


            #celda_total es igual al valor de ruta en el indice 9
            celda_total= int(ruta[9])


            #La variable ruta_encontrada se inicializará en False
            ruta_encontrada =False


            #Se realizará una nueva iteración en lista_rutas
            for linea_ruta in lista_rutas:

                #si celda_ruta es igual a linea_ruta en la posición 0 entonces:
                if celda_ruta == linea_ruta[0]:


                    #linea_ruta en el índice 1 se le incrementará un valor
                    linea_ruta[1]+=1

                    #linea_ruta en el índice 2 se igualará a linea_ruta en el indice 2 y se irá sumando los valores que se vallan encontrando
                    linea_ruta[2]= linea_ruta[2]+celda_total


                    #ruta_encontrada se volvera verdadera
                    ruta_encontrada =True


            #Si ruta_encontrada es igual a False entonces...
            if  ruta_encontrada ==False:

               #se añadira el valor encontrado a lista_rutas poniendo primero el nombre de la ruta despues el valor de
               #de veces que se encontro y finalmente la sumatoria del valor monetario
               lista_rutas.append([celda_ruta,1, celda_total ])


    #se retornará la variable lista_rutas
    return lista_rutas



#//////////////////////////////////////// Opción1: Exportaciones ////////////////////////////////////////////////////


#funcion que ordenará y mostrara la lista con las rutas de exportacion más solicitadas
def ruta_export():

    #variable que llevará el conteo de las veces que se mostraran los datos de la lista
    contador_busq_rutas=1

    #lista_rutas sera igual a rutas_origen pero que contengan Exports"
    #Es decir, solo tomara los valores de exportación
    lista_rutas= rutas_origen("Exports")

    #lista_rutas se ordenara de mayor a menor
    (lista_rutas.sort(reverse=True, key=lambda x:x[1]))

    #mensaje para el usuario
    print("----------Listado: Rutas de transporte más utilizadas en Exportaciones---------- \n ")
    print("     Origen - Destino          No.  Valor Monetario ")


    #Se hará una nueva iteración el lista_rutas
    for linea_rutas_tot in lista_rutas:

        #Se imprimirán los datos en pantalla
        print(contador_busq_rutas,linea_rutas_tot, "\n")

        #si el contador es mayor a 10 entonces...
        if contador_busq_rutas >=10:

            #Se detendrá
            break

        #el contador se autoincrementará
        contador_busq_rutas = contador_busq_rutas+1




#//////////////////////////////////////// Opción1: Importaciones ////////////////////////////////////////////////////

#funcion que ordenará y mostrara la lista con las rutas de importacion más solicitadas
def ruta_import():

    #variable que llevará el conteo de las veces que se mostraran los datos de la lista
    contador_busq_rutas=1

    #lista_rutas sera igual a rutas_origen pero que contengan Imports"
    #Es decir, solo tomara los valores de Importación
    lista_rutas= rutas_origen("Imports")

    #lista_rutas se ordenara de mayor a menor
    (lista_rutas.sort(reverse=True, key=lambda x:x[1]))


    #mensaje para el usuario
    print("----------Listado: Rutas de transporte más utilizadas en Importaciones---------- \n ")
    print("     Origen - Destino        No.  Valor Monetario  ")


    #Se hará una nueva iteración el lista_rutas
    for linea_rutas_tot in lista_rutas:

        #Se imprimirán los datos en pantalla
        print(contador_busq_rutas,linea_rutas_tot, "\n")

        #si el contador es mayor a 10 entonces...
        if contador_busq_rutas >=10:

            #Se detendrá
            break

        #el contador se autoincrementará
        contador_busq_rutas = contador_busq_rutas+1





#///////////////////////////////////Parte 2 //////////////////////////////////////////////////

#Creación de la funcion tipo_transp que retornara el parámetro direccion_ruta
def tipo_transp(direccion_ruta):


    #lista vacia que al final contendra los valores ordenados de nombre o tipo de transporte , veces que se repitio y el valor monerario
    lista_transportes=[]


    #contendrá los valores del tipo de transporte
    celda_transporte=" "


    #contendrá la sumatoria de los valores monetarios
    celda_total=0



    # iteración de la lista_datos
    for envio in lista_datos:


        #si envió en la posición 1 es igual a la direccion_ruta entoces...
        if envio[1] == direccion_ruta:


            #Celda_transporte es igual al valor de envió en la posición  7
            celda_transporte = envio[7]


            #celda_total es igual al valor entero de envió en la posición 7
            celda_total=int(envio[9])

            #Transporte encontrado se inicializará en falso
            transporte_encontrado=False



            #Se hará una nueva iteración de lista_transportes
            for linea_transporte in lista_transportes:


                    # Si celda_transporte es igual a lista_transportes en el indice 0 entonces...
                    if celda_transporte == linea_transporte[0]:


                        #lista_transportes en el indice 1 se le incrementará 1
                        linea_transporte[1]+=1


                        #linea_transporte  en el indice 2 se igualará a linea_transporte[2]+ el valor que se tiene en celda_total
                        linea_transporte[2]= linea_transporte[2]+celda_total


                        #transporte_encontrado será verdadero
                        transporte_encontrado=True


            #si transporte_encontrado es igual a falso entonces...
            if transporte_encontrado ==False:

                #Se añadira a lista_transportes el nombre de la ruta, número de veces que se encuentra y el total monetario
                lista_transportes.append([celda_transporte,1,celda_total])


    #print(lista_transportes)
    return lista_transportes



#----------------------------Opción 2: Exportaciones-------------------------------

#Función que realizará el ordenamiento del listado  para exportación a partir de los tipos de transporte
def transp_export():


    #variable que llevará el conteo de las veces que se mostraran los datos de la lista
    contador_busq_trans =1


    #La lista_transportes se igualará al valor "Exports" de tipo_transp_exp
    lista_transportes= tipo_transp("Exports")


    #Los datos de lista_transportes se ordenaran de mayor a menor
    (lista_transportes.sort(reverse=True, key=lambda x:x[2]))


    #mensaje para el usuario
    print("          Listado: Medio de transporte utilizado en Exportaciones ")
    print("-----------------Clasificación por valor monetario----------------\n")
    print("   Tipo  Total  Valor monetario")


    #Se hará una iteración en lista_transportes
    for linea_trans_tot in lista_transportes:

        #se imprimiran los datos de linea_trans_tot adémas del contador
        print(contador_busq_trans,linea_trans_tot,"\n")

        #si el contador es mayor a 3 entonces...
        if contador_busq_trans>=3:

            #se detendrá
            break

        #contador_busq_trans se incrementará uno a uno
        contador_busq_trans =contador_busq_trans +1






#----------------------------Opción 2: Importaciones-------------------------------

#Función que realizará el ordenamiento del listado  para importación a partir de los tipos de transporte
def transp_import():


    #variable que llevará el conteo de las veces que se mostraran los datos de la lista
    contador_busq_trans =1


    #La lista_transportes se igualará al valor "Imports" de tipo_transp_exp
    lista_transportes= tipo_transp("Imports")


    #Los datos de lista_transportes se ordenaran de mayor a menor
    (lista_transportes.sort(reverse=True, key=lambda x:x[2]))

    #mensaje para el usuario
    print("          Listado: Medio de transporte utilizado en Importaciones ")
    print("-----------------Clasificación por valor monetario----------------\n")
    print("   Tipo  Total  Valor monetario")


    #Se hará una iteración en lista_transportes
    for linea_trans_tot in lista_transportes:


        #se imprimiran los datos de linea_trans_tot adémas del contador
        print(contador_busq_trans,linea_trans_tot,"\n")


        #si el contador es mayor a 3 entonces...
        if contador_busq_trans>=3:


            #se detendrá
            break


        #contador_busq_trans se incrementará uno a uno
        contador_busq_trans =contador_busq_trans +1






#//////////////////////////////Opción 3 /////////////////////////////////////////
#////////////////////////////Opción 3: porcentaje de exportaciones



#funcion que sacara el porcentaje de los valores de exportacion
def suma_valores_exp():


    #lista vacia que contendra los valores totales de las exportaciones
    lista_datos_tot=[]

    #La variable valor_unitario es igual a los valores que contengan Exports en rutas_origen
    valor_unitario =rutas_origen("Exports")



    #Se hará una iteracion en la lista valor_unitario
    for line_datos in valor_unitario:

        #se añadira a lista_datos los valores de line_datos en el índice 2
        lista_datos_tot.append(int(line_datos[2]))


    #Se hará la suma de todos los valores de lista_datos
    suma_total=(sum(lista_datos_tot))


    #Se sacará el 80% del valor de suma_total
    porcentaje= ((suma_total*80)/100)


    #Mensaje para el usuario
    print("El valor total de todas las exportaciones es:",suma_total, )
    print("El 80% del valor total es: ",porcentaje,"\n", "\n")







#////////////////////////////////Opción 3: porcentaje importaciones/////////////////////////////////////////

#funcion que sacara el porcentaje de los valores de importacion
def suma_valores_imp():


    #lista vacia que contendra los valores totales de las exportaciones
    lista_datos_tot=[]

    #La variable valor_unitario es igual a los valores que contengan Exports en rutas_origen
    valor_unitario =rutas_origen("Imports")


    #Se hará una iteracion en la lista valor_unitario
    for line_datos in valor_unitario:

        #se añadira a lista_datos los valores de line_datos en el índice 2
        lista_datos_tot.append(int(line_datos[2]))


    #Se hará la suma de todos los valores de lista_datos
    suma_total_imp=(sum(lista_datos_tot))


    #Se sacará el 80% del valor de suma_total
    porcentaje_imp= ((suma_total_imp*80)/100)


    #Mensaje para el usuario
    print("El valor total de todas las Importaciones es:",suma_total_imp )
    print("El 80% del valor total es: ",porcentaje_imp,"\n")








# ////////////////////////////////// Menú  //////////////////////////////////

# Mensaje para el usuario
print("-----------------------Menú Principal----------------------- \n")


# Mensaje que mostrará las opciones del menú
print("Elige un número de las siguientes opciones:\n")
print("Opción 1 Rutas de importación y exportación.")
print("Opción 2 Medio de transporte utilizado.")
print("Opción 3 Valor total de importaciones y exportaciones.\n")


# Se le pedira al usuario ingresar una opción
opcion_menu_principal = input("Seleccionaste la opción: ")


# Validar que los datos ingresados son verdaderos en el menu principal
while validar_menu_prin != 1:



    # ////////////////////////////////OPCIÓN 1 Menú //////////////////////////////////////

    # si la opción seleccionada es 1 entonces...
    if opcion_menu_principal == "1":

        # Se mandará llamar ala función transp_export que mostrará la lista con las rutas de mayor exportación
        ruta_export()


        # Se mandará llamar ala función  ruta_import que mostrará la lista con las rutas de mayor importación
        ruta_import()


        # La bandera se pondra en verdadero validando los datos ingresados en la opción menú
        validar_menu_prin = 1




    # ////////////////////////////////OPCIÓN 2 Menú //////////////////////////////////////

    # Si la opción seleccionada es 2 entonces
    elif opcion_menu_principal == "2":

        #Se mandará llamar la funcion transp_export para mostrar los datos del medio de transporte mas utilizado y el
        #que genera mayor valor monetario en las exportaciones
        transp_export()


        #Se mandará llamar la función transp_impor para mostrar los datos del medio de transporte mas utilizado y el
        #que genera mayor valor monetario en las importaciones
        transp_import()


        # La bandera para validar el menú se pondra en verdadero
        validar_menu_prin = 1






    # ////////////////////////////////OPCIÓN 3 Menú//////////////////////////////////////
    elif opcion_menu_principal == "3":

        #Se mandará llamar la funcion suma_valores_exp
        suma_valores_exp()


        #Se mandará llamar la funcion suma_total_imp
        suma_valores_imp()


        # La bandera se pondra en verdadero
        validar_menu_prin = 1



    else:
        print("OPCIÓN NO VALIDA\n")

        # Mensaje para el usuario
        print("-----------------------Menú Principal----------------------- \n")

        # Mensaje que mostrará las opciones del menú
        print("Elige un número de las siguientes opciones:\n")
        print("Opción 1 Rutas de importación y exportación.")
        print("Opción 2 Medio de transporte utilizado.")
        print("Opción 3 Valor total de importaciones y exportaciones.\n")

        # Se le pedira al usuario ingresar una opción
        opcion_menu_principal = input("Seleccionaste la opción: ")

















