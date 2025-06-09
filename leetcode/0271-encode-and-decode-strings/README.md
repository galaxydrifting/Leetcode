# 271. Encode and Decode Strings

> 難度：Medium 🟡

> 題型：String, Design

## 題目描述
> 設計一個演算法，將字串列表編碼為單一字串，並能將其解碼回原始的字串列表。
> 
> Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

---

## 💡 解題思路
1. 為避免分隔符衝突，對每個字串，先記錄其長度，再加上一個特殊分隔符（如 `#`），接著串上字串本身。
2. 編碼時，將每個字串轉為 `長度#字串` 形式，全部串接。
3. 解碼時，從頭掃描，遇到 `#` 前的數字即為長度，之後取出該長度的字串，重複直到結束。

> ⚠️ 注意：字串本身可包含任何字符，因此僅用長度分隔最安全。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| ["leet","code","!"] | "4#leet4#code1#!" |
| ["abc","","def"] | "3#abc0#3#def" |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 字串操作                    |
| 時間複雜度   | O(N)（N 為所有字元總長度）  |
| 空間複雜度   | O(N)                        |
| 優點         | 不會因內容衝突導致解碼錯誤  |
| 缺點         | 編碼後字串長度略增           |

---

## ⚡ 程式碼實作（Python）

```python
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
```
