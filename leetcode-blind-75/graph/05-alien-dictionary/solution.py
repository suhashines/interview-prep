from collections import defaultdict,deque

def alien_dictionary(dict:list[list[str]],K:int,n:int)->str:

    # construct the graph

    g = defaultdict(set)
    # default dictionary has the provision that
    # if a key doesn't exist it will create that with an empty set

    in_degree_map = {}

    # initialize the in_degree_map

    for w in dict:

        for ch in w:

            in_degree_map[ch] = 0

    for i in range(n-1):

        s1 = dict[i]
        s2 = dict[i+1]

        min_length = min(len(s1),len(s2))

        k = 0
        while(k<min_length):

            if s1[k]!= s2[k] and s2[k] not in g[s1[k]]:

                # add a directed edge from s1[k],s2[k]
                g[s1[k]].add(s2[k])

                # track the in degrees
                in_degree_map[s2[k]] += 1

                break
            k += 1
        
        if k == min_length and len(s1)>len(s2) :
            # invalid dictionary
            return ""
    
    # g.print_graph()

    print(f"in degree map: {in_degree_map}")
    
    # now find a topological ordering of the constructed graph

    def kahns_algorithm():

        q = deque()

        order = []

        visited = {}

        for node in in_degree_map:

            if in_degree_map[node] == 0 :
                visited[node] = 1
                q.append(node)
        
        while q :

            u = q.popleft()

            for v in g[u]:

                in_degree_map[v] -= 1

                if v not in visited:
                    visited[v] = 1
                    if in_degree_map[v] == 0:
                        q.append(v)
            # append u to the order array
            order.append(u)        

        return order

    topo_order = kahns_algorithm()

    if len(topo_order) != K :
        return ""
    
    return "".join(topo_order)

words = ["za","zb","ca","cb"]
K=4

print(alien_dictionary(words,K,len(words)))