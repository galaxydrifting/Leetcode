from collections import defaultdict  # 匯入 defaultdict 方便計數


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # 用來記錄視窗內每個字母的出現次數
        res = 0  # 最長長度結果
        l = 0  # 視窗左邊界
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)  # 右邊界字母計數加一
            # 若需要替換的字母數超過 k，縮小左邊界
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1  # 左邊界字母計數減一
                l += 1  # 左邊界右移
            res = max(res, r - l + 1)  # 更新最大長度
        return res  # 回傳結果


if __name__ == "__main__":
    # 範例測試
    solution = Solution()
    print(solution.characterReplacement("ABAB", 2))      # 輸出 4
    print(solution.characterReplacement("AABABBA", 1))  # 輸出 4
