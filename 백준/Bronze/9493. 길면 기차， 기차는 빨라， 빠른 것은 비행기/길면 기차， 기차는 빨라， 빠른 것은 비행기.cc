# include <iostream>
# include <cmath>

using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while(1) {
        int M, A, B;
        cin >> M >> A >> B;
        if (M==0 && A==0 && B==0) {
            break;
        }

        int hour, minute, second;

        double train_hour, airplane_hour;
        train_hour = static_cast<double>(M) / A;
        airplane_hour = static_cast<double>(M) / B;
        
        double hourDiff = train_hour - airplane_hour;
        hour = static_cast<int>(hourDiff);
        double minuteDiff = (hourDiff - hour) * 60;
        minute = static_cast<int>(minuteDiff);
        double secondDiff = (minuteDiff - minute) * 60;
        second = round(secondDiff);

        if (second == 60) {
            minute++;
            second = 0;
        }

        if (minute == 60) {
            minute = 0;
            hour++;
        }

        cout << hour << ":";

        if (minute >=10) {
            cout << minute << ":";
        }
        else {
            cout << "0" << minute << ":";
        }

        if (second >= 10) {
            cout << second << endl;
        }
        else {
            cout << "0" << second << endl;
        }
        
    }
    

    return 0;
}