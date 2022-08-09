class PancakeGraph:

    def __init__(self, n):
        self.n = n
        self.V = self.permutations([i for i in range(1, self.n + 1)])
        self.adjacencyList = {tuple(v): [] for v in self.V}
        self.addEdges()

    def permutations(self, arr):
        res = []
        n = len(arr)

        def dfs(curr, arrLeft):
            if len(curr) == n:
                res.append(curr)

            else:
                for i in range(len(arrLeft)):
                    dfs(curr + [arrLeft[i]], arrLeft[:i] + arrLeft[i+1:])

        dfs([], arr)
        return res

    def flip(self, arr, k):
        return tuple(arr[::-1][-k:] + arr[k:])

    def addEdges(self):
        for v in self.V:
            for k in range(2, self.n + 1):
                self.adjacencyList[tuple(v)].append(self.flip(v, k))

    def showAdjacencyList(self):
        print(self.adjacencyList)


