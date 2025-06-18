# 141. Linked List Cycle

> 題型：Linked List

> 難度：Easy 🟢

## 題目描述
> Given head, the head of a linked list, determine if the linked list has a cycle in it.
>
> There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
>
> Return true if there is a cycle in the linked list. Otherwise, return false.
>
> 給定一個連結串列的頭節點 head，判斷該連結串列是否有環。
>
> 如果連結串列中存在某個節點，可以通過不斷跟隨 next 指標再次到達，則表示該連結串列存在環。內部使用 pos 表示尾節點連接的節點索引（但 pos 不作為參數傳入）。
>
> 如果連結串列有環，返回 true；否則返回 false。

---

## 💡 解題思路
1. 使用快慢指針（Floyd's Tortoise and Hare）：
    - 設定兩個指針 slow 與 fast，slow 每次走一步，fast 每次走兩步。
    - 如果存在環，fast 最終會追上 slow（即兩者會相遇）。
    - 如果 fast 或 fast.next 為 None，則代表無環。
2. 也可用 set 記錄已訪問節點，若遇到重複節點則有環，但空間複雜度較高。

> ⚠️ 快慢指針法空間複雜度 O(1)，是最常見且高效的解法。

---

## 📚 範例

| 輸入 | 輸出 |
|----------------------|-------|
| head = [3,2,0,-4], pos = 1 | true  |
| head = [1,2], pos = 0      | true  |
| head = [1], pos = -1       | false |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 連結串列            |
| 時間複雜度   | O(n)                |
| 空間複雜度   | O(1)                |
| 優點         | 空間效率高，易於實作 |

---