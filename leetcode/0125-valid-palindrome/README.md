# 125. Valid Palindrome

> 難度：Easy 🟢

> 題型：Two Pointers

## 題目描述
> 給定一個字串 s，若將所有大寫字母轉為小寫並移除所有非英數字字元後，該字串正著讀與反著讀皆相同，則稱為回文（palindrome）。請判斷 s 是否為回文。
>
> A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

---

## 💡 解題思路
1. 使用雙指標（Two Pointers）分別從字串頭尾向中間靠攏。
2. 跳過所有非英數字字元。
3. 比較兩指標所指字元（皆轉為小寫），若不同則回傳 False。
4. 若所有比對皆通過，則回傳 True。

> ⚠️ 注意：需考慮空字串、僅有非英數字字元等特殊情況。

---

## 📚 範例

| 輸入                | 輸出   |
|---------------------|--------|
| "A man, a plan, a canal: Panama" | true   |
| "race a car"         | false  |
| " "                  | true   |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 雙指標（Two Pointers）      |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(1)                        |
| 優點         | 不需額外空間，效率高        |
| 缺點         | 需注意字元過濾與大小寫處理  |

---

## ⚡ 程式碼實作（Python）

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    # 更簡潔的寫法（非 two pointer，僅供參考）
    # def isPalindrome(self, s: str) -> bool:
    #     filtered = [c.lower() for c in s if c.isalnum()]
    #     return filtered == filtered[::-1]
```
