class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        start, end = 0, 0
        max_h, max_w = 0, 0
        
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        for i in range(len(horizontalCuts)):
            end = horizontalCuts[i]
            curr = end - start
            if curr > max_h:
                max_h = curr 
            start = end
        curr = h - end
        if curr > max_h:
            max_h = curr
        
        start, end = 0, 0
        for j in range(len(verticalCuts)):
            end = verticalCuts[j]
            curr = end - start
            if curr > max_w:
                max_w = curr
            start = end
        curr = w - end
        if curr > max_w:
            max_w = curr
        
        max_area = (max_h * max_w) 
        if max_area > (10 ** 9):
            max_area = max_area % ((10 ** 9) + 7)
        return max_area
