class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_chars = Counter(s1)
        perm_chars = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            perm_chars[s2[r]] += 1
            if r - l + 1 < len(s1):
                continue
            if s1_chars == perm_chars:
                return True
            else:
                perm_chars[s2[l]] -= 1
                if perm_chars[s2[l]] == 0:
                    del perm_chars[s2[l]]
                l += 1

        return False