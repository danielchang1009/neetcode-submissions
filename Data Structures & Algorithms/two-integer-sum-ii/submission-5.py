class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ptr1 in range(len(numbers)):
          for ptr2 in range(ptr1+1,len(numbers)):
             if  numbers[ptr1]+numbers[ptr2]==target:
                 return [ptr1+ 1, ptr2 + 1]
        return[]
            