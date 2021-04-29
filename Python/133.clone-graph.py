#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#
# https://leetcode.com/problems/clone-graph/description/
#
# algorithms
# Medium (26.31%)
# Likes:    743
# Dislikes: 813
# Total Accepted:    213.9K
# Total Submissions: 812.9K
# Testcase Example:  '{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}'
#
# Given a reference of a node in a connected undirected graph, return a deep
# copy (clone) of the graph. Each node in the graph contains a val (int) and a
# list (List[Node]) of its neighbors.
#
#
#
# Example:
#
#
#
#
# Input:
#
# {"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}
#
# Explanation:
# Node 1's value is 1, and it has two neighbors: Node 2 and 4.
# Node 2's value is 2, and it has two neighbors: Node 1 and 3.
# Node 3's value is 3, and it has two neighbors: Node 2 and 4.
# Node 4's value is 4, and it has two neighbors: Node 1 and 3.
#
#
#
#
# Note:
#
#
# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no
# self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q
# must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned
# graph.
#
#
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Solution(object):

    def cloneGraph(self, node):
        if not node:
            return None
        
        # step 1: find nodes
        nodes = self.find_nodes_bfs(node)
        # step 2： copy nodes
        mapping = self.copy_nodes(nodes)
        # step 3: copy edges
        self.copy_edges(nodes, mapping)

        return mapping[node]
    
    def find_nodes_bfs(self, node):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    continue

                queue.append(neighbor)
                visited.add(neighbor)
        return list(visited)
    
    def copy_nodes(self, nodes):
        mapping = {}
        for node in nodes:
            mapping[node] = Node(node.val)
        return mapping
    
    def copy_edges(self, nodes, mapping):
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(mapping[neighbor])
        

    # BFS
    def cloneGraph1(self, node):
        if not node:
            return None
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:  # neighbor is not visited
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS iteratively
    def cloneGraph2(self, node):
        if not node:
            return
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    # DFS recursively
    def cloneGraph3(self, node):
        if not node:
            return
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

