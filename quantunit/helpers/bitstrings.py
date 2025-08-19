def int_to_bitstring(n, width, endian='little'):
    """Convert int to zero-padded bitstring of length width (default little-endian)."""
    s = format(n, f'0{width}b')
    return s[::-1] if endian == 'little' else s

def bitstring_to_int(bits, endian='little'):
    """Convert a string/list of bits to int."""
    if endian == 'little':
        bits = bits[::-1]
    return int(''.join(bits), 2)