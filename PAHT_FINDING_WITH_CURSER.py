#Dijkstra Alog
import sys

class Dijkstra:
    def __init__(self,graph):
        self.V = len(graph)
        self.grid = graph
        self.Graph = self.Make_graph()
        self.path = None
        self.source = None
    def Make_graph(self):
        graph = {i:[] for i in range(len(self.grid))}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] > 0:
                    graph[i].append((j,self.grid[i][j]))
                    graph[j].append((i,self.grid[j][i]))
        return graph

    def Dijkstra_Algo(self,sorc):
        self.source = sorc
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
        self.path = path
        return Dp

    def Get_Min(self,dp,has):
        mine = sys.maxsize
        v = 0
        for i in range(len(dp)):
            if has[i] == False and dp[i] < mine:
                mine = dp[i]
                v = i
        return v
    def Path_to_sorc(self,fro):
        s = ''
        pa = fro
        sour = self.source
        path = self.path
        while pa != sour:
            s = s + str(pa) + '>-'
            pa = path[pa]
        s = s + str(pa)
        return s[::-1]


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
p = Dijk.Dijkstra_Algo(sour)
print(p)
pat = Dijk.Path_to_sorc(8)
pa = Dijk.Path_to_sorc(7)
print(pat)
print(pa)