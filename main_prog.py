"""
-------------------------------------------------------------------
Programming Assignment 3
-------------------------------------------------------------------
Name        : Manan Darji
Roll Number : CS22MTECH14004
Subject     : Advance Data Structure and Algorithm (CS6013)
Topic       : Steiner Tree Problem
-------------------------------------------------------------------
"""
__author__ = "@Manan_Darji"

# -------------------------------------------------- IMPORTS --------------------------------------------------
import math
import numpy as np

# -------------------------------------------------- FLOYD_WARSHALL_ALGO --------------------------------------------------
def FLOYD_WARSHALL_ALGO(G, V):
    """Here I Implemented The Floyd Warshall Algorithm Which Is Used For Solving All Pairs Shortest Path Problems.
    The Problem Is To Find The Shortest Distances Between Every Pair Of Vertices In A Given Edge-Weighted Directed Graph.

    Args:
        G (List): Graph
        V (Int): No Of Vertices In A Graph

    Returns:
        Tuple: Complete Graph
    """
    # Here i initialized PAR matrix and weights
    distance = np.copy(G)
    parent = np.zeros((V, V))

    for i in range(0, V):
        for j in range(0, V):
            if i == j:
                parent[i][j] = 0
            elif distance[i][j] != math.inf:
                parent[i][j] = i
            else:
                parent[i][j] = -1

    # FLOYD WARSHALL - Time Complexity - O(n3)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    parent[i][j] = k
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance, parent


# -------------------------------------------------- VALID_EDGE_CHECK --------------------------------------------------
def VALID_EDGE_OR_NOT(u, v, m):
    """This Is A Helper Function That I Created In Order To Check That Is It A Valid Prims Edge. I.E. It's Not Included
    Already And One Of It's End Point Is Explored.

    Args:
        U (Int): Node1
        V (Int): Node 2
        m (List): Already Added Nodes

    Returns:
        Bool: Valid Edge Or Not
    """
    if u == v:
        return False
    if m[u] == False and m[v] == False:
        return False
    elif m[u] == True and m[v] == True:
        return False
    return True


# -------------------------------------------------- PRIMS_ALGO --------------------------------------------------
def PRIMS_ALGO(Graph):
    """This is a Prims algo which finds the MST from the Graph

    Args:
        Graph (list): 2d Matrix

    Returns:
        List : List Of Edges In MST.
    """
    V = Graph.shape[0]
    Container = [False] * V
    # Here I Am Adding First Vertex Into the Mst
    Container[0] = True
    EdgeCount = 0
    MSTEdgeList = []

    # Add Edges Unless V-1 Edges Are Added
    while EdgeCount < V - 1:
        minimum = math.inf
        a = -1
        b = -1
        for i in range(V):
            for j in range(V):
                if Graph[i][j] < minimum:
                    # Here I Am Checking if edge should be Added in MST or not according to prims algo.
                    if VALID_EDGE_OR_NOT(i, j, Container) == 1:
                        minimum = Graph[i][j]
                        a = i
                        b = j

        if a != -1 and b != -1:
            # print(f"Edge {EdgeCount}: ({a+1}, {b+1})")
            EdgeCount += 1
            Container[b] = Container[a] = True
            MSTEdgeList.append([a, b])
    return MSTEdgeList


# -------------------------------------------------- TraceRoute FUNCTION --------------------------------------------------
def TraceRoute(parent, q, p, route):
    """Helper Function To Find The Shortest Path Recursively From Parents

    Args:
        parent (list): Parent Nodes List
        q (int): Node 1
        p (int): Node 2
        route (list): We Return In This List
    """
    if parent[q][p] == q:
        return
    TraceRoute(parent, q, parent[q][p], route)
    route.append(parent[q][p])


def print_path(parent, p, q):
    """Function to Find the shortest path

    Args:
        parent (list): Parent Nodes List
        p (int): Node 1
        q (int): Node 2

    Returns:
        list: Returns Route
    """
    route = [p]
    TraceRoute(parent, p, q, route)
    route.append(q)
    return route


# -------------------------------------------------- MAIN FUNCTION --------------------------------------------------


# Here i used numpy to read the input txt file
InputMat = np.loadtxt("input.txt")
print("-" * 50)
print("INPUT MATRIX : ")
print("-" * 50)
print(InputMat)
print("-" * 50)

NoOfVertices = InputMat.shape[0]
print("No Of Vertices In Input Graph : ", NoOfVertices)

# Here i have set non connected nodes in a graph as infinity
for i in range(NoOfVertices):
    for j in range(NoOfVertices):
        if i != j and InputMat[i][j] == 0:
            InputMat[i][j] = math.inf

StainerVertSet = []
print("-" * 50)
print("List all the Steiner vertices (type * to quit):")
print("-" * 50)
Flag = False
while True:
    InpStainerVert = input()
    if InpStainerVert.isnumeric():
        val = int(InpStainerVert)
        if val > NoOfVertices or val < 1:
            print("This Vertex is Invalid.")
        else:
            if val - 1 in StainerVertSet:
                print("Vertex Already Added In Set")
            else:
                StainerVertSet.append(val - 1)
    elif InpStainerVert == "*":
        break
    else:
        print("Please Enter Valid Stainer Vertex!")
        continue
    
    if len(StainerVertSet) == NoOfVertices:
        print("No Required Vertices. So, No Path Calculation Needed.")
        Flag = True
    if len(StainerVertSet) == NoOfVertices - 1:
        print("Only One Required Vertex. So, No Path Calculation Needed.")
        Flag = True
        
print("-" * 50)
if Flag:
    exit()

# Here I Am Running Floyd Warshall To Get Complete Graph.
CompleteGraph, ParentVertices = FLOYD_WARSHALL_ALGO(InputMat, NoOfVertices)

# Here I Am Removing Stainer Vertices From Complete Graph
CompleteGraphCopy = np.copy(CompleteGraph)
Required = np.delete(CompleteGraphCopy, StainerVertSet, axis=0)
Required = np.delete(Required, StainerVertSet, axis=1)

# Here I Am Finding MST On Required Vertices.
MSTEdgeList = PRIMS_ALGO(Required)

# Here I am Converting 2D Array to 1D Array.
tree = ParentVertices.tolist()
tree = [[int(tree[i][j]) for j in range(NoOfVertices)] for i in range(NoOfVertices)]

MSTPath = []
for i in range(len(MSTEdgeList)):
    u = MSTEdgeList[i][0]
    v = MSTEdgeList[i][1]

    for index in StainerVertSet:
        if u >= index:
            u += 1
        if v >= index:
            v += 1
        lst = print_path(tree, u, v)
        MSTPath.append(lst)

FinalPath = MSTPath.copy()
for i in range(len(MSTPath)):
    FinalPath[i] = [x + 1 for x in FinalPath[i]]
    SteinerList = np.zeros((NoOfVertices, NoOfVertices))

for i in range(len(MSTPath)):
    for j in range(len(MSTPath[i]) - 1):
        p = MSTPath[i][j]
        q = MSTPath[i][j + 1]
        SteinerList[p][q] = 1
        SteinerList[q][p] = 1

# Here I Am Printing The Steiner Tree.
for i in range(NoOfVertices):
    l = []
    for j in range(NoOfVertices):
        if SteinerList[i][j] != 0:
            l.append(j + 1)
    print("Neighbors of Vertex", i + 1, ":", l)

print("-" * 50)
