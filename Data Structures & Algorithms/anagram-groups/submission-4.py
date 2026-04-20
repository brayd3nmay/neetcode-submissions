class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            char_count = [0] * 26
            for c in s:
                pos = ord('a') - ord(c)
                char_count[pos] += 1

            groups[tuple(char_count)].append(s)

        return list(groups.values())