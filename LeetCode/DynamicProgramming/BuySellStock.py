from typing import List

def maxProfit(prices: List[int]) -> int:
    
    profit = int(0)
    individualProfit = int(0)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j] and prices[j] - prices[i] > individualProfit:
                individualProfit = prices[j] - prices[i]
        if individualProfit > profit:
            profit = individualProfit
    
    # min_price = prices[0]
    # max_profit = 0

    # for price in prices:
    #     min_price = min(min_price, price)
    #     max_profit = max(max_profit, price - min_price)

    # return max_profit
            
    return profit
                
def main():
    result = maxProfit(prices = [7,1,5,3,6,4]) # expected profit = 5 ([buy = 1; sell = 6])
    print (result)
    
if __name__ == "__main__":
    main()