# 1. Two Sum

> 難度：Easy 🟢

## 題目描述
> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
> You can return the answer in any order.
>
> 給定一個整數陣列 nums 和一個整數 target，請回傳陣列中兩個數字的索引，使得它們的和等於 target。
> 每個輸入只會有一組解，且同一元素不可重複使用。

## 解題思路
- 使用哈希表（字典）記錄已遍歷過的數字及其索引。
- 每次遍歷時，計算 target 與當前數字的差值（complement），檢查該差值是否已存在於哈希表中。
- 若存在，代表找到答案，直接回傳兩個索引。
- 若不存在，將當前數字與索引加入哈希表，繼續遍歷。
- 由於題目保證有唯一解，找到即回傳。

## 演算法與資料結構分析
- 使用的演算法與資料結構：哈希表（dict）
- 時間複雜度：O(n)，n 為陣列長度（每個元素最多查找與插入一次）
- 空間複雜度：O(n)，最壞情況下哈希表需存放所有元素
- 優點：查找與插入皆為 O(1)，效率高，適用於需快速查找配對的情境
- 缺點：需額外 O(n) 空間

## 程式碼實作（Python）
```python
def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
```
