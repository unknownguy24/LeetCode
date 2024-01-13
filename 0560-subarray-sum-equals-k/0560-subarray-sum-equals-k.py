class Solution(object):
    def subarraySum(self, nums, k):
        sumdict = {0:1} #initializing our dict with 0 as 1 at begining
        n = len(nums) 
        counter = 0
        s = 0  #initial cumulative sum as 0 which we put in dictionary

        for num in nums:
            s+= num #cumulative sum
            if s-k in sumdict:
                counter += sumdict[s-k] #adding the value from dict to counter 
            if s in sumdict:
                sumdict[s] += 1 #increasing the value in dict if s is already there
            else:
                sumdict[s] = 1

        return counter
        