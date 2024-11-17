"""Collection of minor help functions."""

import ctypes
import struct


# TODO: remove when grams are enforced
def rational_string_to_float(string: str) -> float:  # pragma: no cover
    """Small helper function to convert strings into floats ('1/4' becomes 0.25)."""
    if "/" in string:
        numerator, denominator = string.split("/")
        return int(numerator) / int(denominator)
    else:
        return float(string)


def get_terminal_size() -> tuple[int, int]:
    """Superior to the shutil.get_terminal_size() function for Windows; responds to dynamic window reshaping."""
    standard_handle = ctypes.windll.kernel32.GetStdHandle(-12)
    string_buffer = ctypes.create_string_buffer(22)
    info = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(standard_handle, string_buffer)
    if info:
        (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack(
            "hhhhHhhhhhh",
            string_buffer.raw,
        )
        sizex = right - left + 1
        sizey = bottom - top + 1

        return sizex, sizey
    else:
        return 80, 25  # default value
