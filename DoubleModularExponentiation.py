from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        index = 0

        for a, b, c, m in variables:
            temp = (((a ** b) % 10) ** c) % m

            if temp == target:
                res.append(index)
            index += 1    

        return res        