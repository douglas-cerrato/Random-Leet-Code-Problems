# URL 
# https://leetcode.com/problems/is-subsequence/description/

def isSubsequence(s: str, t: str) -> bool:
    if(s == ""): return True 
    if(s != "" and t == ""): return False
    pointerOne = 0
    pointerTwo = 0
    
    while pointerOne < len(s):
        for x in range(pointerTwo, len(t)):
            print(f"x is {x}")
            if(s[pointerOne] == t[pointerTwo]):
                print(f"Found a match. pointerOne is {pointerOne} and pointerTwo is {pointerTwo}")
                if(pointerOne == len(s) - 1):
                    print("Found a match for the last char in string s")
                    return True
                
                # Found a match, this means we move pointerOne to find a match for the next character in 
                # string s. We also move the pointer in string t to iterate one by one in that string
                # to look for a match    
                pointerOne+=1
                pointerTwo+=1
                break
            # print(f"pointerTwo is {pointerTwo} and len(t)-1 is {len(t)-1}")
            # if(pointerTwo == len(t)-1):
            #     # We have hit the end of string t without finding a match 
            #     return False
            
            
            
            # Iterating through the next position in pointer Two
            pointerTwo+=1          
        print(f"pointerTwo is {pointerTwo} and len(t)-1 is {len(t)-1}")    
        if(pointerTwo >= len(t)):
            # We have hit the end of string t without finding a match 
            return False
        
#print(f"Test 1: {isSubsequence("abc", "ahbgdc") == True}")
#print(f"Test 2: {isSubsequence("axc", "ahbgdc") == False}")
#print(f"Test 1: {isSubsequence("acb", "ahbgdc") == False}")
print(f"Test 1: {isSubsequence("bcd", "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuubcd") == True}")