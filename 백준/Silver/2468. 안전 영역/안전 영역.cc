#include <bits/stdc++.h>

using namespace std;

int N;
vector<vector<int>> board;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};


void bfs(int x, int y, int h, vector<vector<bool>>& visited) {
    queue<pair<int, int>> queue;
    queue.push({x, y});
    visited[x][y] = true;

    while (!queue.empty()) {
        auto [x, y] = queue.front();
        queue.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];
            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && board[nx][ny] > h) {
                queue.push({nx, ny});
                visited[nx][ny] = true;
            }
        }
    }

}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int maxH = 0, maxCnt = 0;
    cin >> N;
    board.resize(N, vector<int>(N, 0));

    for(int i = 0; i < N; i++) {
        for(int j = 0; j < N; j++) {
             cin >> board[i][j];
             maxH = max(maxH, board[i][j]);
        }
    }   

    for (int h = 0; h < maxH + 1; h++) {
        int cnt = 0;
        vector<vector<bool>> visited(N, vector<bool>(N, false));
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] > h && !visited[i][j]) {
                    bfs(i, j, h, visited);
                    cnt++;
                }
            }
        } 
        maxCnt = max(cnt, maxCnt);
    }

    cout << maxCnt;
}