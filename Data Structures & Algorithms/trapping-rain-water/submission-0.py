class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        left, right = 0, n-1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:

            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])

                potential_water = max_left - height[left]

                if potential_water > 0:
                    water += potential_water

            else:
                right -= 1
                max_right = max(max_right, height[right])

                potential_water = max_right - height[right]

                if potential_water > 0:
                    water += potential_water

        return water
        