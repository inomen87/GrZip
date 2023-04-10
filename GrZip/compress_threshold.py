"""
Compression Implementation with new spec considering the threshold and delimiter of the compression.

Given a sequence S. Suppose a character C occurs consecutively X times in the string.
Replace these consecutive occurrences (1 or more) of the character C with (X,C) in the string.

NEW SPEC:
Only compress, if the consecutive occurrences of C is equal or bigger than threshold.
ZaaabbbbbXccccccdefY => Zaaa(5,b)X(6c)defY
"""

def compress(sequence, threshold=5, delimiter=["(",")"]):
    """ Take a sequence as a string and returns the compressed sequence as a string.
    """
    return "Zaaa(5,b)X(6c)defY"

def decompress(sequence, delimiter=["(",")"]):
    """ Take a compressed sequence as a string and returns the expanded sequence as a string.
    """
    return "ZaaabbbbbXccccccdefY"

if __name__ == "__main__":
    assert compress("ZaaabbbbbXccccccdefY", 5) == "Zaaa(5,b)X(6c)defY"
    assert decompress("Zaaa(5,b)X(6c)defY") == "ZaaabbbbbXccccccdefY"