#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin>>n;
    vector<pair<int, int>> sh;
    for (int i=0;i<n;++i) {
        int a, b;
        cin >>a>>b;
        sh.push_back({a,1});    
        sh.push_back({b+1,-1}); 
    }
    sort(sh.begin(), sh.end());
    int c=0;
    int s=0;
    for (const auto& i:sh) {
        c+=i.second;
        s=max(s,c);
    }
    cout <<s<< endl;
    return 0;
}
