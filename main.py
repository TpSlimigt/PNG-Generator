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


def create_ihdr_data():
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


def create_image_data(width, height):
    solid_red_color = struct.pack("!BBBB", 255, 0, 0, 255)  # Solid red color (RGBA)
    image_data = solid_red_color * (width * height)
    return image_data


def apply_filter(image_data, width):
    filtered_data = bytearray()
    for row_start in range(0, len(image_data), width * 4):
        row_data = image_data[row_start : row_start + width * 4]
        filtered_data.append(0)
        filtered_data.extend(row_data)
    return bytes(filtered_data)


def compress_data(data):
    return zlib.compress(data)


# IEND chunk checklist:
# Empty chunk with type IEND (empty data)


def create_iend_data():
    return b""


# Chunk checklist:
# Length of bytes in data (4-bytes)
# Type (IHDR,IDAT,IEND 4-bytes)
# Data (variable length)
# CRC (4-bytes)


def create_data_chunk(data_type, data):
    data_length = len(data)
    crc = zlib.crc32(data_type + data)
    return struct.pack("!I", data_length) + data_type + data + struct.pack("!I", crc)


def create_png_file():
    ihdr_chunk = create_data_chunk(b"IHDR", create_ihdr_data())

    image_data = create_image_data(WIDTH, HEIGHT)
    filtered_data = apply_filter(image_data, WIDTH)
    compressed_data = compress_data(filtered_data)
    idat_chunk = create_data_chunk(b"IDAT", compressed_data)

    iend_chunk = create_data_chunk(b"IEND", create_iend_data())

    with open("output.png", "wb") as png_file:
        png_file.write(PNG_SIGNATURE)
        png_file.write(ihdr_chunk)
        png_file.write(idat_chunk)
        png_file.write(iend_chunk)


if __name__ == "__main__":
    create_png_file()
