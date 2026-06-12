class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        shortest_substring = ""

        valid_idx = [] # queue of indexes in s, where s[i] == t[i]

        window, t_counts = {}, {}
        for i in range(len(t)):
            t_counts[t[i]] = t_counts.get(t[i], 0) + 1

        have, need = 0, len(t_counts)
        l = 0
        for r in range(len(s)):
            if s[r] in t_counts:
                window[s[r]] = window.get(s[r], 0) + 1
                valid_idx.append(r)

                if window[s[r]] == t_counts[s[r]]:
                    have += 1
                
            while have == need:
                l = valid_idx.pop(0)
                shortest_substring = s[l: r + 1] if r - l + 1 < len(shortest_substring) or shortest_substring == "" else shortest_substring
                window[s[l]] -= 1

                if window[s[l]] < t_counts[s[l]]:
                    have -= 1

        return shortest_substring