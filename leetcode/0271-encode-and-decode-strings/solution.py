class Codec:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
