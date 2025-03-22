#include <bits/stdc++.h>
using namespace std;
#define int long long
 
const int max_num_digits = 20;
int dp[max_num_digits][max_num_digits][2][2];
int n, m, k, d;
 
void reset() {
  for (int i = 0; i < max_num_digits; i++) {
    for (int j = 0; j < max_num_digits; j++) {
        for(int k = 0; k < 2; ++k){
              dp[i][j][k][0] = -1;
              dp[i][j][k][1] = -1;
        }
    }
  }
}
 
int dfs(int c, int x = 0, int y = 11, int lead = 1, bool z = 0) { 

  if (dp[x][y][lead][z] != -1) { // memoization
    return dp[x][y][lead][z];
  }
  if (x == to_string(c).length()) {
    // succesfully placed everything
    return dp[x][y][lead][z] = 1;
  }
  int limit = 9;
  int dig = to_string(c)[x] - '0';
  if (!z) { // if the number being formed CAN exceed c
    limit = dig; // the xth digit of c
  }
  cout<<c;
  // now setting the xth digit of the number we're building
  dp[x][y][lead][z] = 0; // going to permanently set dp[x][y][lead][z] now
  for (int xth_digit = 0; xth_digit <= limit; xth_digit++) {
    if(!lead && xth_digit == y) continue;
    if (z) {
      dp[x][y][lead][z] += dfs(c, x + 1, xth_digit, xth_digit == 0 && lead, 1);
    } else {
      dp[x][y][lead][z] += dfs(c, x + 1, xth_digit, xth_digit == 0 && lead, xth_digit < limit);
    }
  }
  return dp[x][y][lead][z];
}

signed main() {
    reset();
    cin >> n >> m;
    int total = dfs(m);
    reset();
    int torem = dfs(n-1);
    total -= torem;
    cout << total;
}