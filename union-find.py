

def init(E):
    nodes = dict()
    for e in E:
        nodes[e] = None
    return nodes

def find(nodes, U):
    if nodes[U] == None:
        return U
    return find(nodes[U])

def union(nodes,U0,U1):
    temp = find(U0)
    nodes[find(U1)] = temp
    return temp

E = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
nodes = init(E)
print nodes
