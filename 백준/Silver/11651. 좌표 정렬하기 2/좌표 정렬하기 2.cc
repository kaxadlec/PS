#include <bits/stdc++.h>

using namespace std;

int main() 
{   
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;
    
    vector<pair<int, int>> p;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        p.push_back(make_pair(b, a));
    }
    
    sort(p.begin(), p.end());
    
    for (const auto& x: p){
        cout << x.second << " " << x.first << "\n";
    }
    
    
    return 0;
}
