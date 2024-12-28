# URL 
# https://leetcode.com/problems/is-subsequence/description/

def isSubsequence(s: str, t: str) -> bool:
    if(s == ""):
        return True
    if(t == ""):
        return False
    startingPoint = 0
    for value in range(len(s)):
        for secondValue in range(startingPoint ,len(t)):
            if s[value] == t[secondValue]:
                print(f"Found a match. {s[value]} == {t[secondValue]}")
                startingPoint = secondValue + 1
                if(value == len(s)-1):
                    return True
                else:
                    break
            if(secondValue == len(t)-1):
                return False

print(f"Test 1: {isSubsequence("abc", "ahbgdc") == True}")
print(f"Test 2: {isSubsequence("axc", "ahbgdc") == True}")