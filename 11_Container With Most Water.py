
def find_max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    for i in range(len(height)):
        area = (min(height[left], height[right]) * (right - left))
        max_area = max(area, max_area)
        if height[right] < height[left]:
            right -= 1
        else:
            left += 1
        if left == right:
            break
    return max_area



