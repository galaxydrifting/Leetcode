# 76. Minimum Window Substring

> 難度：Hard 🔴

> 題型：Sliding Window & Hash Table

## 題目描述
> 給定兩個字串 s 和 t，分別長度為 m 和 n，請找出 s 中最短的子字串，使得 t 中的每個字元（包含重複）都至少出現一次於該子字串中。若無解，請回傳空字串 ""。

> Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

---

## 💡 解題思路
1. 使用兩個指標（左右）維護一個滑動視窗，初始都在字串開頭。
2. 用一個字典記錄 t 中每個字元需要的數量。
3. 右指標向右擴展視窗，遇到 t 中的字元就減少需求數量。
4. 當所有需求都滿足時，嘗試移動左指標縮小視窗，並更新最小長度。
5. 若左指標移動導致需求不滿足，則右指標繼續擴展。
6. 最後回傳最小視窗的子字串。

> ⚠️ 注意：t 可能包含重複字元，需正確處理每個字元的需求數量。

---

## 📚 範例

| 輸入                | 輸出   |
|---------------------|--------|
| s = "ADOBECODEBANC", t = "ABC" | "BANC" |
| s = "a", t = "a"             | "a"    |
| s = "a", t = "aa"            | ""     |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                                  |
|--------------|---------------------------------------|
| 使用資料結構 | 雙指標、Hash Table（字典）             |
| 時間複雜度   | O(m + n)（m 為 s 長度，n 為 t 長度）   |
| 空間複雜度   | O(n)（t 中不同字元數量）               |
| 優點         | 只需一次遍歷 s，效率高                 |
| 缺點         | 需額外字典記錄視窗狀態，實作較繁瑣     |

---

## ⚡ 程式碼實作（Python）

```python
# 最小覆蓋子字串演算法（Two Pointers 寫法）
from collections import Counter  # 匯入 Counter 用於計算字元出現次數

def min_window(s: str, t: str) -> str:
    counter_t = Counter(t)  # 統計 t 中每個字元需要的數量
    window = {}  # 用來記錄目前視窗內的字元數量
    need = len(counter_t)  # 需要滿足的不同字元種類數
    have = 0  # 目前已經滿足的字元種類數
    res = [-1, -1]  # 記錄最小視窗的左右邊界
    res_length = float("inf")  # 最小視窗長度，初始為無限大
    l = 0  # 左指標，視窗左邊界

    for r in range(len(s)):  # 右指標從頭到尾遍歷 s
        window[s[r]] = 1 + window.get(s[r], 0)  # 將 s[r] 加入視窗並更新數量
        if s[r] in counter_t and counter_t[s[r]] == window[s[r]]:  # 若該字元數量剛好滿足需求
            have += 1  # 已滿足的種類數 +1
        
        while have == need:  # 當所有需求字元都滿足
            if (r - l + 1) < res_length:  # 若當前視窗更小
                res = [l, r]  # 更新最小視窗邊界
                res_length = r - l + 1  # 更新最小長度
            window[s[l]] -= 1  # 移除左指標字元
            if s[l] in counter_t and window[s[l]] < counter_t[s[l]]:  # 若移除後不再滿足需求
                have -= 1  # 已滿足的種類數 -1
            l += 1  # 左指標右移

    l, r = res  # 取得最小視窗的左右邊界
    return s[l: r + 1] if res_length != float("inf") else ""  # 回傳結果

if __name__ == "__main__":
    # 範例測試
    print(min_window("ADOBECODEBANC", "ABC"))  # 輸出：BANC
    print(min_window("a", "a"))                # 輸出：a
    print(min_window("a", "aa"))               # 輸出：
```
