class UFDS:
    def __init__(self, size: int):
        self.size = size
        self.num_sets = size
        self.rank = [0 for i in range(size)]
        self.p = [i for i in range(size)]

    def findSet(self, i: int):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.findSet(self.p[i])
            return self.p[i]

    def isSameSet(self, i: int, j: int):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self, i: int, j: int):
        if not self.isSameSet(i, j):
            self.num_sets -= 1

            # get indices x and y
            x = self.findSet(i)
            y = self.findSet(j)

            # compare rank of both to see which tree to add to
            if self.rank[x] < self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1

    def getNumDisjointSets(self):
        return self.num_sets
