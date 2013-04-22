import math

# Algoritma penghitung nilai keyakinan berdasarkan penilaian positif dan
# negatif.
def confidence(pos, neg):
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
