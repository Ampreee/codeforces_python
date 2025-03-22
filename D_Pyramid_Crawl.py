MOD = 100000007
N = 4
 
t = int(input())
for _ in range(t):
    k = int(input())
    M = []
    for i in range(4):
        row = []
        for j in range(4):
            if i != j:
                row.append(1)
            else:
                row.append(0)
        M.append(row)
    
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
 
    power = k
    while power:
        if power % 2 == 1:
            temp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    sum_val = 0
                    for l in range(N):
                        sum_val = (result[i][l] * M[l][j]) % MOD
                        temp[i][j] = (temp[i][j] + sum_val) % MOD
            result = temp
 
        temp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                sum_val = 0
                for l in range(N):
                    sum_val = (M[i][l] * M[l][j]) % MOD
                    temp[i][j] = (temp[i][j] + sum_val) % MOD
        M = temp
 
        power //= 2
    
    print(result[0][0])