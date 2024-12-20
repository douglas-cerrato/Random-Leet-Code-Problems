# URL
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/


def gcdOfStrings(str1: str, str2: str) -> str:
    lenStr1, lenStr2 = len(str1), len(str2)
    if lenStr1 % lenStr2 != 0:
        if lenStr1 % (int(lenStr2/2)) != 0:
            return ""
        else:
            j = 0
            for i in range(lenStr1):
                if(str1[i] != str2[j]):
                    return ""
                if(j == int((lenStr2/2) - 1)):
                    j = 0
                else:
                    j+=1                
            return str2[:int(lenStr2/2)]
    else:
        j = 0
        for i in range(lenStr1):
            if(str1[i] != str2[j]):
                return ""
            if(j == lenStr2 - 1):
                j = 0
            else:
                j+=1

        return str2                         
    
print(f"Test 1: {gcdOfStrings("ABCABC","ABC") == "ABC"}")
print(f"Test 2: {gcdOfStrings("ABABAB","ABAB") == "AB"}")
print(f"Test 3: {gcdOfStrings("LEET","CODE") == ""}")
