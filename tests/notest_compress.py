"""
Test the compression and decompression of a sequence
"""

from ..compress import compress_algorithmic, decompress_algorithmic

cases = (
    ("aaaaaaaaaa", "(10,a)"),
    ("aaaaabcdef", "(5,a),(1,b),(1,c),(1,d),(1,e),(1,f)"),
    ("abcdefghij", "(1,a),(1,b),(1,c),(1,d),(1,e),(1,f),(1,g),(1,h),(1,i),(1,j)"),
    ("aacdefghij", "(2,a),(1,c),(1,d),(1,e),(1,f),(1,g),(1,h),(1,i),(1,j)"),
    ("abcdefghaa", "(1,a),(1,b),(1,c),(1,d),(1,e),(1,f),(1,g),(1,h),(2,a)"),
)

def test_compress_algorithmic():
    # Compressing the test cases
    for case in cases:
        assert compress_algorithmic(case[0]) == case[1]

def test_decompress_algorithmic():
    # decompressing the test cases
    for case in cases:
        assert decompress_algorithmic(case[1]) == case[0]