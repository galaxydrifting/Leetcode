# 242. Valid Anagram

> 題型：Array & Hashing

> 難度：Easy 🟢

## 題目描述
> Given two strings s and t, return true if t is an anagram of s, and false otherwise.
>
> 給定兩個字串 s 和 t，若 t 為 s 的字母重組（anagram），則回傳 true，否則回傳 false。

---

## 💡 解題思路
1. 字母重組的定義：兩字串長度相同，且每個字母出現的次數皆相同。
2. 最簡單的做法：將兩字串排序後比較是否相等。
3. 進階做法：使用雜湊表（dict 或 collections.Counter）統計每個字母出現次數，最後比較兩字串的字母計數是否一致。

> ⚠️ 僅當兩字串長度相同且字母分布完全一致時才為 anagram。

---

## 📚 範例

| 輸入           | 輸出  |
|----------------|-------|
| s = "anagram", t = "nagaram" | true  |
| s = "rat", t = "car"         | false |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 排序、雜湊表（dict/Counter）|
| 時間複雜度   | O(n log n)（排序法），O(n)（Counter 法）|
| 空間複雜度   | O(1)（僅限小寫字母），否則 O(n) |
| 優點         | 排序法簡單直觀，Counter 法效率高 |
| 缺點         | 排序法在字串很長時較慢，Counter 法需額外空間 |

---

## ⚡ 程式碼實作（Python）

```python
def isAnagram(s, t):
    return sorted(s) == sorted(t)

# 進階寫法：使用 Counter
# from collections import Counter
# def isAnagram(s, t):
#     return Counter(s) == Counter(t)
```
