# -- Imports ------------------------------------------------------------------
import sys


# -- Main class ---------------------------------------------------------------
class Paths():
    def __init__(self, vertices):
        self.vertices = vertices
        self.paths= [[0 for column in range(vertices)]for row in range(vertices)]

    
    '''function that prints the shortest distances between the final location and the source location'''
    def printSolution(self, dist):
        print("The shortest distance from your souce point")
        for node in range(self.vertices):
            print(" The distance between the souce and " +node+ "is", dist[node])

    '''this is a utility function that is used to find the vertex with the shortest distance'''
    def minDistance(self, dist, shortestPathSet):
        min = sys.maxsize


        for vertex in range(self.vertices):
            if dist[vertex]< min and shortestPathSet[vertex]==False:
                min = dist[vertex]
                min_index = vertex

        return min_index

    
    '''this functions uses the concept of the dijkstra's algorithm to evaluate the shortest path between the source and the given node
        It utilizes the adjacency matrix representation
    '''
    def shortestPath(self, src):
        dist = [sys.maxmize]* self.vertices
        dist[src]=0
        shortestPathSet = [False] * self.vertices

        for cout in range(self.vertices):

            u=self.minDistance(dist, shortestPathSet)

            shortestPathSet[u] =True


            for vertex in range(self.vertices):
                if self.paths[u][vertex]>0 and shortestPathSet[vertex] == False and dist[vertex]> dist[u] + self.grapg[u][vertex]:
                    dist[vertex] = dist[u] + self.paths[u][vertex]
        
        self.printSolution(dist)

