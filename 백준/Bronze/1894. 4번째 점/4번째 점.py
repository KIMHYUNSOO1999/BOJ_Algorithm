import sys

def is_close(a, b, tol=1e-8):
    return abs(a - b) < tol

def point_equal(p1, p2, tol=1e-8):
    return is_close(p1[0], p2[0], tol) and is_close(p1[1], p2[1], tol)

for line in sys.stdin:
    if not line.strip():
        continue

    arr_tmp = list(map(float, line.strip().split()))
    arr = [(arr_tmp[i], arr_tmp[i+1]) for i in range(0, len(arr_tmp), 2)]

    shared = None
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if point_equal(arr[i], arr[j]):
                shared = arr[i]
                break
        if shared:
            break

    if shared is None:
        continue  

    others = [p for p in arr if not point_equal(p, shared)]

    Dx = others[0][0] + others[1][0] - shared[0]
    Dy = others[0][1] + others[1][1] - shared[1]

    print(f"{Dx:.3f} {Dy:.3f}")
