# include <stdio.h>

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

int main () {
	int x;
	int results;
	printf("User, enter a number: ");
	scanf("%d", &x);
	results = digit_counter(x);
	printf("%d has %d digits\n", x, results);
}
