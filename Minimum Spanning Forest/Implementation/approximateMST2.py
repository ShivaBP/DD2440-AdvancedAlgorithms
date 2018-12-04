import sys
import fileinput
import numpy as np
import random
from random import randint
import math
import time


epsilon = 0.2 
maxIter = int(8/epsilon)
W = [1,2,3,4]
numWeights = len(W)
edges = list ()
visitedEdges = list()
#numVertices = int (input())
numVertices = int (sys.stdin.readline())


def getVertexInfo(vertex):
    #print(vertex)
    sys.stdout.write(str(vertex) + "\n")
    sys.stdout.flush()
    kattisInput = list(sys.stdin.readline())
    vertexInfo = list()
    for i in range(len(kattisInput)):
        if (kattisInput[i]== ' ' or kattisInput[i] =='\n'):
            i = i+1
        else:
            nei = int (kattisInput[i])
            node = int ( vertex)
            vertexInfo.append(nei)
            edges.append ( [node, nei])
            i= i +1
    return vertexInfo

def getDegree (  vertexInfo):
    return int(vertexInfo[0])

def getNeighbours( vertexInfo):
    numNeighbors = int ( vertexInfo [0]) 
    neighbors = list()
    pointer = 1
    while(pointer < numNeighbors):
        neighbors.append(int (vertexInfo[pointer]))
        pointer = pointer +2 
  
    return neighbors


def getNeighborWeight (vertexInfo , neighbor ):
    
    weight = 0

    for i in range (1, (len(vertexInfo) -1 ) ):
       
        if (vertexInfo[i] == neighbor):
            weight =  vertexInfo[i+1]
        else:
            i =  i+2

    return int(weight)

def BFS ( root ,  maxIters, W):
    visited = list()
    queue = list()
    BFSEdges = list()

    iter = 0
    while ( iter <= maxIters   ):
        if (iter == 0):
            queue.append(root)
            visited.append(root)
        elif (iter > 0 ) :
            popIndex = 0
            while ( popIndex < len(queue)) :
                popped = queue[popIndex] 
                queue.pop(popIndex)
                info = getVertexInfo(popped)
                neighbours =  getNeighbours(info)
                for neighbor in neighbours:
                    if ( (checkVisited(neighbor , visited) == 0)  and (getNeighborWeight(info, neighbor) <= W)):
                        queue.append(neighbor)
                        visited.append(neighbor)
                        visitedEdges.append([popped, neighbor])
                        BFSEdges.append([popped, neighbor])
                popIndex = popIndex + 1
        iter = iter +1 

    return (queue , visited , BFSEdges)

def checkVisited(vertex , visited):
    for index in range(len(visited) ):
        if (visited[index] == vertex):
            return int (1)
    return int(0)

def countVisited (visited):
    return len(visited)

def checkBFSTermination(queue ):
    if (len(queue) == 0 ):
        return int (1)
    return int (0)

def calculateMU( W , vertex):
    componentEdges = list()
    queue = list()
    visited = list ()

    queue.append(vertex)
    visited.append(vertex)
    popIndex = 0
    while ( popIndex < len(queue)) :
        popped = queue[popIndex] 
        queue.pop(popIndex)
        info = getVertexInfo(popped)
        neighbours =  getNeighbours(info)
        for neighbor in neighbours:
  
            if ( (checkVisited(neighbor , visited) == 0)  and (getNeighborWeight(info, neighbor) <=  W )):
                
                queue.append(neighbor)
                visited.append(neighbor)
                visitedEdges.append([popped, neighbor])
                componentEdges.append([popped, neighbor])
        popIndex = popIndex + 1

    mu = len ( componentEdges)
    return int (mu)

def calculateDU ( W, vertex ):
    info = getVertexInfo ( vertex)
    incidents = getNeighbours(info )
    count = 0
    for incident in incidents:
        if (getNeighborWeight(info , incident ) <= W):
            count = count + 1
    return int (count)

def approxCC ( epsilon ,bound,  W, averageDegree):
    #s =int (1/  math.pow(epsilon , 2) )
    s = int ( math.sqrt( numVertices))
    lastVertexIndex = int (numVertices -1 )
    chosenVertices = random.sample(range(0, lastVertexIndex), s)
    beta = list()
    for i in range(s):
        beta.append(0)

    for i in range(s):
        flipCount = 0
        flipTime = 1 
        #init BFS
        root = chosenVertices[i]
        mu = calculateMU(W , root) 
        du = calculateDU ( W , root)
        (queue, visited , BFSEdges )= BFS(root , 1, W)
        numVisited = countVisited (visited)

        #flip a coin     
        while ( checkBFSTermination (queue) == 0):
            if ( flipTime == 0):
                if ( (flip == 1) and  (numVisited  <  bound)  and  ( getDegree(vertex)  <= averageDegree for vertex in visited )  ):
                    iterUpdate = len(visitedEdges)
                    maxIterUpdate = len(visitedEdges) * 2
                    #while ( iterUpdate <  maxIterUpdate  ):                 
                    (queue , visited , BFSEdges) =  BFS( root , 1, W)
                    if( checkBFSTermination(queue) == 0):
                        flipTime = 1 
                    #iterUpdate = iterUpdate +1
            elif ( flipTime == 1):
                flip = random.randint(0, 1)
                flipCount = flipCount +1 
                flipTime = 0

        if (checkBFSTermination(queue) == 1 ):
            if (mu ==  0 ):
                beta[i] = 2

            else:
                beta[i] = ( (du * math.pow(2 , flipCount))  / len(BFSEdges) )

    # sum beta values
    sum = 0
    for i in range(s):
        sum = sum + beta[i]
    
    approxCC = (numVertices * sum ) / (2* s)
    return  approxCC

def averageDegree():
    # a random sample of vertices
    #r =int (1/  math.pow(epsilon , 2) )
    r = int ( math.sqrt( numVertices))
    lastVertexIndex = int (numVertices -1 )
    chosenVertices = random.sample(range(0, lastVertexIndex) , r)

    #approximate average degree
    iter= 0
    current = 0

    degrees = list()
    for i in range(r):
        degrees.append(0)
    average = 0
    while(iter <= maxIter):
        # compute  degree of each sampled vertex
        
        for index in range(r):
            vertexInfo = getVertexInfo(chosenVertices[index])
            degrees[index] = getDegree ( vertexInfo)
            if ( degrees[index] > average):
                average = average + degrees[index]
        
        #compute average degree of sampled vertices
        '''
        current = (sum(degrees) / len(degrees))
        if ( current < average):
            average = current 
    '''
        iter = iter +1 
        
    #average = current / maxIter
        
        
    return average/ maxIter
        
def run():

    dStar = averageDegree()
    #approximate MST
    numConnectedComponents = 0 
    for i in range(numWeights):
        temp = 4/ epsilon

        numConnectedComponents = numConnectedComponents + approxCC(epsilon ,temp ,  W[i] , dStar)
    MST = numVertices - numWeights + numConnectedComponents

    sys.stdout.write("end " + str(MST) + "\n")
    sys.stdout.flush()   


run()