def factorial_recursive(n):
    """DOC STRING"""
    if n <= 1:
        return 1
    else:
        return (n * (factorial_recursive(n - 1)))

def factorial_loop(n):
    """DOC STRING"""
    if n <= 1:
        return 1
    for num in range(1, n):
        b = n * num
        n = b
    return b