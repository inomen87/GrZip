"""
Test the compression and decompression of a sequence with the New Spec:

Only compress, if the consecutive occurrences of C is equal or bigger than threshold.
ZaaabbbbbXccccccdefY => Zaaa(5,b)X(6c)defY
"""

from ..GrZip.compress_threshold import compress, decompress
from ..GrZip.decompression_2 import decompress


cases_t5 = (
    ("aaaaaaaaaa", "(10,a)"),
    ("aaaaabcdef", "(5,a)bcdef"),
    ("abcdefghij", "abcdefghij"),
    ("aacdefghij", "aacdefghij"),
    ("abcdefghaa", "abcdefghaa"),
    ("abbbbbbbbc", "a(8,b)c"),
    ("aaaaabccccc", "(5,a)b(5,c)"),
)

def notest_compress_threshold(t=5):
    # Compressing the test cases NEW SPEC
    for case in cases_t5:
        assert compress(case[0],t) == case[1]

def test_decompress_threshold():
    # decompressing the test cases
    for case in cases_t5:
        assert decompress(case[1]) == case[0]