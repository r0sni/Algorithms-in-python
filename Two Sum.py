def two_sum(num, t):
    z = {}
    for i, num in enumerate(num):
        diff = target - num
        if diff not in z:
            z[num] = i
        else:
            return [i, z[diff]]
