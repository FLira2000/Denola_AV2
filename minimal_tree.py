class Edge:

   def __init__(self, src, dst, weight):
       self.src = src
       self.dst = dst
       self.weight = weight

class Graph:

    def __init__(self, num_nodes, edgelist):
        self.num_nodes = num_nodes
        self.edgelist  = edgelist
        self.parent = []
        self.rank = []
        # mst guarda todas as arestas da arvore
        self.mst = []

    def FindParent (self, node):
         if node == self.parent[node]:
            return node
         return self.FindParent(self.parent[node])

    def KruskalMST (self):

        # Ordena os objetos da classe Edge baseado no peso (weight) 
        self.edgelist.sort(key = lambda Edge : Edge.weight)

        self.parent = [None] * self.num_nodes
        self.rank = [None] * self.num_nodes

        for n in range(self.num_nodes):
            self.parent[n] = n # Todos os nodes sao pais deles mesmos no comeco
            self.rank[n] = 0

        for edge in self.edgelist:
            root1 = self.FindParent(edge.src)
            root2 = self.FindParent(edge.dst)

            # Os pais de src e dst nao estao no mesmo subset
            # Adiciona a aresta a arvore
            if root1 != root2:
               self.mst.append(edge)
               if self.rank[root1] < self.rank[root2] :
                  self.parent[root1] = root2
                  self.rank[root2] += 1
               else:
                  self.parent[root2] = root1
                  self.rank[root1] += 1

        print("\nArestas minimas para a arvore no grafo:")
        cost = 0
        for edge in self.mst:
            dict_places = {0: "SFO", 1: "LAX", 2: "ORD", 3: "DFW", 4: "JFK", 5: "MIA", 6: "BOS"}

            print("[" + dict_places[edge.src] + " - " + dict_places[edge.dst] + "](" + str(edge.weight) + ")")
            cost += edge.weight
        print("\nCusto minimo da arvore: " +str(cost))

def main():

    SFO = 0
    LAX = 1
    ORD = 2
    DFW = 3
    JFK = 4
    MIA = 5
    BOS = 6
   
    num_nodes = 7
    
    SFO1 = Edge(SFO, LAX, 337)
    SFO2 = Edge(SFO, ORD, 1846)
    SFO3 = Edge(SFO, DFW, 1464)
    SFO4 = Edge(SFO, BOS, 2704)


    LAX1 = Edge(LAX, DFW, 1235)
    LAX2 = Edge(LAX, MIA, 2342)


    ORD1 = Edge(ORD, DFW, 802)
    ORD2 = Edge(ORD, JFK, 740)
    ORD3 = Edge(ORD, BOS, 867)


    DFW = Edge(DFW, MIA, 1121)


    JFK1 = Edge(JFK, MIA, 1090)
    JFK2 = Edge(JFK, BOS, 187)

    MIA = Edge(MIA, BOS, 1258)

    g2 = Graph(num_nodes, [SFO1, SFO2, SFO3, SFO4, LAX1, LAX2, ORD1, ORD2, ORD3, DFW, JFK1, JFK2, MIA])
    g2.KruskalMST()

if __name__ == "__main__" :
    main()
