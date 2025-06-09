from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())


if __name__ == "__main__":
    # 測試範例
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(groupAnagrams([""]))
    print(groupAnagrams(["a"]))
