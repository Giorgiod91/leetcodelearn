def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:  # Check if the number is already in the result list
            unique_nums.append(num)
    return unique_nums

# Example usage:
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  
