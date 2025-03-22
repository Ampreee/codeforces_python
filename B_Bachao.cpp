#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
int dfs(int n,vector<vector<int>> &a,vector<bool> &v) {
    v[n] = true;
    int s = 1;
    for(auto i : a[n]) {
        if(!v[i]){
            s+=dfs(i,a,v);
        }
    }
    return s;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while(t--){
        int n, m;
        cin>>n>>m;
        vector<vector<int>> l1(n+1);
        for (int i = 0; i < m; ++i) {
            int a,b;
            cin>>a>>b;
            l1[a].push_back(b);
            l1[b].push_back(a);
        }
        int s=0;
        long long c=1;
        vector<bool> v(n+1,false);
        for (int i=1;i<=n;++i) {
            if (!v[i]) {
                s++;
                c=(c*dfs(i,l1,v))%MOD;
            }
        }
        cout<<s<<" "<<c<<"\n";
    }
    return 0;
}
