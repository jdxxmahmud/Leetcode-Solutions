# Problem Link: https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        commonNodes = set()

        visited = {}

        for edge in edges:
            startNode, endNode = edge

            visited[startNode] = True
            visited[endNode] = True

            if startNode in commonNodes:
                return startNode
            elif endNode in commonNodes:
                return endNode

            commonNodes.update(edge)

