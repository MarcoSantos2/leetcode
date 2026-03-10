"""You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        
        for i in range(len(temperatures)):
            j = i+1
            counter = 0
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    counter +=1
                    result.append(counter)
                    break
                elif temperatures[i] >= temperatures[j]:
                    counter += 1
                    j += 1
                    continue
            else:
                result.append(0)
                            
            print(result)
        return result
                
