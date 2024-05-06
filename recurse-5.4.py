"""
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        
recurse(3, 0)


|  recurse(3, 0)    |
|-------------------|
|    n = 3          |
|    s = 0          |
|-------------------|
|  recurse(2, 3)    |
|-------------------|
|    n = 2          |
|    s = 3          |
|-------------------|
|  recurse(1, 5)    |
|-------------------|
|    n = 1          |
|    s = 5          |
|-------------------|
|  recurse(0, 6)    |
|-------------------|
|    n = 0          |
|    s = 6          |
|-------------------|

"""

def recurse(n, s):
    """
    Recursively computes and prints the result of adding consecutive integers starting from s up to n.

    Parameters:
    n (int): The number of consecuive integers to add. It should be a non-negative integer.
    s (int): The starting value from which the consecutive integers will be added. IT can be any integer.


    Returns: 
    None

    Usage: 
    Call the recurse function with two arguments: n, the number of consecutive integers to add, and s, the starting value.
    Ensure that n is a non-negative integer, otherwise a ValueError will be raised.

    Example:
    >>> recurse(3, 0)
    6
    >>> recurse(-1, 0)
    Traceback (most recent call last):
        ...
    ValueError Parameter 'n' should be a non-negative integer. 
    """

    if n < 0:
        print("Error 'n' should be a non-negative integer.")
        return
    
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
        