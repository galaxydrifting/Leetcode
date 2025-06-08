---
applyTo: "**"
---
# LeetCode 問題蒐集與解答儲存專案指引

本專案專為 LeetCode 題目蒐集與解答儲存設計，請依下列規範產生、整理與回覆所有相關內容：

## 題目內容要求
- 每個題目皆需包含：
  - 題目描述
  - 解題思路（說明解法邏輯與步驟）
  - 演算法與資料結構分析（包含所用演算法、資料結構、時間與空間複雜度、優缺點等）
  - 程式碼（以 Python 為主）
- 預設以 Python 為主要解題語言，所有程式碼範例請優先提供 Python。
- 回覆時，請依據下方 README.md 樣板格式產生內容。

## README.md 樣板

```
# 題目名稱（如：217. Contains Duplicate）

## 題目描述
> 題目原文或簡要說明

## 解題思路
- 說明解法邏輯、步驟與選擇原因

## 演算法與資料結構分析
- 使用的演算法與資料結構
- 時間複雜度、空間複雜度
- 優缺點與適用情境

## 程式碼實作（Python）
```python
# Python 程式碼
```

## 資料夾結構建議

```
leetcode/
  ├── 0001-two-sum/
  │     ├── README.md      # 題目描述、解題思路、演算法分析、程式碼
  │     ├── solution.py    # Python 解答（主要
  ├── 0002-add-two-numbers/
  │     └── ...
  └── ...
```

---

## README.md 範例

以下為 217. Contains Duplicate 的完整範例，請依此格式撰寫：

````markdown
# 217. Contains Duplicate

## 題目描述
> Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
> 給定一個整數陣列 nums，若陣列中有任何數值至少出現兩次，則回傳 true；若每個元素皆不相同，則回傳 false。

## 解題思路
- 利用集合（set）特性：集合中的元素不會重複。
- 將 nums 轉為 set，若 set 的長度小於原陣列，代表有重複元素。
- 也可用迴圈與 set 判斷，遇到重複即提前回傳 true。

## 演算法與資料結構分析
- 使用的演算法與資料結構：集合（set）
- 時間複雜度：O(n)，n 為陣列長度（set 插入與查找均為 O(1)）
- 空間複雜度：O(n)，最壞情況下 set 需存放所有元素
- 優點：簡潔、效率高，適用於需快速判斷重複元素的情境
- 缺點：需額外 O(n) 空間

## 程式碼實作（Python）
```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# 進階寫法：遇到重複即提前回傳
# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
````

---

- 本 instructions.md 會自動套用於所有檔案與 Copilot Chat 產生的內容。
- 請嚴格遵循上述規範，確保所有解答具備完整說明與分析。
- 如有更新，請同步修正本 instructions.md。
