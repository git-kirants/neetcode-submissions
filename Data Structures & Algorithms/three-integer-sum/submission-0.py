class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i , a in enumerate(nums):
            if a > 0:
                break # we have reached the end of -ve numbers, stop

            if i > 0 and a == nums[i-1]:
                continue  # skip duplicates at a

            l ,r = i + 1, len(nums) - 1 # init pointers to frist after a and last point 

            while l < r:
                threeSum = a + nums[l] + nums[r] # calc
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l], nums[r]]) # if 0 add to ans
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 # if duplicate i.e same as last, increment
                
        return res