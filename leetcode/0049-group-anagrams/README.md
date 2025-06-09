# 49. Group Anagrams

> 難度：Medium 🟡

> 題型：Hash Table & String

## 題目描述
> 給定一個字串陣列 `strs`，請將所有的異位詞（Anagrams）分組。你可以以任意順序返回答案。

> Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

---

## 💡 解題思路
1. 使用哈希表（字典）來分組異位詞。
2. 對每個字串進行排序，排序後的字串作為 key，將原字串加入對應的 value list。
3. 最後回傳所有 value list。

> ℹ️ 排序後的字串能唯一標識一組異位詞。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| ["eat","tea","tan","ate","nat","bat"] | [["eat","tea","ate"],["tan","nat"],["bat"]] |
| [""] | [[""]] |
| ["a"] | [["a"]] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 字典（哈希表）                        |
| 時間複雜度   | O(N * KlogK)，N 為字串數，K 為最長字串長度 |
| 空間複雜度   | O(NK)                                 |
| 優點         | 分組效率高，實作簡單                   |
| 缺點         | 需對每個字串排序，排序成本較高         |

---

## ⚡ 程式碼實作（Python）

```python
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())
```
