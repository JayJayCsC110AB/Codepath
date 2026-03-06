def goldilocks_approved(nums):
 min_val = min(nums)
 max_val = max(nums)

    # loop through numbers to find first that is strictly between min and max
 for num in nums:
    if num != min_val and num != max_val:
        return num
 return -1
nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))


nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))