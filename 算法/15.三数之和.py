class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        s = []
        n = len(nums)
        right = n - 1
        left = 0
        for i in range(n-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    s.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return s



if __name__ == '__main__':
    nums = [1,-1,3,-2,4,-5,-2,3]
    print(Solution().threeSum(nums))