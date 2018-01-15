class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dmap = collections.defaultdict(list)
        for i, x in enumerate(B):
            dmap[x].append(i)
        return [dmap[x].pop() for x in A]