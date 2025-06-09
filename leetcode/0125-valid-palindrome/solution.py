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
