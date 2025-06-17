# 567. Permutation in String

> 難度：Medium 🟡

> 題型：Sliding Window & Hashing

## 題目描述
> 給定兩個字串 s1 和 s2，請判斷 s2 是否包含 s1 的任一排列（permutation）作為其子字串。
> 換句話說，若 s2 中存在一個子字串，其字元組合與 s1 完全相同（順序可不同），則回傳 True，否則回傳 False。

> Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
> In other words, return true if one of s1's permutations is the substring of s2.

---

## 💡 解題思路
1. 使用滑動視窗（Sliding Window）技巧，視窗大小為 s1 長度。
2. 建立兩個字典（或陣列）：分別記錄 s1 的字元計數與當前視窗的字元計數。
3. 每次移動視窗時，更新視窗字元計數，並與 s1 的字元計數比較。
4. 若兩者相同，代表找到一個排列，回傳 True。
5. 若遍歷完 s2 都沒找到，回傳 False。

> ⚠️ 注意：s1 和 s2 只包含小寫英文字母，且 s1 長度不會大於 s2。

---

## 📚 範例

| 輸入                | 輸出   |
|---------------------|--------|
| s1 = "ab", s2 = "eidbaooo" | True   |
| s1 = "ab", s2 = "eidboaoo" | False  |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 字典（dict）或陣列（長度 26）         |
| 時間複雜度   | O(n)（n 為 s2 長度）                  |
| 空間複雜度   | O(1)（僅 26 個字母的計數）            |
| 優點         | 高效、僅需一次遍歷 s2                 |
| 缺點         | 需額外空間儲存字元計數                |

---

## ⚡ 程式碼實作（Python）

```python
# 判斷 s2 是否包含 s1 的排列
from collections import Counter  # 匯入 Counter 用於字元計數

def checkInclusion(s1: str, s2: str) -> bool:
    s1_len = len(s1)  # 取得 s1 長度
    s2_len = len(s2)  # 取得 s2 長度
    if s1_len > s2_len:
        return False  # 若 s1 較長，直接回傳 False

    s1_count = Counter(s1)  # 計算 s1 各字元出現次數
    window = Counter(s2[:s1_len])  # 初始化視窗，計算前 s1_len 個字元

    # Counter 物件支援 == 比較，會比對每個 key-value 是否完全相同
    # 即使 window 有 value 為 0 的 key，Counter 會自動忽略，不影響比較正確性
    if window == s1_count:
        return True  # 若初始視窗即符合，回傳 True

    for i in range(s1_len, s2_len):  # 從 s1_len 開始滑動視窗
        window[s2[i]] += 1  # 新增右側字元（視窗右移，加入新字元）
        window[s2[i - s1_len]] -= 1  # 移除左側字元（視窗左端字元計數減 1）
        # 若某字元計數為 0，建議用 del 移除，讓 Counter 更精簡、比較更快
        # 但不移除也不影響正確性，因為 Counter 比較時會自動忽略 value 為 0 的 key
        if window[s2[i - s1_len]] == 0:
            del window[s2[i - s1_len]]  # 若計數為 0，移除該字元
        if window == s1_count:
            return True  # 若視窗計數符合，回傳 True
    return False  # 遍歷完都沒找到，回傳 False

if __name__ == "__main__":
    # 範例測試
    print(checkInclusion("ab", "eidbaooo"))  # True
    print(checkInclusion("ab", "eidboaoo"))  # False

# 補充說明：
# - Counter 是 dict 的子類別，可以用索引方式賦值與取值。
# - Counter 沒有 hash，不能當 set 元素或 dict key，但支援內容比較（==）。
# - 用 del 移除 value 為 0 的 key 主要是讓 Counter 更精簡，提升效能，非正確性所必須。
```
