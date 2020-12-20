class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        cleaned = ''.join(S.split('-')).upper()
        # remainder from division will give length of first
        length_of_first = len(cleaned) % K
        result = cleaned[:length_of_first]
        no_substrings = len(cleaned) // K
        for i in range(no_substrings):
            result += '-' + cleaned[i * K +
                                    length_of_first: i * K + K + length_of_first]
        if result and result[0] == '-':
            return result[1:]
        return result
