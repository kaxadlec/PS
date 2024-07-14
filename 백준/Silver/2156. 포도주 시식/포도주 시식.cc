#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> arr(N);
    vector<vector<int>> dp(N, vector<int>(2));

    for(int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    dp[0][0] = arr[0];
    dp[0][1] = arr[0];
    if (N > 1) {
        dp[1][0] = arr[1];
        dp[1][1] = arr[0] + arr[1];
    }
    
    if (N > 2) {
        for(int i = 2; i < N; i++) {
            dp[i][0] = max(dp[i-2][0] + arr[i], dp[i-2][1] + arr[i]);
            dp[i][1] = max(dp[i-1][0] + arr[i], dp[i-1][1]);
        }
    }

    int res = max(dp[N-1][0], dp[N-1][1]);

    cout << res;
}