class Solution:
    def maxArea(self, height: list[int]) -> int:
        p=0
        q=len(height)-1
        maximum = 0

        while(p != q):
            current = (q-p) * min( height[p],height[q])
            if (current >= maximum):
                maximum = current
            if (height[p] <= height[q]):
                p+=1
            else : 
             q-=1

        return maximum