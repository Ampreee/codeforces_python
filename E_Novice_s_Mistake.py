t=int(input())
for _ in range(t):
    n=int(input())
    bad_tests = []
    for a in range(1, 10001):
        b = n * a - 1
        if b >= 1 and b <= min(10000, n * a):
            bad_tests.append((a, b))
    print(bad_tests[0])