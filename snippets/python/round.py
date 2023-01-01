# https://twitter.com/raymondh/status/1608356566255955969
def round(x: float) -> int:
    "Round randomly based on proportional distance."
    p = ceil(x) - x
    return floor(x) if random() < p else ceil(x)
