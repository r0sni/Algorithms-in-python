def productofarray(nums):
    left, right, output = [], [], []
    left.append(nums[0])
    right.append(nums[-1])
    length = len(nums)
    for i in range(1, length):
        left.append(left[i-1]*nums[i])
    for i in range(length-1,0,-1):
        right.insert(0,nums[i-1]*right[0])
    print(left)
    print(right)
    output = []
    for i in range(length):
        if i == 0:
            output.insert(i, right[i+1])
        elif i == length-1:
            output.insert(i, left[i-1])
        else:
            output.append(left[i-1]*right[i+1])
    return output