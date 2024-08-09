import math

def Theatre(n, m, a):
    tiles_required = math.ceil(n / a) * math.ceil(m / a)
    return tiles_required


n, m, a = map(int, input().split())
print(Theatre(n, m, a))