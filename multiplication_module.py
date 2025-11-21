def multiplication_table(n, limit):
    """
    Return a list of lines representing multiplication table of n up to limit.
    Example: multiplication_table(3,5) -> ["3 x 1 = 3", ..., "3 x 5 = 15"]
    """
    lines = []
    for i in range(1, limit + 1):
        lines.append(f"{n} x {i} = {n * i}")
    return lines
