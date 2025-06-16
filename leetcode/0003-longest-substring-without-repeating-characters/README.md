# 3. Longest Substring Without Repeating Characters

> 難度：Medium 🟡

> 題型：Sliding Window & Hash Table

## 題目描述
> 給定一個字串 s，請找出不含重複字元的最長子字串的長度。

> Given a string s, find the length of the longest substring without repeating characters.

---

## 💡 解題思路
1. 使用滑動視窗（Sliding Window）技巧，維護一個不含重複字元的子字串區間。
2. 使用哈希表（字典）記錄每個字元最後出現的位置。
3. 當遇到重複字元時，將左指標移動到該重複字元上次出現位置的下一格。
4. 每次更新最大長度。

> ⚠️ 注意：左指標只會往右移動，且每個字元最多只會被檢查兩次，確保時間複雜度為 O(n)。

---

## 📚 範例

| 輸入      | 輸出 |
|-----------|------|
| "abcabcbb"| 3    |
| "bbbbb"   | 1    |
| "pwwkew"  | 3    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                         |
|--------------|------------------------------|
| 使用資料結構 | 集合（set）、雙指標        |
| 時間複雜度   | O(n)                         |
| 空間複雜度   | O(k)，k 為字元種類數         |
| 優點         | 單次遍歷、效率高              |
| 缺點         | 需額外空間存儲視窗內字元      |

---

## ⚡ 程式碼實作（Python）

```python
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
```
