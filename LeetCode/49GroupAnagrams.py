'''
Python 3
https://leetcode.com/problems/group-anagrams/

By Soleil Vivero
09/09/23
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        elif s == t:
            return True
        else:
            count = defaultdict(int)

            for sChar, tChar in zip(s, t):
                count[sChar] += 1
                count[tChar] -= 1
            
            for val in count.values():
                if val != 0:
                    return False
            
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagrams = []
        anagrams = set()

        while strs:
            cols = []

            if strs[-1] not in anagrams:
                cols.append(strs.pop())

                for s in strs:
                    if self.isAnagram(s, cols[0]):
                        anagrams.update([s])
                        cols.append(s)

                groupedAnagrams.append(cols)

            else:
                strs.pop()

        return groupedAnagrams