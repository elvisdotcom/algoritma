import math

def confidence_wilson_interval(pos, neg):
    """\
    Confidence sort algoritm using Wilson score interval
    """
    pos, neg = float(pos), float(neg)
    if pos + neg == 0.0:
        return 0
    n = pos + neg
    z = 1.0
    hat_p = pos / n
    return math.sqrt(
                     hat_p + z * z / (2 * n) - \
                     z * ((hat_p * (1 - hat_p) + z * z / (4 * n)) / n)
                     ) / \
           (1 + z * z/n)

confidence = confidence_wilson_interval
