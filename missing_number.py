''' Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
Example 1:
Input: [3,0,1]  Output: 2
Example 2:
Input: [9,6,4,2,3,5,7,0,1]  Output: 8'''


# Solution1: Check for 1 missing number

class Find:
    def noMiss(self, no):
        for x in range(-1,len(no)):
            if(x+1) not in no:
                return (x+1)
obj = Find()
obj.noMiss([3,0,1])
