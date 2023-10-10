class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))  # Initialize each element as its own parent
        self.rank = [0] * n  # Rank for each element (used for union by rank)

    def find(self, x):
        # Find the representative of the set to which 'x' belongs (with path compression)
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        # Union two sets (with union by rank)
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Example usage:
if __name__ == "__main__":
    n = 6  # Number of elements
    uf = UnionFind(n)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(4, 5)

    # Check if two elements are in the same set
    print(uf.find(0) == uf.find(2))  # Output: True
    print(uf.find(1) == uf.find(3))  # Output: False
