class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        newList = {i: abs(costs[i][0] - costs[i][1]) for i in range(len(costs))}
        newList = sorted(newList.items(), key=lambda x: x[1], reverse=True)
        newList = [costs[i] for i, j in newList]
        countA = countB = len(costs)/2
        sumT = 0
        for i in newList:
            if i[0] <= i[1] and countA > 0:
                sumT += i[0]
                countA -= 1
            elif i[1] <= i[0] and countB > 0:
                sumT += i[1]
                countB -= 1
            elif countA > 0:
                sumT += i[0]
                countA -= 1
            else:
                sumT += i[1]
                countB -= 1
        return (sumT)
                
                
            
        
