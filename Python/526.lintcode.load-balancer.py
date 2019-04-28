#
# @lc app=lintcode id=1 lang=python
#
# [526] load-balancer
#
# https://www.lintcode.com/problem/load-balancer/description
#
# Implement a load balancer for web servers. It provide the following functionality:
# Add a new server to the cluster => add(server_id).
# Remove a bad server from the cluster => remove(server_id).
# Pick a server in the cluster randomly with equal probability => pick().
# At beginning, the cluster is empty. When pick() is called you need to randomly return a server_id in the cluster.
# 
# Example 1:
# Input:
#   add(1)
#   add(2)
#   add(3)
#   pick()
#   pick()
#   pick()
#   pick()
#   remove(1)
#   pick()
#   pick()
#   pick()
# Output:
#   1
#   2
#   1
#   3
#   2
#   3
#   3
# Explanation: The return value of pick() is random, it can be either 2 3 3 1 3 2 2 or other.
# 
# 
#
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.arr2id = {}
        self.ids = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.arr2id:
            return
        
        self.ids.append(server_id)
        self.arr2id[server_id] = len(self.ids) -1
        

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.arr2id:
            return
        
        idx = self.arr2id[server_id]
        del self.arr2id[server_id]
        
        last = self.ids[-1]
        self.arr2id[last] = idx
        self.ids[idx] = last
        self.ids.pop()
        

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        import random
        index = random.randint(0, len(self.ids) - 1)
        return self.ids[index]





