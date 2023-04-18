#Dijkstra Alog
import sys

class Dijkstra:
    def __init__(self,graph):
        self.V = len(graph)
        self.grid = graph
        self.Graph = self.Make_graph()

    def Make_graph(self):
        graph = {i:[] for i in range(len(self.grid))}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] > 0:
                    graph[i].append((j,self.grid[i][j]))
                    graph[j].append((i,self.grid[j][i]))
        return graph

    def Dijkstra_Algo(self,sorc):
        path = dict()
        inf = sys.maxsize
        Dp = [inf for _ in range(self.V)]
        haset = [False for _ in range(self.V)]
        Dp[sorc] = 0

        for _ in range(self.V):

            v = self.Get_Min(Dp,haset)
            haset[v] = True

            for d,w in self.Graph[v]:
                if Dp[v] + w < Dp[d]:
                    Dp[d] = Dp[v]+w
                    path[d] = v
        return Dp,path

    def Get_Min(self,dp,has):
        mine = sys.maxsize
        v = 0
        for i in range(len(dp)):
            if has[i] == False and dp[i] < mine:
                mine = dp[i]
                v = i
        return v





graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
Dijk = Dijkstra(graph)
sour = 0
p,path = Dijk.Dijkstra_Algo(sour)
pa = 6
while pa != sour:
    print(pa)
    pa = path[pa]
print(pa)
print(p)
print()
print(path)