# 424. Longest Repeating Character Replacement

> 難度：Medium 🟡

> 題型：Sliding Window & String

## 題目描述
> 給定一個字串 s 和一個整數 k，你可以最多將 k 個字元替換成其他大寫英文字母。請回傳經過最多 k 次替換後，最長的連續相同字母子字串長度。

> Given a string s and an integer k, you can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

---

## 💡 解題思路
1. 使用滑動視窗（Sliding Window）技巧，維護一個區間 [l, r]。
2. 用一個字典 count 記錄視窗內每個字母的出現次數。
3. 當視窗長度減去視窗內最多的字母數量大於 k 時，代表需要超過 k 次替換，需縮小左邊界 l。
4. 每次更新最大視窗長度。

> ⚠️ 注意：每次都用 max(count.values()) 取得目前視窗內最多的字母數量。

---

## 📚 範例

| 輸入         | 輸出 |
|--------------|------|
| s = "ABAB", k = 2 | 4    |
| s = "AABABBA", k = 1 | 4    |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 字典（紀錄字母次數）、滑動視窗         |
| 時間複雜度   | O(26 * n) ≈ O(n)，n 為字串長度。每次 while 需計算 max(count.values())，最壞 O(26) |
| 空間複雜度   | O(1)，最多 26 個大寫英文字母           |
| 優點         | 實作簡單，直觀易懂                     |
| 缺點         | 每次 while 需重新計算 max，理論上比最佳解慢一點，但實務上差異不大 |

---

## ⚡ 程式碼實作（Python，class 寫法）

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

# 範例測試
sol = Solution()
print(sol.characterReplacement("ABAB", 2))      # 輸出 4
print(sol.characterReplacement("AABABBA", 1))  # 輸出 4
```
