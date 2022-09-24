
from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Gready, sort
        """
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        np = len(players)
        nt = len(trainers)
        rst = 0
        p = 0
        t = 0

        while p < np:
            if t == nt:
                return rst
            if players[p] > trainers[t]:
                p += 1
            else:
                rst += 1
                p += 1
                t += 1

        return rst