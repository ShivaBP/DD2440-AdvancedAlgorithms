import matplotlib.pyplot as plt
import numpy
import time

import sys

import random

'''
class Edge:
    w = 0
    def __init__(self, w=random.random()):
        self.w = w
'''
class Node:
    neighborW = []
    coord = [random.random(), random.random()]

    def __init__(self, x=random.random(), y=random.random()):
        self.coord = [x,y]
        #self.age = age

    def printCoord(self):
        print(self.coord)

    def printNeighbors(self):
        print(self.neighborW)

class Graph:
    nodes = []
    def setGraph(self, G):
        self.nodes = G
    def addNode(self, krafs):
        print("Hello my name is " + krafs)

isDone = False
            
def request(G):
    global isDone
    if(not isDone):
        #time.sleep(1)
        #req = input()

        #req = sys.stdin.readline().rstrip()
        req = input()

        newReq = req.split(" ")
        #print(len(newReq))

        if(len(newReq) == 1):
            req = int(newReq[0])
            temp = str(len(G[req][1])) + " "
            for i in range(0,len(G[req][1])):
                temp += str(G[req][1][i][0]) + " " + str(G[req][1][i][1]) + " "
            
            sys.stdout.write(temp + "\n")
            sys.stdout.flush()
            #sys.stderr.write(temp + "\n")
            #print(temp)
        elif(newReq[0] == "end"):
            '''
            f = open('myfile', 'w')
            f.write("answer: " + str(averageDeg))
            f.write("approx: " + str(newReq[1]))
            f.close()
            '''
            #sys.stderr.write("Average degree: " + str(averageDeg) + "\n")
            sys.stderr.write("MST-weight: " + str(newReq[1]) + "\n")
            quit()
            #print("answer: " + str(averageDeg))
            #print("approx: " + str(newReq[1]))
            isDone = True
        else:
            #sys.stderr.write("Average degree: " + str(averageDeg) + "\n")
            sys.stderr.write("approx-MST-weight: " + str(newReq[1]) + "\n")


averageDeg = 0
extraweights = 0
def main(argv):
    #sys.stderr.write("prutt" + "\n")
    #sys.stderr.write("Struts"+ "\n")
    global extraweights
    
    n = 10
    extraweights = 5*n
    maxweight = 4
    G = randomizeG(n, maxweight)
    #paint(G)

    sum = 0
    for i in range(0, len(G)):
        sum += len(G[i][1])
    
    avdeg = sum / len(G)

    global averageDeg
    averageDeg = avdeg
    
    #print(avdeg)
    #print(n)
    sys.stdout.write(str(n) + "\n")
    sys.stdout.flush()
    sys.stderr.write("Total number of nodes: " + str(n) + "\n")
    #sys.stderr.write("answer: " + str(averageDeg) + "\n")
    sys.stderr.write("Average degree: " + str(averageDeg) + "\n")
    #sys.stdout.write(str(n) + "\n")

    while(True):
        request(G)
    

    #print(G[0][1])

    #p = Node(1,2)
    #p.printCoord()
    #p2 = TestNode()
    #p2.myfunc()

    #print("done")
    time.sleep(10000)

def randomizeG(n, w):

    G = []
    for i in range(0, n):
        G.append([[],[]])
    
    for i in range(0, n):
        x = random.random()
        y = random.random()
        G[i][0].append(x)
        G[i][0].append(y)

    

    for i in range(0, n):
        tempNode = i+1
        weight = random.randint(1,w)
        if(i != n-1):
            G[i][1].append([tempNode, weight])
            G[tempNode][1].append([i, weight])
        else:
            G[i][1].append([0, weight])
            G[0][1].append([i, weight])
        '''
        tempNode = random.randint(0,n-1)
        while(True):
            if(tempNode != i):
                contains = False
                for j in range(0,len(G[i][1])):
                    if(G[i][1][j][0] == tempNode):
                        contains = True
                if(not contains):
                    break
            tempNode = random.randint(0,n-1)
        weight = random.randint(1,w)
        G[i][1].append([tempNode, weight])
        G[tempNode][1].append([i, weight])
        '''
    global extraweights
    extraEdges = random.randint(0,extraweights)
    for j in range(0, extraEdges):
        i = random.randint(0,n-1)
        tempNode = random.randint(0,n-1)
        while(True):
            if(tempNode != i):
                contains = False
                for j in range(0,len(G[i][1])):
                    if(G[i][1][j][0] == tempNode):
                        contains = True
                if(not contains):
                    break
            tempNode = random.randint(0,n-1)

        weight = random.randint(1,w)
        G[i][1].append([tempNode, weight])
        G[tempNode][1].append([i, weight])
        
    return G





screenStarted = False
fig = None
ax = None

def paint(G):
    global screenStarted
    global fig
    global ax
    if(screenStarted == False):
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.set_title('klafsPelle')
        fig.canvas.draw()
        fig.canvas.draw()
        screenStarted = True
    else:
        ax.cla()

    for i in range(0,len(G)):
        ax.plot(G[i][0][0], G[i][0][1], 'r.')

    for i in range(0,len(G)):
        for j in range(0,len(G[i][1])):
            index = G[i][1][j][0]

            x = []
            x.append(G[i][0][0])
            x.append(G[index][0][0])

            y = []
            y.append(G[i][0][1])
            y.append(G[index][0][1])

            ax.plot(x, y, 'b-')
    #ax.plot(classBx, classBy, 'b-')

    #x = numpy.linspace(-2,2)
    
    #y = k*x+m

    #line = ax.plot(x, y, 'r-')

    fig.canvas.draw()

if __name__ == "__main__":
    main(sys.argv)