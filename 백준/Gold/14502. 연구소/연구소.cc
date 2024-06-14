# include <iostream>
# include <vector>
# include <queue>
# include <tuple>
# include <algorithm>

using namespace std;

int N, M;
vector<vector<int>> board;
vector<pair<int, int>> blank_arr;
vector<pair<int, int>> virus_arr;

void spreading_virus(vector<vector<int>>& spread_board) {
    vector<vector<int>> visited(N, vector<int>(M, 0));
    queue<pair<int, int>> virus_queue;
    for (auto& virus : virus_arr) {
        virus_queue.push(virus);
    }

    while (!virus_queue.empty()){
        int r, c;
        tie(r, c) = virus_queue.front();
        virus_queue.pop();

        for (auto& dir : vector<pair<int, int>>{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}) {
            int nr = r + dir.first;
            int nc = c + dir.second;
            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
            if (visited[nr][nc]) continue;
            if (spread_board[nr][nc] == 0) {
                spread_board[nr][nc] = 2;
                visited[nr][nc] = 1;
                virus_queue.push({nr, nc});
            }
        }
    }
}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> N >> M;
    board.resize(N, vector<int>(M));

    for (int i=0; i < N; i++){
        for (int j=0; j < M; j++) {
            cin >> board[i][j];
            if (board[i][j] == 0) {
                blank_arr.emplace_back(i, j);
            } else if (board[i][j] == 2) {
                virus_arr.emplace_back(i, j);
            }
        }
    }

    int max_cnt = 0;

    vector <int> comb(blank_arr.size(), 1);
    fill(comb.begin(), comb.begin() + 3, 0);
    
    do {
        vector<vector<int>> new_board = board;
        for (int i = 0; i < blank_arr.size(); i++){
            if (comb[i] == 0) {
                int x = blank_arr[i].first;
                int y = blank_arr[i].second;
                new_board[x][y] = 1;
            }
        } 
        spreading_virus(new_board);
        
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (new_board[i][j] == 0) {
                    cnt += 1;
                }
            }
        }
        max_cnt = max(max_cnt, cnt);

    } while (next_permutation(comb.begin(), comb.end()));


    cout << max_cnt << endl;
    
    return 0;
}