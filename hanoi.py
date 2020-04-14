depth = -1
def hanoi(n, start, dest, assist):
    global depth
    depth += 1
    indent = '\t' * depth
    print(f'{indent}running hanoi({n}, {start}, {dest}, {assist})')
    if n == 1:
        print(f'{indent}move disc from {start} to {dest}')
    else:
        hanoi(n-1, start, assist, dest)
        print(f'{indent}*move disc from {start} to {dest}')
        hanoi(n-1, assist, dest, start)
    depth -= 1


hanoi(3, 'A', 'C', 'B')
