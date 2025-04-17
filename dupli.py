 
from typing import List

def Contains_duplicate_true_or_false(nums: List[int]) -> bool:
    
    unique = []
    for i in nums:
            if i in unique:
                 return True
            unique.append(i)
                

           

    return False

Contains_duplicate_true_or_false([1,2,3,4])


