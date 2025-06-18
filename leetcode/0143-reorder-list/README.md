# 143. Reorder List

> 題型：Linked List

> 難度：Medium 🟠

## 題目描述
> You are given the head of a singly linked-list. The list can be represented as:
> L0 → L1 → … → Ln - 1 → Ln
>
> Reorder the list to be on the following form:
>
> L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
>
> You may not modify the values in the list's nodes. Only nodes themselves may be changed.
>
> 給定一個單向鏈結串列的頭節點 head，串列可表示為：
> L0 → L1 → … → Ln - 1 → Ln
>
> 請將串列重新排序為：
>
> L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
>
> 不可更改節點的值，只能改變節點本身的連結。

---

## 💡 解題思路
1. 使用快慢指針找到鏈結串列的中點，將串列一分為二。
2. 將後半段鏈結串列反轉。
3. 交錯合併前半段與反轉後的後半段。

---

## 📚 範例

| 輸入 | 輸出 |
|----------------------|----------------------|
| 1→2→3→4 | 1→4→2→3 |
| 1→2→3→4→5 | 1→5→2→4→3 |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 鏈結串列            |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(1)                |
| 優點         | 原地操作，無需額外空間 |
| 缺點         | 操作指標較繁瑣        |
