import re
def palindrome(string):
    modStr = re.sub('\W', '', string.lower())
    print modStr
    if modStr == modStr[::-1]:
        return True
    else:
        return False
    
print palindrome(u" ab*cdc -Ba ")