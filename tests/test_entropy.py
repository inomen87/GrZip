"""
Test the entropy and byte savings methods
"""

from ..compress import compress_algorithmic
from ..compress import byte_difference, sequence_consecutives, sequence_entropy

def test_sequence_consecutives():
    # Tests if consecutives are properly generated
    assert sequence_consecutives("abcdefghij") == []
    assert sequence_consecutives("aabcceffff") == [2,2,4]
    assert sequence_consecutives("aaaaaaaaaa") == [10]

def test_sequence_entropy():
    # Test if entropy is calculated properly
    assert sequence_entropy("aaaaaaaaaa") == 0.0, "Absolute order, no entropy"
    assert sequence_entropy("aaaaabcdef") == 0.5, "Starting consecutive is not recognized"
    assert sequence_entropy("abcdefghij") == 1.0, "Absolute entropy, no order"
    assert sequence_entropy("aacdefghij") == 0.8, "Starting consecutive is not recognized"
    assert sequence_entropy("abcdefghaa") == 0.8, "Ending consecutive is not recognized"

def test_byte_difference(original = ["aaaaaaaaaa", "aaaaabcdef"]):
    original = "aaaaaaaaaa"
    compressed = compress_algorithmic(original)
    assert byte_difference(original, compressed) == 4
    original = "aaaaabcdef"
    compressed = compress_algorithmic(original)
    assert byte_difference(original, compressed) == -25 # No savings