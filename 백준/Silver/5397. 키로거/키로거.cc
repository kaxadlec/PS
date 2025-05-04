#include <bits/stdc++.h>

using namespace std;

int main() 
{   
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;  
    cin >> T;
    
    for (int tc = 0; tc < T; tc++) {
        string s;
        cin >> s;
        
        list<char> keylogger;
        auto cursor = keylogger.begin();
        
        for (auto& c : s) {
            if (c == '-') {
                if (cursor != keylogger.begin()) {
                    cursor = keylogger.erase(--cursor);
                }
            } else if (c == '<') {
                if (cursor != keylogger.begin()) cursor--;
            } else if (c == '>') {
                if (cursor != keylogger.end()) cursor++;
            } else {
                keylogger.insert(cursor, c);
            }
        }
        
        for (auto& c : keylogger) {
            cout << c;
        }
        cout << "\n";
    }
    return 0;
}
