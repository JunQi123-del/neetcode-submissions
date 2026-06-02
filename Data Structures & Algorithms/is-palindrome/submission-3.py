class Solution:
    def isPalindrome(self, s: str) -> bool:
        compare = ""

        for i in s:
            if i.isalnum():
                compare+=i
        print(f"{compare}")

        left = 0
        right = len(compare)-1

        while left<right:
            if compare[left].lower() == compare[right].lower():
                left+=1
                right-=1
            else:
                return False
        
        return True