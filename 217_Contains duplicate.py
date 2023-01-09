
def check_duplicate(nums):
    dict_out = {}
    for i in nums:
        if i in dict_out:
            return True
        else:
            dict_out[i] = 1
    return False


