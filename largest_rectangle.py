"""You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotonic stack of indices; O(n) — each index pushed/popped once.
        extended = heights + [0]
        stack: List[int] = []
        max_area = 0
        for i in range(len(extended)):
            while stack and extended[stack[-1]] > extended[i]:
                h = extended[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        return max_area

print(Solution().largestRectangleArea([7,1,7,2,2,4]))