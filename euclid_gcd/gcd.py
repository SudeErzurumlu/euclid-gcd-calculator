def euclid_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.
    Handles both positive and negative integers by taking the absolute values.
    
    Parameters:
    -----------
    a : int
        First integer (can be positive or negative).
    b : int
        Second integer (can be positive or negative).
    
    Returns:
    --------
    int
        The greatest common divisor (GCD) of |a| and |b|.
    
    Raises:
    -------
    ValueError:
        If either number is not an integer.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
        
    a, b = abs(a), abs(b)  # Ensure inputs are positive
    
    while b != 0:
        a, b = b, a % b
    return a
