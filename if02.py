def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mm = a
    if mm > b:
        mm = b
    if mm > c:
        mm = c
    return mm