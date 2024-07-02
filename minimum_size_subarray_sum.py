def minSubArrayLen(target: int, nums: list[int]) -> int:
    start = 0
    finish = 0
    lenght = float('inf')
    arr_sum = 0
    while (finish <= (len(nums) - 1)) and start <= (len(nums) - 1):
            finish += 1
            arr_sum += nums[finish-1]
            while arr_sum >= target:
                lenght = min(lenght, finish - start)
                arr_sum -= nums[start]
                start+=1

    if lenght != float('inf'):
        return lenght
    else:
        return 0
