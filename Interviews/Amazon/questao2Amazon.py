def stockSpike(prices, k):
    nKSpikes = 0
    for i in range(k, len(prices) - k):
        nLeftElementsLesser = 0
        nRightElementsLesser = 0
        for j in range(0, len(prices)):
            if j < i:
                if prices[j] < prices[i]:
                    nLeftElementsLesser += 1
            elif j > i:
                if prices[j] < prices[i]:
                    nRightElementsLesser += 1
        if nLeftElementsLesser >= k and nRightElementsLesser >= k:
            nKSpikes += 1
    return nKSpikes

if __name__ == '__main__':
    print(stockSpike([1,2,8,3,7,4,6,5], 3))