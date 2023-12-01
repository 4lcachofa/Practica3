import heapq
import time
import random
import matplotlib.pyplot as plt
#Para este código, ya no se usará el ejemplo pedido en la práctica, sino que se usarán muchos grafos aleatorios
#y e graficará su tiempo de ejecución :D

# Definición de la clase para representar el grafo 
class Grafoo:
    def __init__(xd):
        xd.vertiC = set() #Conjunto para almacenar vértices
        xd.aristocrata = {}  #Diccionario para almacenar las arisas de cada vértice 
    def aniadirVertice(xd, nodo):
        xd.vertiC.add(nodo) #Agregar un vértice al conjunto de vértices
        xd.aristocrata[nodo] = [] #Inicializar una lita vacía para las aristas del vértice
    def aniadirArista(xd, inicio, finite, pesao):
        xd.aristocrata[inicio].append((finite, pesao)) #Agregar una aristac on peso desde un vértice de inicio a uno final

#Algoritmo de Dijkstra para encontrar los  caminos mínimos en un grafo ponderado dirigido
def Sigismund(gragrafo, inicio):
    dist = {nodo: float('infinity') for nodo in gragrafo.vertiC} #Inicialaizar distancias a infinito para todos los vértices
    dist[inicio]= 0 #Establecer la distancia del vértice de inicio a sí mismo como 0
    lista_priori =[(0, inicio)] #Cola de p rioridad para manejar los nodos no visitados ordenados por distancia
    
    while lista_priori:
        current_distance, current_vertex = heapq.heappop(lista_priori) #Obtener el nodo con la distancia mínima
        if current_distance > dist[current_vertex]:
            continue #Si la distancia actual es mayor que la almacenada, ignorar este nodo
        for laVecinita, pesao in gragrafo.aristocrata[current_vertex]:
            dizt = current_distance + pesao #Calculr la nueva distancia
            if dizt < dist[laVecinita]:
                dist[laVecinita] = dizt #Actualizar la distancia mínima
                heapq.heappush(lista_priori, (dizt, laVecinita)) #Agregar el vecino a la cola de prioridad
    return dist #Devolver las distancias mínimas desde el vértice de inicio a todos los demás vértices

#Función para medir el tiempo y ejecutar el algoritmo en varios grafos aleatorios
def medir_tiempo_y_graficar(NoGrafos, NoVertices, NoAristas):
    tiempoEjecucionuwu = []
    for _ in range(NoGrafos):
        grafo = Grafoo()
        for i in range(NoVertices):
            grafo.aniadirVertice(str(i))
        for _ in range(NoAristas):
            start = str(random.randint(0, NoVertices - 1))
            end = str(random.randint(0, NoVertices - 1))
            weight = random.randint(1, 10)
            grafo.aniadirArista(start, end, weight)
        empezar = str(random.randint(0, NoVertices - 1))
        tiempo_ejecucion = DIO(grafo, empezar)
        tiempoEjecucionuwu.append(tiempo_ejecucion)
        
    #Graficar los tiempos de ejecución
    plt.plot(tiempoEjecucionuwu, marker='o', linestyle='-', color='b')
    plt.title(f'Tiempos de ejecución para {NoGrafos} grafos aleatorios')
    plt.xlabel('Número de grafos')
    plt.ylabel('Tiempo de ejecución (en segundos xd)')
    plt.show()

def DIO(gragrafo, inicio):
    za = time.time() #Tiempo inicial
    Sigismund(gragrafo, inicio) #Llamar a la función Dijkstra
    warudo = time.time() #Tiempo final
    return warudo - za #Devolver el tiempo de ejecución

#Parámetros para la función
NoGrafos=100
NoVertices = 10
NoAristas = 15

#Llamar a la función para medir el tiempo y graficar
medir_tiempo_y_graficar(NoGrafos, NoVertices, NoAristas)
