"""Collection of minor help functions."""


# TODO: remove when grams are enforced
def rational_string_to_float(string: str) -> float:  # pragma: no cover
    """Small helper function to convert strings into floats ('1/4' becomes 0.25)."""
    if "/" in string:
        numerator, denominator = string.split("/")
        return int(numerator) / int(denominator)
    else:
        return float(string)
