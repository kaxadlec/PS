#include <bits/stdc++.h>

using namespace std;

int board[501][501];
bool visited[501][501];
int n, m;
int di[4] = {1, 0, -1, 0};
int dj[4] = {0, 1, 0, -1};


int bfs(int start_i, int start_j) {
    queue<pair<int, int>> queue;

    queue.push({start_i, start_j});
    visited[start_i][start_j] = 1;

    int area = 1;
    while (!queue.empty()) {
        int i = queue.front().first;
        int j = queue.front().second;
        queue.pop();

        for (int dir = 0; dir < 4; dir++) {
            int ni = i + di[dir];
            int nj = j + dj[dir];

            if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
            if (visited[ni][nj] == 1) continue;
            if (board[ni][nj] == 1) {
                queue.push({ni, nj});
                visited[ni][nj] = 1;
                area++;
            } 
        }
    }

    return area;
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    int cnt = 0;
    int max_area = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (visited[i][j] == 1) continue;
            if (board[i][j] == 1) {
                int area = bfs(i, j);
                max_area = max(max_area, area);
                cnt++;
            }
        }
    }

    cout << cnt << endl;
    cout << max_area;

    return 0;
}