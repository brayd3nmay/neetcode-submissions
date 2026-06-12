class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        shortest_substring = ""
        valid_idx = [] # queue of indexes in s, where s[i] == t[i]
        window, t_counts = {}, {}
        for i in range(len(t)):
            t_counts[t[i]] = t_counts.get(t[i], 0) + 1
        print(f"[INIT] t_counts={t_counts}")
        have, need = 0, len(t_counts)
        print(f"[INIT] have={have}, need={need}")
        l = 0
        for r in range(len(s)):
            print(f"\n[OUTER] r={r}, s[r]={s[r]!r}, l={l}")
            if s[r] in t_counts:
                window[s[r]] = window.get(s[r], 0) + 1
                valid_idx.append(r)
                print(f"  [ADD] added s[r]={s[r]!r} -> window={window}")
                print(f"  [ADD] valid_idx={valid_idx}")
                if window[s[r]] == t_counts[s[r]]:
                    have += 1
                    print(f"  [HAVE++] window[{s[r]!r}]={window[s[r]]} == t_counts[{s[r]!r}]={t_counts[s[r]]} -> have={have}")
                else:
                    print(f"  [NO HAVE] window[{s[r]!r}]={window[s[r]]} vs t_counts[{s[r]!r}]={t_counts[s[r]]}")
                
            while have == need:
                prev = shortest_substring
                l = valid_idx.pop(0)
                shortest_substring = s[l: r + 1] if r - l + 1 < len(shortest_substring) or shortest_substring == "" else shortest_substring
                print(f"  [WHILE] have==need=={need}; l={l}, r={r}, candidate={s[l:r+1]!r}")
                print(f"  [WHILE] shortest: {prev!r} -> {shortest_substring!r}")
                print(f"  [POP] popped l={l}, valid_idx now={valid_idx}")
                window[s[l]] -= 1
                print(f"  [SHRINK] window[{s[l]!r}]-- -> window={window}")
                if window[s[l]] < t_counts[s[l]]:
                    have -= 1
                    print(f"  [HAVE--] window[{s[l]!r}]={window[s[l]]} != t_counts[{s[l]!r}]={t_counts[s[l]]} -> have={have}")
                else:
                    print(f"  [STILL VALID] window[{s[l]!r}]={window[s[l]]} == t_counts[{s[l]!r}]={t_counts[s[l]]}")
        print(f"\n[RETURN] {shortest_substring!r}")
        return shortest_substring