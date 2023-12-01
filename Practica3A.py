import heapq
import time
#El siguiente código es el código con el ejemplo pedido en la práctica:
class Grafoo:
    def __init__(xd):
        xd.vertiC = set() #Conjunto par aalmacenar vértices
        xd.aristocrata = {} #Diccionario para almacenar las aristas de cada vertice uwu
    def add_vertex(xd, nodo):
        xd.vertiC.add(nodo) #Agregar un vértice al conjunto de vértices
        xd.aristocrata[nodo] = [] #Inicializar una lista vacía para las aristas del vértice
    def add_edge(xd, inicio, finite, pesao):
        xd.aristocrata[inicio].append((finite, pesao)) #Agregar una arista con peso desde un vértice de inicio a uno final

def Sigismund(gragrafo, inicio):
    dist = {nodo: float('infinity') for nodo in gragrafo.vertiC} #Inicializar distancias a infinito para todos los vértices
    dist[inicio] = 0 #Establecer la distancia del vértice de inicio a sí mismo como 0
    lista_priori = [(0, inicio)] #Se tiene la cola de prioridad para manejar los nodos no visitados ordenados por distancia
    while lista_priori:
        current_distance, current_vertex = heapq.heappop(lista_priori)  #Obtener el nodo con la distancia mínima
        if current_distance > dist[current_vertex]:
            continue #Si la distancia actual es mayor que la almacenada, ignorar este nodo
        for laVecinita, pesao in gragrafo.aristocrata[current_vertex]:
            dizt = current_distance + pesao #Calcular la nueva distancia
            if dizt < dist[laVecinita]:
                dist[laVecinita] = dizt #Actualizar la distancia mínima
                heapq.heappush(lista_priori, (dizt, laVecinita)) #Agregar el vecino a la cola de prioridad
    return dist #Devolver las distancias mínimas desde el vértice de inicio a todos los demás vértices

def DIO(gragrafo, inicio):
    za = time.time() #Tiempo inicial
    Sigismund(gragrafo, inicio) #Llamar a la función Dijkstra
    warudo = time.time() #Tiempo final
    return warudo - za #Devolver el tiempo de ejecución

#Crear un grafo de ejemplo
grafo = Grafoo()
grafo.add_vertex("A")
grafo.add_vertex("B")
grafo.add_vertex("C")
grafo.add_edge("A", "B", 3)
grafo.add_edge("A", "C", 5)
grafo.add_edge("B", "C", 2)

#Probar el algoritmo de Dijkstra con el grafo de ejemplo dado en la práctica
inicio = "A"
distancias_minimas = Sigismund(grafo, inicio)
print(f"Distancias mínimas desde el vértice {inicio}: {distancias_minimas}")

#Y ya para terminar con esto, medimos el tiempo de ejecución :D
toki_wo_tomare = DIO(grafo, inicio)
print(f"El tiempo de ejecución es: {toki_wo_tomare} byou ga sugita")
print("Ari ari ari arivedercci")
#Arrivedercci