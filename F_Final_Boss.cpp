#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <iomanip>
 
using namespace std;
 
#define ENDL '\n'
#define INFINITY 1000000000
#define MODULUS 1000000007
#define PUSH_BACK push_back
#define MAKE_PAIR make_pair
#define ALL(x) (x).begin(), (x).end()
 
typedef long long int64;
typedef vector<int> vec_int;
typedef vector<vec_int> vec_vec_int;
typedef pair<int, int> pair_int;
 
int64 maximum(int64 a, int64 b){
    return (a > b) ? a : b;
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int test_cases;
    cin >> test_cases;
    while (test_cases--) {
        int64 height, num_elements;
        cin >> height >> num_elements;
        vector<int64> heights(num_elements);
        vector<int64> costs(num_elements);
        int i = 0;
        while (i < num_elements) {
            cin >> heights[i];
            i++;
        }
        i = 0;
        while (i < num_elements) {
            cin >> costs[i];
            i++;
        }
        int64 start_index = 0;
        int64 end_index = 8e10;
        int64 result = -1;
        while (start_index <= end_index) {
            int64 mid_index = (start_index + end_index) / 2;
            int64 total_cost = 0;
            i = 0;
            while (i < num_elements) {
                total_cost += ((mid_index / costs[i]) + 1) * heights[i];
                i++;
            }
            if (total_cost >= height) {
                result = mid_index;
                end_index = mid_index - 1;
            } else {
                start_index = mid_index + 1;
            }
        }
        cout << (result + 1) << ENDL;
    }
 
    return 0;
}