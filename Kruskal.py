from unionfind import *
from re import split
from pprint import pprint
import operator

def setup():
    #Get information from file
    theFile = open('test01.txt')
    rawData = theFile.read()
    theFile.close()
    
    #Split data string into list
    rawData = split('\n',rawData)
    rawData = filter(bool,rawData)
    
    cities = list()

    #Create and return sorted data in list
    data = list()
    for line in rawData:
        item = list()
        temp = line.split()
        item.append(temp[0])
        item.append(temp[1])
        item.append(int(temp[2]))
        cities.append(temp[0])
        cities.append(temp[1])
        data.append(item)

    cities = sorted(set(cities))
    return sorted(data, key=operator.itemgetter(2)),cities

# Method to perform Kruskal's Algorithm    
def kruskal(data,cities):
    distance = 0
    result = list()
    cities = init(cities)
    for edge in range(len(data)):
        path = data.pop(0)
        #if (cities[path[0]] == None):
        #If the two cities in the path do not have the same
        #canonical representative, join them together
        if find(cities,path[0]) != find(cities,path[1]):
            union(cities, path[0],path[1])
            result.append((path[0] + ' -> ' + path[1]))
            distance += path[2]
    return result,distance

data,cities = setup()
result,distance = kruskal(data,cities)
pprint(result)
print("Distance of minimum spanning tree: " + str(distance))





