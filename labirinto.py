#Labirinto AV2

#Caminhos[1,2,6,3,4,17,8,9,7,12,11,18,10,5,25,30,26,32,31,33,19,20,27,24,23,28,34,35,36]
#Caminho correto = [1, 2, 3, 8, 7, 12, 19, 20, 28, 34, 35, 36]
#grafo
graph = {
    1: [2],
    2: [1, 3 ,6],
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

#A funcao eh o algoritmo de busca profunda recursiva
def deepSearchLabyrinth(graph, visited, node):
    if node not in visited:
        removeFromStack = True
        visited.append(node)
        for nearRoot in graph[node]:
            deepSearchLabyrinth(graph, visited, nearRoot)
            if node in visited:
                removeFromStack = False
            break #encontra a saida
        if removeFromStack:
            visited.pop()
    return visited

visited = deepSearchLabyrinth(graph, [] ,36)
visited.reverse()
print(visited)