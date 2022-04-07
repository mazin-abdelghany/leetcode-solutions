###############
# MY SOLUTION #
###############
def twoSum(nums, target):
    counter = 0

    while len(nums) > 0:
        num = nums.pop(0)
        
        for i in range(len(nums)):
            if num + nums[i] == target:
                return [counter, (counter+i+1)]

        counter += 1


#######################
# Two-pass Hash Table #
#######################
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


#######################
# One-pass Hash Table #
#######################
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i