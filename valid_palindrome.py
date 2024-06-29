def isPalindrome(s: str) -> bool:
   a = ''.join(filter(str.isalnum,s))
   a = a.lower()
   if a == a[::-1]:
       return True
   else:
       return False

