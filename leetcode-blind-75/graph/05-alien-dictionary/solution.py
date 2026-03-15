import queue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_undirected_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def add_directed_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)


    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def print_graph(self):

        for node in self.graph:

            print(f"{node}->",end="")

            for v in self.get_neighbors(node):

                print(f"{v}",end=" ")
            print()
    


def alien_dictionary(dict:list[list[str]],K:int,n:int)->str:

    # construct the graph

    g = Graph()

    in_degree_map = {}

    for i in range(n-1):

        s1 = dict[i]
        s2 = dict[i+1]

        min_length = min(len(s1),len(s2))

        k = 0
        while(k<min_length):

            if s1[k]!= s2[k]:

                # add a directed edge from s1[k],s2[k]
                g.add_directed_edge(s1[k],s2[k])

                # track the in degrees

                if s1[k] not in in_degree_map:
                    in_degree_map[s1[k]] = 0

                if s2[k] not in in_degree_map:
                    in_degree_map[s2[k]] = 1
                else:
                    in_degree_map[s2[k]] += 1
                break
            k += 1
        
        if k == min_length and len(s1)>len(s2) :
            # invalid dictionary
            return ""
    
    g.print_graph()

    print(f"in degree map: {in_degree_map}")
    
    # now find a topological ordering of the constructed graph

    def kahns_algorithm():

        q = queue.Queue()

        order = []

        visited = {}

        for node in in_degree_map:

            if in_degree_map[node] == 0 :
                visited[node] = 1
                q.put(node)
        
        while not q.empty() :

            u = q.get()

            for v in g.get_neighbors(u):

                if v not in visited:

                    visited[v] = 1

                    in_degree_map[v] -= 1

                    if in_degree_map[v] == 0:
                        q.put(v)
            # append u to the order array
            order.append(u)        

        return order

    topo_order = kahns_algorithm()

    if len(topo_order) != K :
        return ""
    
    return str(topo_order)

words = ["z","x"]
N=2 
K=2

print(alien_dictionary(words,N,K))