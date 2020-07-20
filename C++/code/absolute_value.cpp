# include <iostream>
using namespace std;

int absolute_value (int num) {
	if (num >= 0) {
		return num;
	}
	else {
		return -num;
	}
}

int main () {
	int x;
	int results;
	cout << "User, enter a number: ";
	cin >> x;
	results = absolute_value(x);
	cout << "|" << x << "| --> " << results << "\n";
}
