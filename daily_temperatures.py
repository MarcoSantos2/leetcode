"""You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
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
                            
        return result
                
        # Test cases for Solution().dailyTemperatures

if __name__ == "__main__":
    from typing import List

    def test_daily_temperatures():
        sol = Solution()
        # Example case
        assert sol.dailyTemperatures([30,38,30,36,35,40,28]) == [1,4,1,2,1,0,0]
        # All increasing
        assert sol.dailyTemperatures([30,31,32,33,34]) == [1,1,1,1,0]
        # All decreasing
        assert sol.dailyTemperatures([40,39,38,37,36]) == [0,0,0,0,0]
        # All same
        assert sol.dailyTemperatures([30,30,30,30]) == [0,0,0,0]
        # Mixed, mid increases
        assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
        # Single element
        assert sol.dailyTemperatures([33]) == [0]
        # Two elements, warmer ahead
        assert sol.dailyTemperatures([21,25]) == [1,0]
        # Two elements, no warming
        assert sol.dailyTemperatures([27,24]) == [0,0]
        # Large identical temperatures
        assert sol.dailyTemperatures([50] * 100) == [0]*100

        print("All test cases passed.")

    test_daily_temperatures()