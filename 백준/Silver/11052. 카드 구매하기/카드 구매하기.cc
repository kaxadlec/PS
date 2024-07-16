#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> dp(n+1);

    for(int i = 1; i < n+1; i++) {
        int num;
        cin >> num;
        dp[i] = num;
    }


    int half;
    for(int i = 1; i < n+1; i++) {
        half = i / 2;
        for (int j = 0; j < half + 1; j++) {
            dp[i] = max(dp[i], dp[j] + dp[i-j]);
        }
    }
    
    cout << dp[n];
    
}