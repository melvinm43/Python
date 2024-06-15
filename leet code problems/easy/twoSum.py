"""
Algorithm:
1. create an empty hashMap
2. loop using the enumerate function
3. find the complement by subtracting the current number from the target value.
4. if the compliment is available in the hashmap then return the index of both the compliment and current number.
5. update the hashMap with the current number and the index
"""
def twoSum(nums, target):
    hashMap = {}
    for index,number in enumerate(nums):
        compliment = target - number
        if(compliment in hashMap):
            return [hashMap[compliment],index]
        hashMap[number] =index


numArray = [9,8,6,3,2]
print(twoSum(numArray,8) )