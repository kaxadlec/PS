#include <bits/stdc++.h>

using namespace std;

int main() 
{   
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    string str;
    cin >> str;
    
    list<char> editor(str.begin(), str.end());
    
    int M;
    cin >> M;
    
    auto cursor = editor.end();

    for (int i = 0; i < M; i++) {
        char command;
        cin >> command;
        
        if (command == 'L') {
            if (cursor != editor.begin()) cursor--;
        } else if (command == 'D') {
            if (cursor != editor.end()) cursor++;
        } else if (command == 'B') {
            if (cursor != editor.begin()) {
                cursor = editor.erase(--cursor);
            }
        } else {
            char newChar;
            cin >> newChar;
            editor.insert(cursor, newChar);
        }
        
    }
    for (auto& e : editor) {
            cout << e;
    }
    

    return 0;
}
