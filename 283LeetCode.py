# URL
# https://leetcode.com/problems/move-zeroes/description/
#TODO: I need to solve this problem using 
# two pointers, not by how I am doing it now

def moveZeroes(nums: list[int]) -> list:
    zeroCount = []
    x = 0
    while x != len(nums) - 1:
        if nums[x] == 0:
            zeroCount.append(0)
            nums.pop(x)
        else:
            x+=1
            
    nums = nums + zeroCount
    return nums

print(f"Test 1: {moveZeroes([0,1,0,3,12]) == [1,3,12,0,0]}")
print(f"Test 2: {moveZeroes([0]) == [0]}")