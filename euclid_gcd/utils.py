def validate_input(value):
    """
    Validates if the input is a non-negative integer.
    
    Parameters:
    -----------
    value : str
        Input value to be validated.
    
    Returns:
    --------
    int
        Validated non-negative integer.
    
    Raises:
    -------
    ValueError:
        If the value is not a valid non-negative integer.
    """
    try:
        ivalue = int(value)
        if ivalue < 0:
            raise ValueError
        return ivalue
    except ValueError:
        raise ValueError(f"Invalid input: {value}. Please enter a non-negative integer.")
