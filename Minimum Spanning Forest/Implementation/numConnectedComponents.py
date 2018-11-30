import sys
import fileinput
import numpy as np
import random
from random import randint
import math

epsilon = 0.2 
maxIter = int(8/epsilon)
W = {1,2,3,4}
numWeights = len(W)
numVertices = int (input())
vertices = np.zeros(numVertices)
for index in range(numVertices):
    vertices[index] = index

edges = list ()
visitedEdges = list()

def getVertexInfo(vertex):
    print(vertex)
    kattisInput = list(input())
    vertexInfo = list()
    for i in range(len(kattisInput)):
        if (kattisInput[i]== ' '):
            i = i+1
        else:
            vertexInfo.append(kattisInput[i])
            edges.append ( {vertex, kattisInput[i]})
            i= i +1
    return vertexInfo

def getDegree (  vertexInfo):
    return vertexInfo[0]

def averageDegree():
    # a random sample of vertices
    r =int (round ((1 / epsilon)*np.sqrt(numVertices)))
    chosenVertices = np.array(random.sample(list(vertices) , r))

    #approximate average degree
    iter= 0
    averageDegree = math.inf 
    while(iter <= maxIter):
        # compute  degree of each sampled vertex
        degrees = np.zeros(r)
        for index in range(r):
            vertexInfo = getVertexInfo(chosenVertices[index])
            degrees[index] = getDegree ( vertexInfo)
        
        #compute average degree of sampled vertices
        current = sum(degrees) / len(degrees)
        if ( current  <  averageDegree ):
            averageDegree = current 
        
        iter = iter +1 
    return averageDegree
        
def BFS ( vertices, root , sampleSize ,  maxIters):
    visited = list()
    queue = list()

    iter = 0
    while ( (iter <= maxIters)   ):
        if (iter == 0):
            queue.append(root)
            visited.append(root)
        else:
            popIndex = 0
            while ( popIndex < numVertices) :
                popped = vertices[popIndex] 
                queue.pop(popIndex)
                neighbours =  getVertexInfo(popped )
                numNeighbors = int (info[0]) 
                for pointer in range( numNeighbors):
                    infoIterator = 1
                    neighbour = neighbours [infoIterator]
                    if ( checkVisited(neighbor , visited) == 0 ):
                        queue.append(neighbor)
                        visited.append(neighbor)
                        visitedEdges.append({popped, neighbor})
                popIndex = popIndex + 1
        iter = iter +1 

    return visited

def checkVisited(vertex , visited):
    for index in range(len(visited) ):
        if (visited[index] == vertex):
            return 1
    return 0

def countVisited (visited):
    return len(visited)

def checkBFSTermination(vertices, visted):
    for vertex in vertices:
        if (checkVisited (vertex, visited ) == 0):
            return 0 
    return 1

def numCC(averageDegree):
     # a random sample of vertices
    r =int (round ( 1 /  math.pow(epsilon , 2) ))
    chosenVertices = np.array(random.sample(list(vertices) , r))

    beta = np.zeros(r)
    for i in range(r):
        #init BFS
        root = chosenVertices[i]
        visited = BFS(chosenVertices,root, r , 0)
        numVisited = countVisited (visited)

        #flip a coin 
        flip = random.randint(0, 1)
        if ( (flip == 1) and  (numVisited  <  numWeights)  and  ( getDegree(vertex)  <= averageDegree for vertex in visited )  ):
            iterUpdate = len(visitedEdges) * 2
            BFS(chosenVertices , iterUpdate)
            if (checkBFSTermination == 1 ):













    

    







    





