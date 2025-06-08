def isAnagram(s, t):
    return sorted(s) == sorted(t)

# 進階寫法：使用 Counter
# from collections import Counter
# def isAnagram(s, t):
#     return Counter(s) == Counter(t)
