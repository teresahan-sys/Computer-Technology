def climbing_stairs(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return climbing_stairs(n-1) + climbing_stairs(n-2)

print(climbing_stairs(5))