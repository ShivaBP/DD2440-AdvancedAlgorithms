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

def getNeighbours( vertexInfo):
    numNeighbors = int ( vertexInfo [0]) 
    neighbors = np.array(numNeighbors)
    index = 0
    pointer = 1
    while(pointer < numNeighbors):
        neighbors[index] = vertexInfo[pointer]
        index = index + 1 
        pointer = pointer +2 
    return neighbors


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
                infoIterator = 1
                while ( infoIterator < numNeighbors):
                    neighbour = neighbours [infoIterator]
                    if ( checkVisited(neighbor , visited) == 0 ):
                        queue.append(neighbor)
                        visited.append(neighbor)
                        visitedEdges.append({popped, neighbor})
                    infoIterator = infoIterator + 2

                popIndex = popIndex + 1
        iter = iter +1 

    return (queue , visited)

def checkVisited(vertex , visited):
    for index in range(len(visited) ):
        if (visited[index] == vertex):
            return 1
    return 0

def countVisited (visited):
    return len(visited)

def checkBFSTermination(queue ):
    if (len(queue) == 0 ):
        return 1
   return 0
    

def numCC(averageDegree):
     # a random sample of vertices
    s =int (math.pow(numWeights , 3 )/  math.pow(epsilon , 2) 

    # to be implemneted more efficiently
    chosenVertices = np.array(random.sample(list(vertices) , s))

    for i in range(s):
        #init BFS
        root = chosenVertices[i]
        (queue , visited) = BFS(chosenVertices,root, r , 0)
        numVisited = countVisited (visited)

        #flip a coin 
        flip = random.randint(0, 1)
        if ( (flip == 1) and  (numVisited  <  numWeights)  and  ( getDegree(vertex)  <= averageDegree for vertex in visited )  ):
            iterUpdate = len(visitedEdges) * 2
            BFS(chosenVertices , iterUpdate)
            if (checkBFSTermination(queue) == 1 ):


