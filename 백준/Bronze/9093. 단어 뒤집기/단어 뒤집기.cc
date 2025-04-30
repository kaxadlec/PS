#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

int T;
int main() 
{   
    string sentence;
    cin >> T;
    cin.ignore();
    for (int i = 0; i < T; i++) {
        getline(cin, sentence);
        stringstream ss(sentence);
        string word;
        
        while (ss >> word) {
            reverse(word.begin(), word.end());
            cout << word << " ";
        }
        cout << endl;
    }
    return 0;
}
