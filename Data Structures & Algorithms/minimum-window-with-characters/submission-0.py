class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        substring = {} 
        t_freq = Counter(t)
        char_freq = {} 
        l = 0
        for r in range(len(s)):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            if all(k in char_freq and char_freq[k] >= t_freq[k] for k in t_freq):
                while all(k in char_freq and char_freq[k] >= t_freq[k] for k in t_freq):
                    char_freq[s[l]] -= 1
                    if char_freq[s[l]] == 0:
                        del char_freq[s[l]]
                    l += 1
                substring[r - l + 2] = s[l - 1: r + 1]

        if substring:
            min_length = min(substring)
            return substring[min_length]
        else:
            return ""