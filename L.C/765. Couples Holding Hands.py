class Solution(object):
    def normalize(self, row):
        crow = []
        for x in range(len(row)):
            sm, bg = row[x][0], row[x][1]
            if sm > bg: sm, bg = bg, sm
            if bg % 2 and sm + 1 == bg: continue
            crow.append((sm, bg))
        shift = {v : i for i, v in enumerate(sorted(reduce(operator.add, crow, ())))}
        crow = sorted([shift[sm], shift[bg]] for sm, bg in crow)
        return crow

    def solve(self, row):
        row = self.normalize(row)
        if not row: return 0
        locs = {}
        for idx, (sm, bg) in enumerate(row):
            locs[sm], locs[bg] = idx * 2, idx * 2 + 1
        row[locs[1] / 2][locs[1] % 2] = row[0][1]
        return self.solve(row[1:]) + 1

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        return self.solve([[row[x], row[x + 1]] for x in range(0, len(row), 2)])
