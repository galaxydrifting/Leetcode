# LeetCode Solutions

本專案收錄 LeetCode 題目的 Python 解答，並以簡潔、易讀為原則。每個題目皆有獨立資料夾，包含題目說明與解題程式碼。

## 目錄結構

```
leetcode/
  └── 題號-題名/
        ├── README.md   # 題目說明（可選）
        └── solution.py # 解題程式碼
main.py                # 入口或測試用（如有）
```

## 範例

以 [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) 為例：

- `leetcode/0217-contains-duplicate/solution.py`：
  - 提供兩種解法：
    1. 直接比較長度與 set 長度。
    2. 使用 set 儲存已見過的數字，遇到重複即提前回傳。

## 如何貢獻

1. Fork 本專案
2. 新增或修改解答
3. 提交 Pull Request

## 環境說明

- Python 3 已預先安裝於 dev container

---

歡迎一同討論、優化解法！
