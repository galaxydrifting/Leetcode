# 217. Contains Duplicate

> 題型：Array & Hashing

> 難度：Easy 🟢

## 題目描述
> Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
>
> 給定一個整數陣列 nums，若陣列中有任何數值至少出現兩次，則回傳 true；若每個元素皆不相同，則回傳 false。

---

## 💡 解題思路
1. 利用集合（set）特性：集合中的元素不會重複。
2. 將 nums 轉為 set，若 set 的長度小於原陣列，代表有重複元素。
3. 也可用迴圈與 set 判斷，遇到重複即提前回傳 true。

> ⚠️ 若遇到重複元素可直接回傳 true，無需檢查完整陣列。

---

## 📚 範例

| 輸入 | 輸出 |
|----------------------|-------|
| nums = [1,2,3,1]     | true  |
| nums = [1,2,3,4]     | false |
| nums = [1,1,1,3,3,4,3,2,4,2] | true |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 集合（set）         |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(n)                |
| 優點         | 簡潔、效率高        |
| 缺點         | 需額外 O(n) 空間    |

---
