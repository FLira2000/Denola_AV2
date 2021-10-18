from os.path import isfile

class Graph():
        def __init__(self, filepath):
                if isfile(filepath):
                        with open(filepath, 'r') as file:
                                content = file.read().split('\n')
                                text_graph = [line.split(';') for line in content]
                                self.graph = [[int(e) for e in l] for l in text_graph]
                                self.V = len(self.graph)
                else:
                        raise Exception('Matriz de adjacências não encontrada.')
        def printMST(self, parent):
                print("Edge \tWeight")
                for i in range(1, self.V):
                        if parent[i] != None:
                                print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

        def minKey(self, key, mstSet):
                min = float('inf')
                for v in range(self.V):
                        if key[v] != None and key[v] < min and mstSet[v] == False:
                                min = key[v]
                                min_index = v
                return min_index

        def primMST(self):
                key = [float('inf')] * self.V
                parent = [None] * self.V
                key[0] = 0
                mstSet = [False] * self.V
                parent[0] = -1
                for cout in range(self.V):
                        u = self.minKey(key, mstSet)
                        mstSet[u] = True

                        for v in range(self.V):
                                if self.graph[u][v] != None:
                                        if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                                                key[v] = self.graph[u][v]
                                                parent[v] = u
                                                self.printMST(parent)
