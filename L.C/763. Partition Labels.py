class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        rangeDict = {}
        for i, c in enumerate(S):
            if c not in rangeDict: rangeDict[c] = [i, i]
            else: rangeDict[c][1] = i
        rangeList = sorted(rangeDict.values(), cmp = lambda x, y: x[0] - y[0] or y[1] - x[1])
        ans = []
        cmin = cmax = 0
        for start, end in rangeList:
            if start > cmax:
                ans.append(cmax - cmin + 1)
                cmin, cmax = start, end
            else: cmax = max(cmax, end)
        ans.append(cmax - cmin + 1)
        return ans