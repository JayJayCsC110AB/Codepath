def moveZeroes(nums):
        i = 0
        j = len(nums) - 1
        

        while i < j:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i += 1


nums = [0, 1, 0, 3, 12] # call the function to modify nums in-place
moveZeroes(nums)
print(nums)