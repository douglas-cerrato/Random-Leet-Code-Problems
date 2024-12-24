# URL
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    results = []
    biggestNum = candies[0]
    for x in candies:
        if(x > biggestNum):
            biggestNum = x
    for x in candies:
        if(x + extraCandies >= biggestNum):
            results.append(True)
        else:
            results.append(False)
            
    return results

print(f"Test 1: {kidsWithCandies([2,3,5,1,3], 3) == [True,True,True,False,True]}")
print(f"Test 2: {kidsWithCandies([4,2,1,1,2], 1) == [True,False,False,False,False]}")
print(f"Test 2: {kidsWithCandies([12,1,12], 10) == [True,False,True]}")


