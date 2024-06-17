# include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int A, B, C;
    int performace;

    cin >> A >> B >> C;
    performace = 3 * B * C / A;

    cout << performace;

    return 0;
}