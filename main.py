import zlib
import struct

# PNG documentation: https://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html

# PNG file signature
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# IHDR chunk checklist:
# Width (4-bytes)
# Height (4-bytes)
# Bit depth (1-byte)
# Color type (1-byte)
# Compression method (1-byte)
# Filter method (1-byte)
# Interlace method (1-byte)

# IHDR chunk constants
WIDTH = 128  # Image width in pixels
HEIGHT = 128  # Image height in pixels
BIT_DEPTH = 8  # Bit depth (8 bits per channel)
COLOR_TYPE = 6  # Color type (2 for RGB, 6 for RGBA)
COMPRESSION_METHOD = 0  # Compression method
FILTER_METHOD = 0  # Filter method
INTERLACE_METHOD = 0  # Interlace method


def create_ihdr_chunk():
    ihdr_data = struct.pack(
        "!IIBBBBB",
        WIDTH,
        HEIGHT,
        BIT_DEPTH,
        COLOR_TYPE,
        COMPRESSION_METHOD,
        FILTER_METHOD,
        INTERLACE_METHOD,
    )
    return ihdr_data


# IDAT chunk checklist:
# Compressed image data (variable length)
# CRC (4-bytes)

# IEND chunk checklist:
# Empty chunk with type IEND (empty data)

if __name__ == "__main__":
    print(PNG_SIGNATURE + create_ihdr_chunk())
