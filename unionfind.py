def init(E):
    nodes = {}
    for e in E:
        nodes[e] = None
    return nodes

def find(nodes, U):
    if U not in nodes:
        print('Find failed: ' + str(U) + ' not found')
        return None
    if nodes[U] == None:
        return U
    return find(nodes,nodes[U])

def union(nodes,U0,U1):
    U1_temp = find(nodes,U1)
    if U1_temp == None:
        print('Union failed ' + str(U1) + ' not found')
        return None
    U0_temp = find(nodes,U0)
    if U0_temp == None:
        print('Union failed ' + str(U0) + ' not found')
        return None
    nodes[U0_temp] = U1_temp
    return U1_temp

