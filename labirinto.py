#Labirinto AV2

#Caminhos[1,2,6,3,4,17,8,9,7,12,11,18,10,5,
# 25,30,26,32,31,33,19,20,27,24,23,28,34,35,36]

graph = {
    1: [2],
    2: [1, 6, 3],
    6: [],
    3: [2, 4, 8],
    4: [3, 17],
    17: [],
    8: [3, 9, 7],
    9: [],
    7: [8, 12],
    12: [7, 11, 19], 
    11: [12, 18, 10],
    18: [],
    10: [11, 5, 25],
    5: [],
    25: [10, 30, 26], 
    30: [],
    26: [25, 32],
    32: [26, 31, 33],
    31: [],
    33: [],
    19: [12, 20],
    20: [19, 28],
    28: [20, 27, 34],
    27: [28, 24],
    24: [23, 27],
    23: [],
    34: [28, 35],
    35: [34, 22, 36],
    22: [35, 21],
    21: [22, 14, 29],
    29: [],   
    14: [21, 13],
    13: [14, 15],
    15: [13, 16],
    16: [],
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


def deepSearchLabyrinth(graph, visited, node):
    if node not in visited:
        visited.append(node)
        removeFromStack = True
        for nearRoot in graph[node]:
            deepSearchLabyrinth(graph, visited, nearRoot)
            removeFromStack = False
            break
        if removeFromStack:
            visited.pop()
        return visited

visited = deepSearchLabyrinth(graph, [] , 36)
visited.reverse()
print(visited)