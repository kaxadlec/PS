#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, H;
    cin >> N >> H;

    vector<long long> section(H);
    for (int i = 0; i < H; i++) {
        section[i] = i + 1;
    }

    vector<long long> usage(H + 2, 0);
    for (int i = 0; i < N; i++) {
        int high;
        cin >> high;

        if (i % 2 == 0) {
            usage[1]++;
            usage[high + 1]--;
        }
        else {
            usage[H- high + 1]++;
        }
    }

    for (int i = 1; i <= H; i++) {
        usage[i] += usage[i-1];
    }

    int min_obstacle = 200001;
    int min_section_cnt;

    for (int i = 1; i <= H; i++) {
        if (usage[i] < min_obstacle) {
            min_obstacle = usage[i];
            min_section_cnt = 1;
        }
        else if (usage[i] == min_obstacle) {
            min_section_cnt += 1;
        }
    }

    cout << min_obstacle << " " << min_section_cnt;

}