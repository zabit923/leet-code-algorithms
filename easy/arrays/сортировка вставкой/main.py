nums = [3, 9, 5, 4, 6, 1, 7, 2, 8]
lenght = len(nums)


for i in range(1, lenght):
    for j in range(i, 0, -1):
        if nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
        else:
            break


print(nums)
