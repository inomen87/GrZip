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
    # VARIABLES
    compressed_sequence = ""
    buffer = ""

    # TODO: Parameter Protection (s,t,d)

    def buffer_compress(last=False):
        # Helper: compress the buffer
        if len(buffer) >= threshold:
            # compressed copy return
            if last:
                return f"{delimiter[0]}{len(buffer)},{buffer[0]}{delimiter[1]}"
            else:
                return f"{delimiter[0]}{len(buffer) - 1},{buffer[0]}{delimiter[1]}"
        else:
            # uncompressed copy return
            if last:
                return buffer
            else:
                return buffer[0:-1]

    # ENGINE
    for c in sequence:
        buffer += c
        if len(buffer) <= 1:
            continue
        # Buffer has a character change
        if buffer[-2] != buffer[-1]:
            compressed_sequence += buffer_compress()
            buffer = buffer[-1]
    # Append remaining buffer
    compressed_sequence += buffer_compress(last=True)

    # RETURN the expanded sequence
    return compressed_sequence

def decompress(sequence, delimiter=["(",")"]):
    """ Take a compressed sequence as a string and returns the expanded sequence as a string.
    """
    expanded_sequence = ""
    buffer = ""

    def buffer_decompress():
        n = ""
        for b in buffer:
            if b.isdigit():
                n += b
            if b == ',':
                break
        return int(n) * buffer[-2]

    # TODO: Parameter Protection (s,d)

    # ENGINE
    for c in sequence:
        if buffer == "" and c != delimiter[0]:
            expanded_sequence += c
        else:
            # Buffer Operation
            buffer += c
            if buffer[0] == delimiter[0] and buffer[-1] == delimiter[1]:
                # Buffer write
                n = ""
                for b in buffer:
                    if b.isdigit():
                        n += b
                    if b == ',':
                        break
                # Write n times the character in the buffer
                expanded_sequence += buffer_decompress()
                buffer = ""

    # RETURN
    return expanded_sequence

if __name__ == "__main__":
    #assert compress("aaaaaaaaaa", 5) == "(10,a)"
    assert compress("ZaaabbbbbXccccccdefY", 5) == "Zaaa(5,b)X(6,c)defY"
    #assert decompress("Zaaa(5,b)X(6,c)defY") == "ZaaabbbbbXccccccdefY"