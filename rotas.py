from queue import PriorityQueue


class Graph:

    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)]
                      for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
            self.edges[u][v] = weight
            self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
            D = {v: float('inf') for v in range(self.v)}
            D[start_vertex] = 0

            pq = PriorityQueue()
            pq.put((0, start_vertex))

            while not pq.empty():
                (dist, current_vertex) = pq.get()
                self.visited.append(current_vertex)

                for neighbor in range(self.v):
                    if self.edges[current_vertex][neighbor] != -1:
                        distance = self.edges[current_vertex][neighbor]
                        if neighbor not in self.visited:
                            old_cost = D[neighbor]
                            new_cost = D[current_vertex] + distance
                            if new_cost < old_cost:
                                pq.put((new_cost, neighbor))
                                D[neighbor] = new_cost
            return D


g = Graph(15)


g.add_edge(0, 1, 12.8)
g.add_edge(0, 9, 23.6)
g.add_edge(0, 7, 27.7)

g.add_edge(1, 2, 24.1)
g.add_edge(1, 6, 17)
g.add_edge(1, 7, 22.3)
g.add_edge(1, 3, 42)

g.add_edge(2, 3, 12.8)
g.add_edge(2, 5, 30.8)
g.add_edge(2, 6, 32)

g.add_edge(3, 4, 20)

g.add_edge(4, 5, 25)
g.add_edge(4, 14, 21.6)
g.add_edge(4, 13, 45)

g.add_edge(5, 13, 31.3)
g.add_edge(5, 12, 33.4)
g.add_edge(5, 11, 37.3)
g.add_edge(5, 6, 14.8)

g.add_edge(6, 7, 24.8)
g.add_edge(6, 11, 33)
g.add_edge(6, 10, 32.5)

g.add_edge(7, 10, 19.8)
g.add_edge(7, 9, 50)
g.add_edge(7, 8, 26.3)

g.add_edge(8, 0, 26.3)


D = g.dijkstra(0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])

