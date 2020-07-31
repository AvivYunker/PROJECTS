# include <iostream>
# include <math.h>
using namespace std;
int main () {
	int x;
	int lower;
	int upper;
	cout << "User, enter the number of digits: " << endl;
	cin >> x;
	lower = (int)(pow(10,x-1));
	upper = (int)(pow(10,x)-1);
	// cout << "The entered number is: " << x << endl;
	while (lower <= upper) {
		cout << lower << endl;
		lower++;
	}
}

