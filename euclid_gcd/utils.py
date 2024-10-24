def validate_input(a: int, b: int) -> bool:
    """
    Validates that both inputs are integers and non-negative.
    
    Parameters:
    -----------
    a : int
        First number.
    b : int
        Second number.
    
    Returns:
    --------
    bool
        True if both inputs are valid, False otherwise.
    
    Raises:
    -------
    TypeError:
        If any input is not an integer.
    ValueError:
        If any input is negative.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    if a < 0 or b < 0:
        raise ValueError("Both inputs must be non-negative.")
    
    return True
