#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int N; 
	cin >> N;
	
	vector<long long> arr(N);
	long long B, C;
	long long res = 0;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	
	cin >> B >> C;

	for (int i = 0; i < N; i++) {
		res += 1;
		if (arr[i] > B) {
			if ((arr[i] - B) % C == 0) {
				res += (arr[i] - B) / C;
			}
			else {
				res += (arr[i] - B) / C + 1;
			}
		}
	}
	
	cout << res;
	
	return 0;
}
