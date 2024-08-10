def Physicist():
    n = int(input())
    x = y = z = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        x += a
        y += b
        z += c

    if x == y == z == 0:
        return "YES"
    return "NO"


print(Physicist())