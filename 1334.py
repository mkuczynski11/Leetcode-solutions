#https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
import heapq
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        graph = {}
        for u,v,w in edges:
            graph[u] = graph.get(u, []) + [(v,w)]   #set vericies
            graph[v] = graph.get(v, []) + [(u,w)]
        vert, min_n = None, float('inf')            #vert - retrurn value, min_n - cur min neighbours
        for i in range(n):
            visited = set()
            dist = [float('inf') for _ in range(n)]
            h = [(0,i)]                             #heap for storing verticies to traverse
            while h:
                d,u = heapq.heappop(h)
                if u in visited : continue
                visited.add(u)
                for v,w in graph.get(u, []):
                    if v not in visited and d+w < dist[v] and d+w <= distanceThreshold:
                        dist[v] = d+w
                        heapq.heappush(h, (d+w,v))
            count = 0
            for k in range(n):
                if(dist[k] != float('inf')):
                    count += 1
            if vert is None or count <= min_n:
                vert = i
                min_n = count
        return vert
        

a = Solution()
print(a.findTheCity(5,[[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],2))