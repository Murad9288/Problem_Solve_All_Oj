class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(lambda: [])
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
            
        def calculateSumOfDistancesInSubtree(root, parent, depth):
            total_sum = depth
            for node in tree[root]:
                if node != parent:
                    total_sum += calculateSumOfDistancesInSubtree(node, root, depth + 1)
            return total_sum
        
        subtree_size = [0 for _ in range(N)]
        def calculateSubtreeSizes(root, parent):
            subtree_size[root] = 1 # root
            for node in tree[root]:
                if node != parent:
                    subtree_size[root] += calculateSubtreeSizes(node, root)
            return subtree_size[root]
        
        sum_of_distances = [0 for _ in range(N)]
        def calculateSumOfDistances(root, parent, root_sum_of_distances):
            sum_of_distances[root] = root_sum_of_distances
            for node in tree[root]:
                if node != parent:
                    # Intuitively: We are one step closer to each node in node's subtree (including this node)
                    # and one step further from each node not in node's subtree (including it's parent)
                    node_sum_of_distances = root_sum_of_distances - subtree_size[node] + (N - subtree_size[node])
                    calculateSumOfDistances(node, root, node_sum_of_distances)
        
        root, dummy_parent = 0, -1
        calculateSubtreeSizes(root, dummy_parent)
        calculateSumOfDistances(root, dummy_parent, calculateSumOfDistancesInSubtree(root, dummy_parent, 0))        

        return sum_of_distances
