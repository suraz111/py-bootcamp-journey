class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Outer loop: picks the first number
        for i in range(len(nums)):
            # Inner loop: picks the second number (starts after the first one)
            for j in range(i + 1, len(nums)):
                # If they add up to the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]



