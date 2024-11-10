def twoSum(nums, target):
    """
    Find indices of two numbers in the list `nums` that add up to the `target`.

    Args:
        nums (list of int): List of integers to search through.
        target (int): The target sum to find.

    Returns:
        tuple of (int, int) or (None, None):
        A tuple with the indices of the two numbers that add up to the target,
        or (None, None) if no such pair exists.
    """
    for i, numOne in enumerate(nums):
        if numOne > target:
            continue
        for j, numTwo in enumerate(nums[i + 1 :]):
            numSum = numOne + numTwo
            if numSum == target:
                return i, j

    return None, None
