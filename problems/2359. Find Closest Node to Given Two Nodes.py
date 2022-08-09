from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        #return self.method1(edges, node1, node2)
        return self.method2(edges, node1, node2) # Preferred method. More straight forward 
    def method1(self, edges, node1, node2):
        from collections import deque
        if node1 == node2:
            return node1
        dq = deque()
        
        seen1 = set()
        seen1.add(node1)
        seen2 = set()
        seen2.add(node2)
        dq.append((node1, 1))
        dq.append((node2, 2))
        candidate = []
        steps = 0
        while dq:
            steps += 1
            for _ in range(len(dq)):
                node, group = dq.popleft()
                if group == 1:
                    nxt = edges[node]
                    if nxt in seen2:
                        candidate.append((steps, nxt))
                    if nxt != -1 and not nxt in seen1:
                        seen1.add(nxt)
                        dq.append((nxt, 1))

                else:#group == 2
                    nxt = edges[node]
                    if nxt in seen1:
                        candidate.append((steps, nxt))
                    if nxt != -1 and not nxt in seen2:
                        seen2.add(nxt)
                        dq.append((nxt, 2))

        if not candidate:            
            return -1
        else:
            candidate.sort()
            return candidate[0][1]
    
    def method2(self, edges, node1, node2):
        """
        compute all the distances of nodes to node1 and node2.
        then from the nodes that are reachable from both node1 and node2,
        find the min value of the larger distance to node1 and node2.
        """
        def get_distance(node):
            """
            Return the distance from node to all other nodes. -1 if not reachable
            """
            dis = [-1] * len(edges)
            dis[node] = 0
            nxtnode = edges[node]
            ## while there are next node and the node has not been visited (not a cycle).
            while nxtnode != -1 and dis[nxtnode] == -1:
                dis[nxtnode] = dis[node] + 1
                node = nxtnode
                nxtnode = edges[nxtnode] 
            
            return dis
        
        dis1 = get_distance(node1)
        dis2 = get_distance(node2)
        minmax = float('inf')
        
        idx = -1
        for i in range(len(edges)):
            ## if reachable
            if dis1[i] != -1 and dis2[i] != -1:
                maxdis = max(dis1[i], dis2[i])
                if maxdis < minmax:
                    minmax = maxdis
                    idx = i
                if maxdis == minmax:
                    idx = min(idx, i)

        return idx
                    
if __name__ == "__main__":
    edges = [23,21,28,30,25,10,13,18,1,22,16,10,27,8, 6, 26,19,0, -1,12,11,29,2, 24,4, 14,17,15,5, 7, 9]
    node1 = 28
    node2 = 13
    # edges = [1,2,3,4,5,6,7,-1]
    # node1 = 0
    # node2 = 3
    rst = Solution().closestMeetingNode(edges, node1, node2)
    print(rst)