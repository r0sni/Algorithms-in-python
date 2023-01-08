def search(nums, target):
    l = 0
    r = len(nums) - 1
    while r >= l:
        mid = l + (r - l) // 2
        if nums[mid] > target > nums[0]:
            r = mid - 1
            continue
        elif nums[mid] < target < nums[-1]:
            l = mid + 1
            continue
        elif nums[mid] == target:
            return mid
        elif nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        l = l + 1
        r = r - 1
    return -1
