"""
Helper script for refreshing the ICO file from a full JPG image.

Must be run manually whenever we wish to update the ICO file.

Requires the `pillow` package (imported as `PIL`).
"""

import importlib.util
import pathlib

if __name__ == "__main__":
    if importlib.util.find_spec("PIL") is None:
        message = "Unable to find the PIL module. Please install it with `pip install pillow`."
        raise ModuleNotFoundError(message)

    import PIL.Image

    full_image_file_path = pathlib.Path(__file__).parent / "full_como_icon.jpg"
    ico_image_file_path = pathlib.Path(__file__).parent / "como_icon.ico"

    shape_in_pixels = (64, 64)

    image = PIL.Image.open(fp=full_image_file_path)
    image = image.resize(size=shape_in_pixels, resample=PIL.Image.Resampling.LANCZOS)
    image.save(fp=ico_image_file_path, format="ICO")
