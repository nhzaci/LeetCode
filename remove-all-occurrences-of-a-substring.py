class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        idx = s.find(part)
        return self.removeOccurrences(
            s[:idx] + s[idx + len(part):],
            part
        ) if idx != -1 else s
