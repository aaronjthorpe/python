def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    This function takes the length and width of a rectangle and returns
    the computed area. Both parameters must be non-negative numbers.

    Parameters
    ----------
    length : float
        The length of the rectangle (must be >= 0).
    width : float
        The width of the rectangle (must be >= 0).

    Returns
    -------
    float
        The area of the rectangle.

    Raises
    ------
    ValueError
        If either `length` or `width` is negative.

    Examples
    --------
    >>> calculate_area(5, 3)
    15.0
    >>> calculate_area(0, 10)
    0.0
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative.")
    return length * width


# Example usage
if __name__ == "__main__":
    try:
        print(calculate_area(5, 3))  # Expected output: 15.0
    except ValueError as e:
        print(f"Error: {e}")
