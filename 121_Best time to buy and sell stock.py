
def maxProfit(self, prices) -> int:
    if len(prices) <= 1:
        return 0
    left = prices[0]
    right = prices[1]
    max_profit = right - left
    for i in range(1, len(prices)-1):
        if prices[i] < left:
            left = prices[i]
            right = prices[i+1]
        else:
            right = prices[i+1]
        diff = right - left
        if max_profit < diff:
            max_profit = diff
    return max(max_profit,0)



