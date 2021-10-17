#Labirinto AV2

#Caminhos[1,2,6,3,4,17,8,9,7,12,11,18,10,5,
# 25,30,26,32,31,33,19,20,27,24,23,28,34,35,36]

graph = {
    1: [2],
    2: [1, 6, 3],
    6: [2],
    3: [2, 4, 8],
    4: [3, 17],
    17: [4],
    8: [3, 9, 7],
    9: [8],
    7: [8, 12],
    12: [7, 11, 19], 
    11: [12, 18, 10],
    18: [11],
    10: [11, 5, 25],
    5: [10],
    25: [10, 30, 26], 
    30: [25],
    26: [25, 32],
    32: [26, 31, 33],
    31: [32],
    33: [32],
    19: [12, 20],
    20: [19, 28],
    28: [20, 27, 34],
    27: [28, 24],
    24: [23, 27],
    23: [24],
    34: [28, 35],
    35: [34, 22, 36],
    22: [35, 21],
    21: [22, 14, 29],
    29: [21],   
    14: [21, 13],
    13: [14, 15],
    15: [13, 16],
    16: [15],
    36: [35]
}
#variaveis globais

contIn = 0 #contador da profundidade das vezes que as arestas entraram na pilha
contOut = 0 #contador da profundidade das vezes que as arestas sairam da pilha
contInOut = {}
arest = {}
NearRoot = {} #NR e o mais proximo da raiz (root)  do grafo
root = {} #raiz do grafo
levels = {}
demarkers = {}
articulators = {}
visited = set()

def deepSearchLabyrinth(graph, visited, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for nearRoot in graph[node]:
            deepSearchLabyrinth(graph, visited, nearRoot)

deepSearchLabyrinth(graph, visited, 36)

# def CallRecursiveDfs(graph, vertex, level):
#     global contIn, contOut, contInOut
#     contIn += 1
#     contInOut[vertex] = [contIn, None]
#     level[vertex]
#     countSons = 0
#     for nextMove in graph.get(vertex):
#         if not contInOut.get(nextMove):
#             root[nextMove] = arest
#             countSons += 1
#             print('aresta', arest)
#             if levels[NearRoot[nextMove]] < levels[NearRoot[vertex]]:
#                 NearRoot[vertex] = NearRoot[nextMove]
#             if nextMove in demarkers:
#                 articulators.add(vertex)
#         else:
#             if not contInOut[vertex][1]:
#                 if root[vertex] != nextMove:
#                     print('retorno para', root[vertex])
#                     if levels[nextMove] < levels[NearRoot[vertex]]:
#                         root[vertex] = nextMove
#                 else:
#                     arest = [(vertex, nextMove)]
#                     print('aresta')
#         contInOut += 1
#         if root[vertex] in (vertex, root[vertex]):
#             demarkers.add(vertex)
#             return countSons
