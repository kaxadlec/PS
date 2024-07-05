#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> adj;
vector<int> visited;
int order = 1;

void dfs(int cur) {
    visited[cur] = order++;
    for (int nxt : adj[cur]) {
        if (visited[nxt] == 0) dfs(nxt);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int N, M, R;
    cin >> N >> M >> R;

    adj.resize(N + 1);
    visited.assign(N + 1, 0);

    while(M--) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    for(int i = 1; i <= N; i++) {
        sort(adj[i].begin(), adj[i].end());
    }

    dfs(R);

    for(int i = 1; i <= N; i++) {
        cout << visited[i] << '\n';
    }


}