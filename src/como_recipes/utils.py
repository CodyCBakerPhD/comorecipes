"""Collection of minor help functions."""

import ctypes
import struct


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
    return 80, 25  # default value
