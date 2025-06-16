# 最長不重複子字串長度
# 使用滑動視窗與集合

def length_of_longest_substring(s: str) -> int:
    # 建立集合，儲存當前視窗內的字元（不重複）
    char_set = set()
    left = 0  # 左指標，表示當前視窗的起始位置
    max_length = 0  # 最長子字串長度
    n = len(s)  # 字串長度
    for right in range(n):  # right 為右指標，遍歷每個字元
        # 如果當前字元已在集合中，代表有重複，需移動左指標並移除集合內的字元
        while s[right] in char_set:
            char_set.remove(s[left])  # 移除左指標的字元，縮小視窗
            left += 1  # 左指標右移一格
        char_set.add(s[right])  # 將當前字元加入集合，維持視窗內無重複
        max_length = max(max_length, right - left + 1)  # 更新最大長度
    return max_length  # 回傳最長長度


if __name__ == "__main__":
    # 範例測試
    print(length_of_longest_substring("abcabcbb"))  # 輸出 3
    print(length_of_longest_substring("bbbbb"))     # 輸出 1
    print(length_of_longest_substring("pwwkew"))    # 輸出 3
