


from typing import List


def missingNumber(nums: List[int]):
        # Step 1: Calculate the expected sum
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2  # Sum of numbers from 0 to n
        
        # Step 2: Calculate the actual sum of elements in the array
        actual_sum = sum(nums)
        
        # Step 3: Return the missing number
        return expected_sum - actual_sum
    

print(missingNumber([3,0,1]))

# add numbers together
def sum_up(nums: List[int]):
        n = len(nums)
        added_sum = (n* ( n+1)) //2

        
        return added_sum


print(sum_up([1,2,3]))
