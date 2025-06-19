# 25. Reverse Nodes in k-Group

> 難度：Hard 🔴

## 題目描述
> 給定一個連結串列的頭節點 head，請你每 k 個一組反轉連結串列中的節點，並返回修改後的連結串列。
> k 是一個正整數，且小於或等於連結串列的長度。如果節點總數不是 k 的整數倍，則剩餘節點保持原樣。
> 你只能改變節點之間的連結，不能更改節點的值。

> Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
> k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
> You may not alter the values in the list's nodes, only nodes themselves may be changed.

> 題型：Linked List

---

## 💡 解題思路
1. 使用虛擬頭節點 dummy，方便處理頭部反轉與連接。
2. 每次以 groupPrev 為起點，尋找第 k 個節點 kth，若不足 k 個則結束。
3. 反轉 groupPrev.next 到 kth 節點這一段，並將反轉後的頭尾正確連接。
4. groupPrev 移動到本組反轉後的尾部，重複步驟 2-3。
5. 只更改節點連結，不更動節點值。

> ⚠️ 需特別注意指標操作，避免遺漏或錯誤連接節點。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| head = [1,2,3,4,5], k = 2 | [2,1,4,3,5] |
| head = [1,2,3,4,5], k = 3 | [3,2,1,4,5] |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                        |
|--------------|-----------------------------|
| 使用資料結構 | 連結串列                    |
| 時間複雜度   | O(n)                        |
| 空間複雜度   | O(1)（僅用常數額外空間）     |
| 優點         | 原地反轉，無需額外空間        |
| 缺點         | 邏輯較複雜，需注意指標操作    |

---

## 🧑‍💻 程式碼（Python，含註解）

```python
# ...請見 solution.py ...
```
