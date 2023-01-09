
def three_sum(nums):
    nums = sorted(nums)
    output = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            total_sum = nums[i] + nums[l] + nums[r]
            if total_sum > 0:
                r -= 1
            elif total_sum < 0:
                l += 1
            else:
                output.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return output


