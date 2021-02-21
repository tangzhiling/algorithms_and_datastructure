"""
547. Number of Provinces

There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected 
directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities 
and no other cities outside of the group.

You are given an n x n matrix isConnected where 
isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.


"""

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        
        if u_root != v_root:
            self.parent[u_root] = v_root
            self.count -= 1

class Solution(object):
    def findCircleNum(self,  isConnected):
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count