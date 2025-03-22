def compare(region):
    return (region[0], -region[1])
 
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
 
regions = [(x[i], y[i], i) for i in range(n)]
 
regions.sort(key=compare)
 
c_any = [0] * n
c_by_any = [0] * n
 
max_end = -1
for region in regions:
    if region[1] <= max_end:
        c_by_any[region[2]] = 1
    max_end = max(max_end, region[1])
 
min_end = None
for i in range(n-1, -1, -1):
    region = regions[i]
    if min_end is not None and region[1] >= min_end:
        c_any[region[2]] = 1
    if min_end is None or region[1] < min_end:
        min_end = region[1]
 
 
for value in c_any:
    print(value, end=' ')
print()
 
for value in c_by_any:
    print(value, end=' ')
print()
    