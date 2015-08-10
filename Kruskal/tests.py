import unionfind
from pprint import pprint
# Method to pretty print the nodes and what they point to
def pp():
    pprint(nodes, width=1)

E = ['a','b','c','d','e','f','g','h','i','j']
print('Nodes initialized to all equal null')
nodes = unionfind.init(E)
pp()

print('Union a and c, node a points to node c')
unionfind.union(nodes,'a','c')
pp()

print('Union b and d, Node b points to node d')
unionfind.union(nodes,'b','d')
pp()

print('Union c and f, node c points to node f')
unionfind.union(nodes,'c','f')
pp()

print('Union j with b, this points canonical rep of j to rep of b')
#node j points to node b, but
# b points to d, therefore j
# will point to d
unionfind.union(nodes,'j','b')
pp()

print('Union h with a, points canonical rep of h to rep of a')
#h will point to c for reasons above
unionfind.union(nodes,'h','a')
pp()

print('Union f with j, point canonical rep of f to rep of j')
# This should make f point to d
unionfind.union(nodes,'f','j')
pp()

