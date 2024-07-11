#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M;
    cin >> N >> M;
    vector<int> lectures(N);
    
    int st = 0, en = 0;
    for(int i = 0; i < N; i++) {
        cin >> lectures[i]; 
        st = max(st, lectures[i]);
        en += lectures[i];
    }

    int res = en;

    while (st <= en) {
        int mid = (st + en) / 2;

        int part_sum = 0, part_cnt = 0;
        for (int i = 0; i < N; i++) {
            if (part_sum + lectures[i] > mid) {
                part_sum = 0;
                part_cnt += 1;
            }
            part_sum += lectures[i];
        }
        if (part_sum) part_cnt += 1;

        if (part_cnt <= M) {
            en = mid - 1;
            res = min(res, mid);
        }

        else {
            st = mid + 1;
        }
    }

    cout << res;
}