MOD = 10**9 + 7
ma = 505
def count_ways(l, r, s, dp, choose):
    if (r - l) % 2 == 1:
        return 0
    if l > r:
        return 1

    if dp[l][r] != -1:
        return dp[l][r]

    if (r - l) == 1:
        dp[l][r] = 1 if s[l] == s[r] else 0
        return dp[l][r]
    result = 0
    for k in range(l + 1, r + 1, 2):
        if s[l] == s[k]:
            temp = (count_ways(l + 1, k - 1, s, dp, choose) 
                    * count_ways(k + 1, r, s, dp, choose) 
                    * choose[(r - l + 1) // 2][(k - l) // 2]) % MOD
            result = (result + temp) % MOD
    dp[l][r] = result
    return result

def compute_combinations(max_n):
    choose = [[0] * (max_n // 2 + 1) for _ in range(max_n // 2 + 1)]
    for i in range(max_n // 2 + 1):
        choose[i][0] = 1
        for j in range(1, i + 1):
            choose[i][j] = (choose[i - 1][j] + choose[i - 1][j - 1]) % MOD
    return choose

# Input reading
n = int(input())
s = input()
dp = [[-1] * ma for _ in range(ma)]
choose = compute_combinations(ma)
result = count_ways(0, n - 1, s, dp, choose)
print(result)

