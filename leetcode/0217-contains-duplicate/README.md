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
```