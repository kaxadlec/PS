# include <iostream>
# include <vector>
# include <queue>
# include <tuple>
# include <climits>
# include <algorithm>

using namespace std;
int N, M;

int move(vector<vector<int>>& board) {
    const int INF = INT_MAX;
    int min_dis = INF;

    vector<vector<vector<int>>> visited(N, vector<vector<int>>(M, vector<int>(2, 0)));
    queue<tuple<int, int, int, int>> q;
    q.emplace(0, 0, 1, 0);
    visited[0][0][0] = 1;

    while (!q.empty()) {
        auto [r, c, dis, is_broken] = q.front();
        q.pop();

        if (r == N-1 && c == M-1) {
            min_dis = min(min_dis, dis);
        }

        const vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (const auto& [dr, dc] : directions) {
            int nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                continue;
            }

            if (is_broken && board[nr][nc] == 0 && !visited[nr][nc][1]) {
                q.emplace(nr, nc, dis+1, 1);
                visited[nr][nc][1] = 1;
            } else if (!is_broken) {
                if (board[nr][nc] == 1 && !visited[nr][nc][1]) {
                    q.emplace(nr, nc, dis+1, 1);
                    visited[nr][nc][1] = 1;
                } else if (board[nr][nc] == 0 && !visited[nr][nc][0]) {
                    q.emplace(nr, nc, dis+1, 0);
                    visited[nr][nc][0] = 1;
                }
            }
        }
    }

    return (min_dis == INF) ? -1 : min_dis;
}

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    vector<vector<int>> board(N, vector<int>(M));
    for (int i = 0; i < N; ++i){
        string line;
        cin >> line;
        for (int j = 0; j < M; ++j){
            board[i][j] = line[j] - '0';
        }
    }

    int result = move(board);
    cout << result << endl;

    return 0;
}