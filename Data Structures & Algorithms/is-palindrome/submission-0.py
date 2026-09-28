class Solution:
    def isPalindrome(self, s: str) -> bool:

        while left < right:

            # checking the condition if there is space either in left / right
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

        