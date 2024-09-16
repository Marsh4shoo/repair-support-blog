#!/usr/bin/python3

def validUTF8(data):
    """
    Validate if a given dataset represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes
    :return: True if data is a valid UTF-8 encoding, False otherwise
    """
    num_bytes = 0
    
    for byte in data:
        # Convert byte to binary and check its format
        byte_bin = format(byte, '08b')  # Convert to 8-bit binary string
        
        if num_bytes == 0:
            # Determine the number of bytes for this character
            if byte_bin.startswith('0'):
                num_bytes = 0
            elif byte_bin.startswith('110'):
                num_bytes = 1
            elif byte_bin.startswith('1110'):
                num_bytes = 2
            elif byte_bin.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            # Check if byte is a valid continuation byte
            if not byte_bin.startswith('10'):
                return False
            num_bytes -= 1
    
    return num_bytes == 0

