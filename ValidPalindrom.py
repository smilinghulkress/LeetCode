"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""

#keep two pointers and check the alnum at each character
class Solution(object):
    def isPalindrome(self, s):
        i = 0
        j = len(s)-1
        while i <j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
            elif not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1

        return True


        # if s == '':
        #     return True
        # s= list(s.lower())
        # for c in s:
        #     if not c.isalnum():
        #         print(c)
        #         s.remove(c)
        #
        # print("s=", str(s))

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))

