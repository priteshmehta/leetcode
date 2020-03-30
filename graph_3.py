# https://www.python-course.eu/graphs_python.php
#Cycle detection
#Depth-first search
#Heuristic search (A* algorithm)
#Identification of connected components
#Minimum spanning tree (Prim's algorithm)
#Mutual-accessibility (strongly connected components)
#Shortest path search (Dijkstra's algorithm)

class Graph():
    def __init__(self, graph_dict={}):
        self.__graph_dict = graph_dict

    def add_vertax(self, vertax):
        if vertax not in self.__graph_dict.keys():
            self.__graph_dict.update({vertax, []})

    def add_edge(self, vertax1, vertax2):
        if vertax1 in self.__graph_dict.keys():
            self.__graph_dict[vertax1].append(vertax2)
        else:
            self.__graph_dict[vertax1] = [vertax2]

    def get_edges(self):
        edges = []
        for vertex in self.__graph_dict.keys():
            for neighbour in self.__graph_dict[vertex]:
                if {vertex, neighbour} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def get_vertices(self):
        return self.__graph_dict.keys()

    def find_path(self, start_vertax, end_vertax, path=[]):
        path = path + [start_vertax]
        if start_vertax not in self.__graph_dict.keys():
            return []
        elif start_vertax == end_vertax:
            return [path]
        paths = []
        for vertax in self.__graph_dict[start_vertax]:
            if vertax not in path:
                extended_path = self.find_path(vertax, end_vertax, path)
            
                for p in extended_path:
                    paths.append(p)
        return paths
        
    def vertex_degree(self, vertext):
        edges  = self.__graph_dict[vertext]
        total = len(edges) + edges.count(vertext)
        return total

    def bfs(self, s):
        visited={}
        for i in self.__graph_dict:
            visited[i]=False
        print(self.__graph_dict)
        queue = []
        queue.append(s)
        visited[s] = True
        while len(queue) != 0:
            s = queue.pop(0)
            for node in self.__graph_dict[s]:
                if visited[node] != True:
                    visited[node] = True
                    queue.append(node)

            print(s)





if __name__ == "__main__":
    g = { "a" : ["d", "f"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : ["d"]
        }
    graph = Graph(g)
    graph.add_edge("z", "a")
    graph.add_edge("z", "z")
    #print(graph.get_vertices())
    #print(graph.get_edges())
    #print(graph.find_path("a", "c"))
    #print(graph.vertex_degree("c"))


    g1 = {  "a": ["b", "c"],
            "b": ["d", "e"],
            "c": ["f", "e"],
            "e": ["h"]
        }
    graph1 = Graph(g1)
    graph1.bfs("a")


    # find_isolated_vertices
    #  is_connected
    # shortest path
    # Grapth Density (2*E / (V * V(-1)), Complete grapth, isolated grapth, sparsed graph
    # Tree / Forest  - each vertex has exastly one edge (no cycles in it)