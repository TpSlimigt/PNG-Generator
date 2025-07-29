import zlib
import struct


# PNG file signature
PNG_SIGNATURE = b'\x89PNG\r\n\x1a\n'

# IHDR chunk checklist:
# Width (4-bytes)
# Height (4-bytes)
# Bit depth (1-byte)
# Color type (1-byte)
# Compression method (1-byte)
# Filter method (1-byte)
# Interlace method (1-byte)

# IDAT chunk checklist:
# Compressed image data (variable length)
# CRC (4-bytes)

# IEND chunk checklist:
# Empty chunk with type IEND (empty data)

if __name__ == "__main__":
    print(PNG_SIGNATURE)