from PancakeGraph import PancakeGraph
import time


class PancakeSort:

    def __init__(self, graph, n):
        self.graph = graph
        self.n = n
        self.root = tuple([i for i in range(1, n + 1)])
        self.maxDepth = self.bfs(self.graph.adjacencyList, self.root) - 1  # subtract 1 since root depth is 0

    # https://stackoverflow.com/questions/70398247/how-can-i-find-the-max-depth
    # run BFS from the root(sorted array) to any possible permutation
    def bfs(self, graph, root):
        maxdepth = 0
        visited = []
        queue = []
        visited.append(root)
        queue.append((root, 1))
        while queue:
            x, depth = queue.pop(0)
            maxdepth = max(maxdepth, depth)
            for child in graph[x]:
                if child not in visited:
                    visited.append(child)
                    queue.append((child, depth + 1))
        return maxdepth

    def size(self):
        return len(self.graph.V)

    def getMaxDepth(self):
        return self.maxDepth


def main():
    print("PancakeSort")
    n = 5
    graph = PancakeGraph(n)
    start = time.time()
    pancake_sort = PancakeSort(graph, n)
    end = time.time()
    print(f"Minimal number of flips required for stack of {n} pancakes : {pancake_sort.getMaxDepth()}")
    print(f"The time of execution of above program is : {end - start}")


if __name__ == "__main__":
    main()
