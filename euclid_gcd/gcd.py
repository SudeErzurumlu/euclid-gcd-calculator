def euclid_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.
    
    Parameters:
    -----------
    a : int
        First non-negative integer.
    b : int
        Second non-negative integer.
    
    Returns:
    --------
    int
        The greatest common divisor (GCD) of a and b.
    
    Raises:
    -------
    ValueError:
        If the provided numbers are not non-negative integers.
    """
    if a < 0 or b < 0:
        raise ValueError("Both numbers must be non-negative integers.")
        
    while b != 0:
        a, b = b, a % b
    return a
