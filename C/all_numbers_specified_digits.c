# include <stdio.h>
# include <math.h>

int all_numbers_specified_digits(int digit) {
	int lower = Pow(10,digit-1);
	int upper = Pow(10,digit)-1;
	while (lower <= upper) {
		printf("%d", lower);
		lower--;
	}
}

int main () {
	int x;
	printf("User, enter the number of digits: ");
	scanf("%d", &x);
	all_numbers_specified_digits(x);
}
