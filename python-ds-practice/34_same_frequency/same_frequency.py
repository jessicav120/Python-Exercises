def count_frequency(nums):
    counts = {}

    for num in nums:
        counts[num] = nums.count(num)
    
    return counts

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return count_frequency(str(num1)) == count_frequency(str(num2))