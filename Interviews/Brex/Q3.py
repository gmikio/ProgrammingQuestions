def solution(operations):
    finalString = ""
    finalStringHistoric = [""]
    canUndo = False
    
    for operation in operations:
        wordsSplitted = operation.split()
        
        match wordsSplitted[0]:
            case "INSERT":
                finalString = finalString + wordsSplitted[1]
                finalStringHistoric.append(finalString)
                canUndo = True
            case "DELETE":
                if len(finalString) != 0:
                    finalString = finalString[:-1]
                    finalStringHistoric.append(finalString)
            case "UNDO":
                if finalStringHistoric[-1] == finalString: finalStringHistoric.pop()
                finalString = finalStringHistoric.pop()
        print("finalString for", operation, " operation is: ", finalString)
            
    
    return finalString
    
if __name__ == "__main__":
    print (solution(["UNDO", 
 "DELETE", 
 "UNDO", 
 "INSERT QD", 
 "DELETE", 
 "DELETE", 
 "UNDO", 
 "INSERT d", 
 "INSERT BE", 
 "INSERT pWiE", 
 "DELETE", 
 "INSERT zk", 
 "UNDO", 
 "DELETE", 
 "DELETE", 
 "UNDO", 
 "INSERT ojH", 
 "UNDO", 
 "DELETE", 
 "DELETE", 
 "INSERT TQg", 
 "INSERT Ps", 
 "DELETE", 
 "INSERT a", 
 "UNDO", 
 "UNDO", 
 "DELETE", 
 "INSERT ep", 
 "DELETE", 
 "UNDO"]))

"""
operations:
["INSERT Code", 
 "INSERT Signal", 
 "DELETE", 
 "UNDO"]
"""

# Expected Output: "CodeSignal"