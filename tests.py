import unionfind

E = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
nodes = unionfind.init(E)
print(nodes.items())

unionfind.union(nodes,1,3)

print(nodes.items())
print(unionfind.find(nodes,3))
