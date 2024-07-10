#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int M, N;
    cin >> M >> N;
    vector<int> arr(N, 0);

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    sort(arr.begin(), arr.end());

    int st = 1;
    int en = arr[N-1];
    int mid, cnt;
    int res = 0;
    while (st <= en) {
        mid = (st + en + 1) / 2;
        cnt = 0;

        for (int i = 0; i < N; i++) {
            if (mid <= arr[i]) {
                cnt += arr[i] / mid;
            }
        }

        if (cnt < M) {
            en = mid - 1;
        }
        
        else {
            st = mid + 1;
            res = max(mid, res);
        }
    }

    cout << res;
}