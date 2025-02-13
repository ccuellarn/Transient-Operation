# # -*- coding: utf-8 -*-
# """
# Created on Sun May 22 16:59:25 2022

# @author: aleja
# """
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# import matplotlib.image as mpimg

# #PUNTO 0
# def cargar_datos(nombre_archivo:str)->pd.DataFrame:
#     """
#     Recibirá el nombre del archivo del cual se realizará el análisis para cargar los datos
#     en un formato que permita el programa.
#     ----------
#     PARÁMETROS:
#     nombre_archivo : str
#         nombre del arcivo con el formato: 'nombre.csv'. 
#     -------
#     Retorna el DataFrame del archivo.
#     """
#     datos = pd.read_csv(nombre_archivo)
#     return datos

# #PUNTO 1
# def diagrama_de_torta_segun_tipo_de_estacion(datos: pd.DataFrame)->None:
#     """
#     Esta función requiere de un DataFrame en donde se encontrarán los datos generales.
#     ----------
#     PARÁMETROS:
#     datos : pd.DataFrame
#         Se usa la función de cargar_datos para crear el DataFrame del parámetro.
#     -------
#     Retorna la distribución de los tipos de estaciones de medición de las variables 
#     climatológicas en una gráfica de pie o de torta.
#     """
#     #Análisis y separación de las columnas del DataFrame
#     columnas = ['Nombre de la estación','Tipo de estación']
    
#     #eliminamos duplicados
#     estaciones = datos[columnas].drop_duplicates()
    
#     #separamos pr tipo de estacion y contamos cuantos hay de cada tipo
#     punto1 = estaciones['Tipo de estación'].value_counts()
    
#     #Detalles de forma y color de la gráfica.
#     pie_colors = ['tab:orange', 'tab:cyan']
#     plt.figure(facecolor='navajowhite')
    
#     #Plot de la gráfica
#     punto1.plot.pie( autopct='%1.1f%%',ylabel='    ', shadow=True, colors=pie_colors)
#     plt.title("Tipo de estación.")
#     plt.show()

# #PUNTO 2
# def tendencia_medidas_por_rango_de_anios(datos: pd.DataFrame, limite_inf: int, limite_sup:int)->None:
#     """
#     Recibe un DataFrame y el usuario ingresa un límite inferior y un límite superior 
#     para determinar el intervalo de años que desea visualizar, el cual se mostrará en un
#     diagrama de lineas.
#     ----------
#     PARÁMETROS:
#     datos : pd.DataFrame
#         Se usa la función de cargar_datos para crear el DataFrame del parámetro.
#     limite_inf : int
#         Año inferior o del cual se iniciará el análisis. Debe ser en forma de entero.
#     limite_sup : int
#         Año superior o del cual se finalizará el análisis. Debe ser en forma de entero.
#     -------
#     Retorna el número de medidas realizadas en el rango de años en un diagrama de líneas.
#     """
#     #Análisis y separación de las columnas del DataFrame 
#     df = datos[["Anio"]]
    
#     #separamos por años para que coincidieran con los limites dados
#     anios_cheveres = df[ (df["Anio"] >= int(limite_inf)) & (df["Anio"] <= int(limite_sup))]
    
#     #contamos cuantos hay de cada uno y los organizmos
#     x2= anios_cheveres["Anio"].value_counts().sort_index()
    
#     #Detalles de forma y color de la gráfica.
#     plt.figure(facecolor='navajowhite')
    
#     #Plot de la gráfica
#     plt.plot(x2,'go-', linewidth=2.0)
#     plt.title(
#     "Tendencia del número de medidas realizadas en el rango de {0} y {1} años."
#     .format(limite_inf,limite_sup))
#     plt.xlabel('Años')
#     plt.ylabel('Número de medidas')
#     plt.show()

# #PUNTO 3
# def diagrama_de_barras_mediciones_o3_mayores_a(datos: pd.DataFrame, con_ingresada: float)->None:
#     """
#     Recibe un DataFrame y el valor de una concentración sobre la cual se realizará el 
#     análisis.
#     ----------
#     PARÁMETROS:
#     datos : pd.DataFrame
#         Se usa la función de cargar_datos para crear el DataFrame del parámetro.
#     con_ingresada : float
#         Es la concentración de O3 ingresada por el usuario en el formato de 
#         'cantidad 𝜇𝑔/𝑚3'.
#     -------
#     Retorna un diagrama de barras horizontal para la concentración ingresada.
#     """
#     #Análisis y separación de las columnas del DataFrame 
#     columnas = ["Departamento", "Variable", "Concentración"]
#     df3 = datos[columnas]
    
#     #se separó para que coincidiera con la variable O3
#     filtro1 = df3[df3['Variable']=='O3']
    
#     #se separó para que coincidiera con el número de la concentración ingresada
#     filtro2 = filtro1[ filtro1["Concentración"] >= float(con_ingresada) ]
    
#     #se agrupó por departamentos para realizar el conteo y solo seleccionar los 5 primeros.
#     x3 = filtro2["Departamento"].value_counts().head()
    
#     #Se ordenó de mayor a menor
#     x3 = x3.sort_values(ascending=True)
    
#     #Detalles de forma y color de la gráfica.
#     plt.figure(facecolor='navajowhite')
#     plot_colors = ['tab:orange', 'tab:cyan', 'tab:green', 'tab:blue', 'tab:red']
    
#     #Plot de la gráfica
#     x3.plot(kind='barh', color=plot_colors)
#     plt.title('Top departamentos con medidas superiores a {0} 𝜇𝑔/𝑚3'.format(con_ingresada))
#     plt.xlabel('Departamento')
#     plt.ylabel('Número de medidas superiores a {0} µg/m³'.format(con_ingresada))
#     plt.show()
    
# #PUNTO 4
# def caja_y_bigotes_distribucion_concentraciones_CO_por_año(datos: pd.DataFrame, anio_i: int)->None:
#     """
#     Recibe un DataFrame y un año sobre la cual se realizará el análisis de concentraciones
#     de CO. Se utilizó únicamente las mediciones con un tiempo de exposición igual a 8.
#     ----------
#     PARÁMETROS:
#     datos : pd.DataFrame
#         Se usa la función de cargar_datos para crear el DataFrame del parámetro.
#     anio_i : int
#         Año sobre el cual se realizará el análisis en formato de número de entero.
#     -------
#     Retorna la distribución de las concentraciones de CO para un año ingresado por 
#     parámetro en un diagrama de caja y bigote o 'boxplot'.
#     """
#     #Análisis y separación de las columnas del DataFrame 
#     columnas=[ 'Anio', "Concentración","Variable"]
#     df4 = datos[columnas]
    
#     #se separó por concentración de CO
#     filtro0= df4[df4['Variable']=='CO']
    
#     #Se clasificó por el año ingreasdo y se ordenó por la columna de concentracion
#     filtro2 = filtro0[filtro0['Anio']==int(anio_i)].sort_values('Concentración')
    
#     #Dada la columna concentracion se realizo el conteo de quartiles.
#     promedio = pd.DataFrame(filtro2['Concentración'])
    
#     #Detalles de forma y color de la gráfica.
#     plt.figure(facecolor='navajowhite')
    
#     #Plot de la gráfica
#     promedio.boxplot(figsize=(5,8))
#     plt.title("Distribución de medidas de CO por un año.")
#     plt.xlabel('{0}'.format(anio_i))
#     plt.ylabel('Concentración')
#     plt.show()


# #PUNTO 5
# def concentraciones_anuales_PM10_por_departamento(datos: pd.DataFrame, departa: str)->None:
#     """
#     Recibe un DataFrame y el nombre de un departamento para identificar las 
#     concentraciones promedio anuales de material particulado menor a 10 
#     micras (PM10).
#     ----------
#     PARÁMETROS:
#     datos : pd.DataFrame
#         Se usa la función de cargar_datos para crear el DataFrame del parámetro.
#     departa : str
#         Nombre del departamento en formato str y totalmente en mayúsculas.
#     -------
#     Retorna un gráfico de barras dónde están la cantidad de concentraciones anuales
#     de dicho departamento.
#     """
#     #Análisis y separación de las columnas del DataFrame 
#     columnas=['Departamento', 'Variable', "Concentración",'Anio']
#     df5 = datos[columnas]
    
#     #se separó por el departamento ingresado
#     departam=departa.upper()
#     filtro1 = df5[df5['Departamento']==departam]
    
#     #se organizo excluyendo las variables de 10 micras
#     filtro2 = filtro1[filtro1['Variable']=='PM10']
    
#     #se agrupo por años
#     filtro3= filtro2.groupby(['Anio'])
    
#     #dada la columna de concentracion se sacó el promedio
#     filtro4= filtro3['Concentración'].mean()
    
#     #Detalles de forma y color de la gráfica.
#     plt.figure(facecolor='navajowhite')
#     plot_colors = ['tab:orange', 'tab:cyan', 'tab:green', 'tab:blue', 'tab:red']
    
#     #Plot de la gráfica
#     filtro4.plot(kind='bar',color=plot_colors)
#     plt.title("Concentración promedio de material particulado menor a 10 micras en {0}.".format(departa))
#     plt.ylabel('Concentración')
#     plt.xlabel('Año')
#     plt.show()
    
    
# #PUNTO 6
# def crear_matriz(datos:pd.DataFrame)-> list:
#     """
#     Recibe un DataFrame sobre el cual retornará la información acerca de los departamentos, ICAs e
#     información de las filas y columnas de la matriz.
#     ----------
#     PARÁMETROS:
#     datos : pd.DataFrame
#        Se usa la función de cargar_datos para crear el DataFrame del parámetro.
#     -------
#     Retorna la matriz con la informacion de concentracion organizadas por departamentos e ICAs.
#     Cada posición (f,c) en la matriz contiene el número de medidas tomadas que pertenecen al 
#     departamento f y que tiene la calidad c (Buena, Aceptable, etc.). Por ejemplo, si Amazonas está 
#     en la fila 1 y Aceptable en la columna 3, el número de medidas aceptables en el departamento 
#     de Amazonas sería el valor en la casilla (1,3).
#     """
#     #Esqueleto diccionarios
#     ICAs =sorted(datos["ICA"].unique())
#     #Diccionario con el nombre de las columnas (ICA)
#     ICAs_dict = dict(list(enumerate(ICAs)))
#     deptos = sorted(datos["Departamento"].unique())
#     #Diccionario con el nombre de las filas (Deptos)
#     dept_dict = dict(list(enumerate(deptos)))
    
#     #Establecer valores de las filas
#     filas= len(deptos)
#     columnas = len(ICAs)
    
#     #Establecer columnas del dataframe
#     colum= ["ICA","Departamento",'Concentración']
    
#     #Crear matriz vacia
#     matriz=[]
#     for i in range(0, filas):
#         y=[0]*columnas
#         matriz.append(y)
        
#     #Recoorido de la matriz vacía.
#     for i in range(0, filas):
#         for j in range(0, columnas):
#             #Cargamos el dataframe
#             df6 = datos[colum]
            
#             #establecemos variables para el nombre del departamento/fila
#             #y para el ICA/columna
#             filanombre= deptos[i]
#             colnombre= ICAs[j]
            
#             #buscamos en el dataframe la columna y fila.
#             df6= df6[df6["ICA"]==colnombre]
#             df6= df6[df6["Departamento"]==filanombre]
            
#             #el valor sera el conteo de cuantas concentraciones hay con esos
#             #parametros, si no tiene será cero.
#             valor= df6['Concentración'].count()
            
#             #añadir a matriz en esa posicion
#             matriz[i][j]=valor
            
#     #retornamos en forma de tupla
#     return (matriz, dept_dict, ICAs_dict)

# #PUNTO7
# def dar_departamento_con_mas_mediciones(m:tuple)->str:
#     """
#     Encuentra el departamento que ha registrado la mayor cantidad de mediciones sin 
#     importar la calidad del ICA registrado en la medición.Parameters
#     ----------
#     PARÁMETROS:
#     m : tuple
#         Tupla con el formato de la función crear_matriz.
#     -------
#     Retorna el nombre del departamento con mayor número de mediciones.
#     """
#     #Se separa de la tupla la matriz, y el diccionario de departamentos
#     matriz1=m[0]
#     dept_dict = m[1]
    
#     #se establece el numero de filas
#     filas=len(matriz1)
#     mayor=matriz1[0][0]
    
#     #se recorre unicamente por filas usando max para hallar el mayor
#     for i in range(1, filas):
#         may=max(matriz1[i])
#         if may>mayor:
#             #el indice del mayor sera en donde estamos recorriendo
#             mayor=may
#             fila=i
            
#     #se busca el departamento en el diccionario dado
#     nombre_dep= dept_dict[fila]
    
#     return nombre_dep
    
# #PUNTO 8
# def contar_numero_de_mediciones_por_ica_dado(m:tuple, ica:str)->int:
#     """
#     Calcula el número total de mediciones que tienen una clasificación ICA específica.
#     ----------
#     PARÁMETROS:
#     m : tuple
#         Tupla con el formato de la función crear_matriz.
#     ica : str
#         Clasificación ICA para la cual desea obtener el número total de mediciones,
#         en formato de mayúsculas.
#     -------
#     Retorna un entero que representa el número de mediciones que son clasificadas en 
#     la categoría ingresada.
#     """
#     #Se separa de la tupla la matriz
#     matriz=m[0]
#     filas=len(matriz[0])
#     ICAs_dict=m[2]
    
#     #se recorre el diccionario de icas buscando la ingresada y su indice
#     for cada in ICAs_dict:
#         if str(ICAs_dict[cada])==ica:
#             indice=cada
            
#     #recorremos la matriz para sumar los valores que coincidan con
#     #la posicion del ica        
#     suma=0
#     for i in range(0, filas):
#         suma+=int(matriz[i][indice])
        
#     return suma

# #PUNTO 9
# def mayores_mediciones_ica_y_departamento(m:tuple)->tuple:
#     """
#     Calcula la fila y la columna en donde se registró el mayor número de 
#     mediciones dentro de toda la matriz dada por parámetro.
#     ----------
#     PARÁMETROS:
#     m : tuple
#         Tupla con el formato de la función crear_matriz.
#     -------
#     Retorna una tupla de la forma (d,g), donde d es el nombre del departamento y 
#     g es el ICA.
#     """
#     #Se separa de la tupla la matriz, el diccionario departamentos e ICA
#     matriz2=m[0]
#     dept_dict = m[1]
#     ICAs_dict = m[2]
#     filas=len(matriz2[0])
#     mayor=matriz2[0][0]
#     fila=0
#     columna=0
    
#     #se recorre la matriz en busca del mayor
#     for i in range(1, filas):
#         may=max(matriz2[i])
#         if may>mayor:
#             mayor=may
            
#             #se establecen los indices de fila y columna para el mayor
#             fila = i
#             columna = matriz2[i].index(mayor)
            
#     #se busca en los diccionarios y se retorna en forma de tupla
#     nom_ica= ICAs_dict[columna]
#     nombre_dep= dept_dict[fila]
#     tupla=(nombre_dep,nom_ica)
    
#     return tupla
    
# #FUNCION AUXILIAR PUNTO 10
# def cargar_coordenadas(nombre_archivo:str)->dict: 
#     """
#     Función auxiliar de la función mayores_mediciones_ica_y_departamento para
#     cargar el archivo de coordenadas a usar.
#     ----------
#     PARÁMETROS:
#     nombre_archivo : str
#         Nombre del archivo, para este caso será 'coordenadas.txt', ya que 
#         fue el dado en el esqueleto del proyecto.
#     -------
#     Retorna un diccionario, cuyas llaves son los nombres de los departamentos y
#     los valores son tuplas con las coordenadas (x,y) de cada departamento.
#     """
#     #fiuncion dada en el esqueleto del proyecto
#     deptos = {}
#     archivo = open(nombre_archivo, encoding="utf8")
#     archivo.readline()
#     linea = archivo.readline()
#     while len(linea) > 0:
#         linea = linea.strip()
#         datos = linea.split(";")
#         deptos[datos[0].upper()] = (int(datos[2]),int(datos[1]))
#         linea = archivo.readline()
#     return deptos

# #PUNTO 10
# def departamentos_mapa(m:tuple)->None:
#     """
#     Determina cuál fue la clasificación ICA que tuvo un mayor número de mediciones
#     en cada departamento. Por ello se muestra la información sobre un mapa de Colombia
#     dónde cada clasificación tiene su propio color.
#     ----------
#     PARÁMETROS:
#     m : tuple
#         Tupla con el formato de la función crear_matriz.
#     -------
#     Retorna el mapa de Colombia con la información de las clasificaciones.
#     """
#     #funcion 10
#     #Declaramos las variables de la tupla a usar y el diccionario de colores dado en el esqueleto.
#     colores = {"Buena":[36/255,226/255,41/255], "Aceptable":[254/255,253/255,56/255], 
#     "Dañina a la salud de grupos sensibles":[252/255,102/255,33/255],
#     'Dañina a la salud':[252/255,20/255,27/255], 'Muy dañina a la salud':[127/255,15/255,126/255], 
#     "Peligrosa":[101/255, 51/255, 8/255]}
#     matriz=m[0]
#     dept_dict = m[1]
#     ICAs_dict = m[2]
#     filas=len(matriz)
#     de = list(dept_dict.values())
#     #Diccionario vacio para guardar las coordenadas y colores que se necesitan
#     graficar={}

#     #Se recorre buscando el mayor por departamento/fila
#     for i in range(0, filas):
#         mayor=int(max(matriz[i]))
        
#         #ica será el indice en donde está el mayor y se busca en el diccionario
#         #de ica, con el indice de la fila se busca el departamento en el diccionario
#         ica= matriz[i].index(mayor)
#         nom_ica= ICAs_dict[ica]
#         nombre_dep= dept_dict[i]
        
#         #Establebecemos las variables de coordenada y el color para guardarlas en el 
#         #diccionario vacío, y se usa la funcion auxiliar para el diccionario de
#         #coordenadas
#         coor=None
#         color=None
#         coordenadas_buscar= cargar_coordenadas('coordenadas.txt')
        
#         #Se recorre el dicccionario para hallar las coordenadas
#         for cada in coordenadas_buscar.keys():
#             if cada==nombre_dep:
#                 coor=coordenadas_buscar[cada]
#             for cada1 in colores.keys():
#                 if cada1==nom_ica:
#                     color=colores[cada1]
#                     # donde i es el indice del departamento, coor la coordenada
#                     #y el color en rgb
#                     graficar[de[i]]=[coor, color]
    
#     a = plt.figure(figsize=(8,8))
#     axd = a.add_subplot()
    
#     for algo in dept_dict.values():
#         xd=mpatches.Rectangle(graficar[algo][0], 13, 13, facecolor=graficar[algo][1])
#         axd.add_patch(xd)
    
#     legends = []
#     for i in range(len(matriz[0])):
#         legends.append(mpatches.Patch(color = colores[m[2][i]], label = m[2][i]))
        
#     plt.legend(handles = legends, loc = 3, fontsize='x-small')
#     mapa = mpimg.imread('mapa.png').tolist()
#     plt.imshow(mapa)
#     plt.show()
    
    