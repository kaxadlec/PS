# include <bits/stdc++.h>
using namespace std;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int num, odd_sum=0, num_min=100, odd_check=0;

    for (int i=0; i<7; i++){
        cin >> num;
        if (num & 1) {
            odd_sum += num;
            if (odd_check ==0) odd_check = 1;
            
            if (num_min > num){
                num_min = num;
            }
        }
    }

    if (odd_check)
        cout << odd_sum << "\n" << num_min;
    else cout << "-1";

}

