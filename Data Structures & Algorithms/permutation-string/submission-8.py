class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = [0] * 26
        for char in s1:
            s1_counts[ord(char) - ord("a")] += 1
        s2_counts = [0] * 26

        l = 0
        for r in range(len(s2)):
            s2_counts[ord(s2[r]) - ord("a")] += 1    

            l = r - len(s1) + 1
            if l < 0:
                continue
            
            if s1_counts == s2_counts:
                return True

            s2_counts[ord(s2[l]) - ord("a")] -= 1
        return False
