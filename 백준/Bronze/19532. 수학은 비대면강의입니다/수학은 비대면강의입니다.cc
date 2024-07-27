#include <iostream>

using namespace std;

int main()
{
	int a, b, c, d, e, f;
	double x, y;

	cin >> a >> b >> c >> d >> e >> f;

	if (a == 0) {
		y = c / b;
		x = (f - e * y) / d;
	}
	else if (d == 0) {
		y = f / e;
		x = (c - b * y) / a;
	}
	else {
		y = (a * f - c * d) / (a * e - b * d);
		x = (c - b * y) / a;
	}

	cout << x << " " << y;
	return 0;
}
