# include <iostream>
using namespace std;
int main () {
	int x;
	int orig;
	int res = 1;
	cout << "User, enter a number: ";
	cin >> x;
	orig = x;
	while (x > 0) {
		res *= x;
		x--;
	}
	cout << orig << " --> " << res << "\n";
}
