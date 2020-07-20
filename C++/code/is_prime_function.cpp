# include <iostream>
using namespace std;

int is_prime (int num) {
	int b = num - 1;
	while (b > 1) {
		if (num % b == 0) {
			return 0;
		}
		b--;
	}
	return 1;
}

int main() {
	int x;
	int results;
	cout << "User, enter a number: ";
	cin >> x;
	results = is_prime(x);
	if (results == 1) {
		cout << x << " is a prime\n";
	}
	else {
		cout << x << " is NOT a prime\n";
	}
}
