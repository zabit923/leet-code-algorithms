nums = [3, 9, 5, 4, 6, 1, 7, 2, 8]
lenght = len(nums)


for i in range(0, lenght-1):
    for j in range(0, lenght-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]


print(nums)
