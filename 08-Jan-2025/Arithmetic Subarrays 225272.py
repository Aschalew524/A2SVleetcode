# Problem: Arithmetic Subarrays - https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lis=[]
        for i in range(len(l)):
            k=nums[l[i]:r[i]+1]
            k.sort()
            l1=[k[i+1]-k[i] for i in range(len(k)-1)] 
            if len(set(l1))==1:
                lis.append(True)
            else:
                lis.append(False)
        return lis


        