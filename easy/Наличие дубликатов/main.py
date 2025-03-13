def containsDuplicate(nums):
    set_nums = set(nums)
    if len(set_nums) == len(nums):
        return True
    return False


print(containsDuplicate([1, 2, 2, 3]))
