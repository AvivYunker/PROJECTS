# include <iostream>
# include <math.h>
using namespace std;

int digit_counter (int num) {
	int counter = 0;
	if (num == 0) {
		counter = 1;
	}
	else {
		while (num > 0) {
			counter++;
			num /= 10;
		}
	}
	return counter;
}

int is_armstrong (int num) {
	int orig = num;
	int d = digit_counter(num);
	int sums = 0;
	while (num > 0) {
		int temp;
		temp = num % 10;
		temp = pow(temp, d);
		sums += temp;
		num /= 10;
	}
	if (sums == orig) {
		return 1;
	}
	else {
	return 0;
	}
}

int main() {
	int x;
	int results;
	cout << "User, enter a number: ";
	cin >> x;
	results = is_armstrong(x);
	if (results == 1) {
		cout << x << " IS an Armstrong\n";
	}
	else {
		cout << x << " is NOT an Armstrong\n";
	}
}
