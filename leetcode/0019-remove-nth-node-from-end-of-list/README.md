# 19. Remove Nth Node From End of List

## 題目描述 (Description)

給定一個連結串列的頭節點 `head`，請移除倒數第 `n` 個節點，並返回修改後的連結串列頭節點。

Given the head of a linked list, remove the nth node from the end of the list and return its head.

---

## 解題思路 (Approach) 🧠

1. 使用雙指針（快慢指針）技巧：
   - 先讓快指針先走 `n` 步。
   - 然後快慢指針一起走，直到快指針到達尾端。
   - 此時慢指針的下一個節點就是要被移除的節點。
2. 處理特殊情況：
   - 若要移除的是頭節點，需特別處理。

---

## 演算法分析 (Complexity Analysis) 📊

- 時間複雜度：O(L)，L 為連結串列長度。
- 空間複雜度：O(1)，只使用了常數額外空間。

---

## 參考範例 (Example)

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

---

## Tags
- Linked List
- Two Pointers
- Medium
