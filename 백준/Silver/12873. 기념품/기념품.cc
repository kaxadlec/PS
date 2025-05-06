#include <queue>
#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    queue<int> q;
    for (int i = 1; i <= n; i++) {
        q.push(i);
    }

    long long t = 1;
    while (q.size() > 1) {
        long long moves = t * t * t % q.size();
        if (moves == 0) moves = q.size();

        for (int i = 0; i < moves - 1; ++i) {
            q.push(q.front());
            q.pop();
        }

        q.pop();
        ++t;
    }

    cout << q.front();
    return 0;
}
