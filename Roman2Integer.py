class Solution:
   def romanToInt(self, s: str) -> int:
        s = "MCMXCIV"
        symbolsArr = ["I","V","X","L","C","D","M"]
        valuesArr = [1,5,10,50,100,500,1000]
        numsArr = []
        numOfIterations = 0


        while numOfIterations <= len(s) - 1:
            i = len(symbolsArr) - 1
            while i >= 0:
                if symbolsArr[i] == s[numOfIterations]:
                    numsArr.append(valuesArr[i])
                    break
                i -= 1
            numOfIterations += 1

        lastIndex = len(numsArr) - 1
        sum = 0
        while lastIndex >= 0:
            if numsArr[lastIndex] > numsArr[lastIndex - 1]:
                sum += abs(numsArr[lastIndex] - numsArr[lastIndex - 1])
                lastIndex -= 1
            else:
                sum += numsArr[lastIndex]
            lastIndex -= 1
            print(lastIndex,sum,numsArr)
            if lastIndex == 0:
                sum += numsArr[lastIndex]
                break
        return(sum)









