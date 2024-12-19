# URL to Problem
# https://leetcode.com/problems/merge-strings-alternately

def mergeAlternately(word1: str, word2: str) -> str:
#     newString = ""
#     if(len(word1) > len(word2)): x = len(word1)
#     else: x = len(word2)
        
#     for y in range(x):
#         if(word1):
#             newString+=word1[0]
#             word1 = word1[1:]
#         if(word2):
#             newString+=word2[0]
#             word2 = word2[1:]

#     return newString
    newString = ""
    for x in range(len(word1)):
        newString+=word1[:1]
        if len(word1) > 1:
            word1=word1[1:]
        else:
            word1 = ""
        print(f"Word1 after slicing last first letter is {word1}")
        newString+=word2[:1]
        
        if len(word2) > 1:
            word2=word2[1:]
        else:
            word2 = ""
        print(f"Word2 after slicing last first letter is {word2}")
        print(newString)
    if(len(word1) > len(word2)):
        newString+=word1
    else:
        newString+=word2
    return newString

print(f"Test 1: {mergeAlternately("abc", "pqr")=="apbqcr"}")
print(f"Test 2: {mergeAlternately("ab", "pqrs")=="apbqrs"}")
print(f"Test 3: {mergeAlternately("abcd", "pq")=="apbqcd"}")

