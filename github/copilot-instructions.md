---
applyTo: "**"
---
# LeetCode 問題蒐集與解答儲存專案指引

本專案專為 LeetCode 題目蒐集與解答儲存設計，請依下列規範產生、整理與回覆所有相關內容：

## 題目內容要求
- 每個題目皆需包含：
  - 題目描述（需包含中英文分段表達，標註難度，格式如：`> 難度：Easy 🟢`）
  - 題型（如：`> 題型：Array & Hashing`，請標註於標題下方）
  - 解題思路（說明解法邏輯與步驟，建議用有序清單或條列）
  - 範例（表格呈現輸入與輸出）
  - 演算法與資料結構分析（表格呈現所用演算法、資料結構、時間與空間複雜度、優缺點等）
  - 程式碼（以 Python 為主，使用 code block 包覆，並加上標題）
- 預設以 Python 為主要解題語言，所有程式碼範例請優先提供 Python。
- 所有程式碼範例，請於每一行加上中文註解，說明該行的思路與作用，讓讀者能逐行理解解法邏輯。
- 回覆時，請依據下方 README.md 樣板格式產生內容，並善用 emoji、表格、分段、提示區塊等讓版面活潑易讀。

## README.md 樣板

````markdown
# 題目名稱（如：217. Contains Duplicate）

> 難度：Easy 🟢

## 題目描述
> 題目原文或簡要說明

---

## 💡 解題思路
1. 步驟一
2. 步驟二
3. ...

> ⚠️ 重要提示或注意事項可用 blockquote 呈現

---

## 📚 範例

| 輸入 | 輸出 |
|------|------|
| ...  | ...  |

---

## 🔍 演算法與資料結構分析

| 項目         | 說明                |
|--------------|---------------------|
| 使用資料結構 | ...                 |
| 時間複雜度   | ...                 |
| 空間複雜度   | ...                 |
| 優點         | ...                 |
| 缺點         | ...                 |

---

## ⚡ 程式碼實作（Python）

```python
# Python 程式碼
```
````

## 資料夾結構建議

```
leetcode/
  ├── 0001-two-sum/
  │     ├── README.md      # 題目描述、解題思路、演算法分析、程式碼
  │     ├── solution.py    # Python 解答（主要）
  ├── 0002-add-two-numbers/
  │     └── ...
  └── ...
```

---

- 本 instructions.md 會自動套用於所有檔案與 Copilot Chat 產生的內容。
- 請嚴格遵循上述規範，確保所有解答具備完整說明與分析，並有活潑、分段明確、易讀的版面。
- 如有更新，請同步修正本 instructions.md。
- 新增規範：所有 solution.py 檔案需加上 `if __name__ == "__main__":` 程式進入點與範例測試資料，方便直接執行測試。
