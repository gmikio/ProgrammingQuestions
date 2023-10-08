def solution(bubbles, operations):
    print (bubbles)
    print (operations)
    
    def bubblePop(bubbles, i, j):
        lenY = len(bubbles)
        lenX = len(bubbles[0])
        
        if bubbles[i][j] != 0:
            middleColor = bubbles[i][j]
            
            bubbles[i][j] == 0
            if i > 0 and j > 1:
                if bubbles[i-1][j-1] == middleColor: 
                    bubbles[i-1][j-1] == 0
            if i < lenY and j < lenX:
                if bubbles[i+1][j+1] == middleColor:
                    bubbles[i+1][j+1] == 0
            if i < lenY and j > 0:
                if bubbles[i+1][j-1] == middleColor:
                    bubbles[i-1][j+1] == 0
            if i > 0 and j < lenX:
                if bubbles[i-1][j+1] == middleColor:
                    bubbles[i-1][j+1] == 0
                           
            
        return bubbles
        
    def rearrangeBubbles(bubles)
        lenY = len(bubbles)
        lenX = len(bubbles[0])
        
        for i in range(0, lenX):
            for j in range(0, lenY):
                if 
        
        return bubbles
    
    for operation in operations:
        i, j = operation[0], operation[1]
        bubbles = bubblePop(bubbles, i, j)
        # Function to make the bubbles go down
        # i ran out of time
        
        """bubbles:
[[1,1,1,4,3], 
 [4,1,2,3,3], 
 [1,5,1,1,2], 
 [4,3,2,2,4]]
operations:
[[1,1], 
 [3,3], 
 [2,2], 
 [3,0]]"""