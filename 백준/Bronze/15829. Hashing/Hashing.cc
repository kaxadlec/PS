# include <iostream>
# include <string>

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int L;
    string s;

    cin >> L;
    cin >> s;

    long long H = 0;
    long long r = 1;
    long long a;
    long long M = 1234567891;

    for (int i=0; i<L; i++) {
        a = s[i] - 'a' + 1;
        H = (H + a*r) % M;
        r = (r * 31) % M; 
    }

    cout << H << endl;

    return 0;
}