# include <stdio.h>

int digit_sum (int num) {
	int results = 0;
	while (num > 0) {
		int temp = num % 10;
		results += temp;
		num /= 10;
	}
	return results;
}

int main () {
	int x;
	int results;
	printf("User, enter a number: ");
	scanf("%d", &x);
	results = digit_sum(x);
	printf("%d --> %d\n", x, results);
}
