def max_subarray(nums):
    curr_sum = 0
    max_sum = nums[0]  # it prevents final sum from being 0 for e.g. in case nums = [-1]
    for i in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += i
        max_sum = max(max_sum, curr_sum)
    return curr_sum
