import math
def initialize(dim: int):
    global count
    count = 0
    global max_point
    # max point = 1/c * 4 ^ d
    # c is constant in ball volume
    c = (math.sqrt(math.pi**dim) / math.gamma(dim/2 + 1))
    max_point = math.ceil((1/c) * 4 ** dim)