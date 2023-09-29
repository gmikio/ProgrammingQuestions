def recentlyViewed(logs):
    # Firstly, we'll write a function to check if the new
    # item has already appeared, if yes, return its index
    def isPresent(listOfItems, item):
        for i in range(len(listOfItems)):
            if item == listOfItems[i]:
                return i        
        return -1
        
    recentlyViewedItems = []

    for log in logs:
        indexIfPresent = isPresent(recentlyViewedItems, log)
        if indexIfPresent != -1:
            recentlyViewedItems.pop(indexIfPresent)
        recentlyViewedItems.insert(0, log)
            
    
    return recentlyViewedItems

if __name__ == '__main__':
    print(recentlyViewed(["Ab3defgHi0", "Ab3defgHi0", "Ab3defgHi0", "Ab3defgHi0", "Ab3defgHi0",]))