

def init(E):
    nodes = {}
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

