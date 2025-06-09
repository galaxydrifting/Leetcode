# 0036. Valid Sudoku

> 難度：Medium 🟡

> 題型：Array & Hashing

## 題目描述
> 給定一個 9 x 9 的數獨盤面，判斷其是否為有效的數獨。只需檢查已填寫的格子是否符合以下規則：
> 1. 每一行必須包含 1-9，且不可重複。
> 2. 每一列必須包含 1-9，且不可重複。
> 3. 每個 3 x 3 的子區塊必須包含 1-9，且不可重複。
>
> Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
>
> 1. Each row must contain the digits 1-9 without repetition.
> 2. Each column must contain the digits 1-9 without repetition.
> 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
>
> Note:
>
> A Sudoku board (partially filled) could be valid but is not necessarily solvable.
> Only the filled cells need to be validated according to the mentioned rules.

---

## 💡 解題思路
1. 分別檢查每一行、每一列、每個 3x3 子區塊，確保已填寫的數字不重複。
2. 可用三個集合陣列分別記錄每行、每列、每區塊已出現的數字。
3. 遍歷整個盤面，對每個非空格子，檢查其數字是否已在對應的行、列、區塊出現過。
4. 若有重複則回傳 False，否則遍歷結束回傳 True。

> ⚠️ 只需檢查已填寫的格子（即非 '.' 的格子），不需判斷是否可解。

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| board = [<br>["5","3",".",".","7",".",".",".","."]<br>["6",".",".","1","9","5",".",".","."]<br>[".","9","8",".",".",".",".","6","."]<br>["8",".",".",".","6",".",".",".","3"]<br>["4",".",".","8",".","3",".",".","1"]<br>["7",".",".",".","2",".",".",".","6"]<br>[".","6",".",".",".",".","2","8","."]<br>[".",".",".","4","1","9",".",".","5"]<br>[".",".",".",".","8",".",".","7","9"]] | True |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | 陣列、集合          |
| 時間複雜度   | O(n²)，但本題 n=9 固定視為 O(1) |
| 空間複雜度   | O(1)                |
| 優點         | 直觀、易於實作      |
| 缺點         | 盤面固定，無法擴展  |

---

## ⚡ 程式碼實作（Python）

```python
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in rows[i] or num in cols[j] or num in boxes[(i//3)*3 + j//3]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[(i//3)*3 + j//3].add(num)
        return True
```
