
def maximum_product(nums):
    max_prod = max(nums)
    curr_min, curr_max = 1, 1
    for i in nums:
        if i == 0:
            curr_min, curr_max = 1, 1
            continue
        tmp = curr_max
        curr_max = max(i * curr_max, i * curr_min, i)
        curr_min = min(i * tmp, i * curr_min, i)
        max_prod = max(curr_max, max_prod)
    return max_prod


