def removeDuplicates(nums: list[int]):
    s = set(nums)
    for i in s:
        while nums.count(i) > 2:
            nums.pop(nums.index(i))
    return nums