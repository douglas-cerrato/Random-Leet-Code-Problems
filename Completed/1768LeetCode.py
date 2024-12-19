# URL to Problem
# https://leetcode.com/problems/merge-strings-alternately

def mergeAlternately(word1: str, word2: str) -> str:
    newString = ""
    if(len(word1) > len(word2)): x = len(word1)
    else: x = len(word2)
        
    for y in range(x):
        if(word1):
            newString+=word1[0]
            word1 = word1[1:]
        if(word2):
            newString+=word2[0]
            word2 = word2[1:]

    return newString

print(f"Test 1: {mergeAlternately("abc", "pqr")=="apbqcr"}")
print(f"Test 2: {mergeAlternately("ab", "pqrs")=="apbqrs"}")
print(f"Test 3: {mergeAlternately("abcd", "pq")=="apbqcd"}")

