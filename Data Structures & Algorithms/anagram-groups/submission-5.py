class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for c in s:
                alpha_char = ord('a') - ord(c)
                chars[alpha_char] += 1
            anagrams[tuple(chars)].append(s)

        return list(anagrams.values())