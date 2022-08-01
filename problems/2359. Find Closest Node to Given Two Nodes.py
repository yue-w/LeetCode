from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
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
                    
if __name__ == "__main__":
    edges = [23,21,28,30,25,10,13,18,1,22,16,10,27,8, 6, 26,19,0, -1,12,11,29,2, 24,4, 14,17,15,5, 7, 9]
    node1 = 28
    node2 = 13
    # edges = [1,2,3,4,5,6,7,-1]
    # node1 = 0
    # node2 = 3
    rst = Solution().closestMeetingNode(edges, node1, node2)
    print(rst)