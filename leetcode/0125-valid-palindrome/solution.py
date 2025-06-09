class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    # 更簡潔的寫法（非 two pointer，僅供參考）
    # def isPalindrome(self, s: str) -> bool:
    #     filtered = [c.lower() for c in s if c.isalnum()]
    #     return filtered == filtered[::-1]


if __name__ == "__main__":
    # 測試案例：只含非英數字元，left 會一直加到 right
    s = "!!"
    sol = Solution()
    print(sol.isPalindrome(s))  # 預期 True

    # 測試案例：left 跳過非英數字元後等於 right
    s = "a@"
    print(sol.isPalindrome(s))  # 預期 True

    # 測試案例：left 跳過後大於 right
    s = "@#"
    print(sol.isPalindrome(s))  # 預期 True

    # 一般回文
    s = "A man, a plan, a canal: Panama"
    print(sol.isPalindrome(s))  # 預期 True

    # 非回文
    s = "race a car"
    print(sol.isPalindrome(s))  # 預期 False
