class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        if not N: return 0
        if len(mines) == N * N: return 0
        self.mmset = []
        for i in range(N):
            self.mmset.append([True for j in range(N)])
        for p in mines:
            self.mmset[p[0]][p[1]] = False

        maxmin = 0
        # using rolling arrays to achieve DP.
        # the 4 elements tuple means length of 1s for [North, West, South, East].
        oldline = [[0, 0, 0, 0] for _ in range(N)]
        for i in range(N):
            newline = [[0, 0, 0, 0] for _ in range(N)]
            for j in range(0, N):
                if not self.mmset[i][j]:
                    continue
                if N - j <= maxmin or N - i <= maxmin:
                    continue
                newline[j][0] = oldline[j][0] + 1

                if j == 0:
                    newline[j][1] = 1
                else:
                    newline[j][1] = newline[j - 1][1] + 1

                if oldline[j][2] == 0:
                    for newi in xrange(i, N):
                        if self.mmset[newi][j]:
                            newline[j][2] += 1
                        else:
                            break
                else:
                    newline[j][2] = oldline[j][2] - 1

                if j == 0 or newline[j - 1][3] == 0:
                    for newj in xrange(j, N):
                        if self.mmset[i][newj]:
                            newline[j][3] += 1
                        else:
                            break
                else:
                    newline[j][3] = newline[j - 1][3] - 1

                maxmin = max(min(newline[j]), maxmin)

            oldline = newline
        return maxmin