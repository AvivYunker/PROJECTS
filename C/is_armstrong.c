# include <stdio.h>
# include <math.h>
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
		int temp = num % 10;
		temp = pow(temp, d);
		sums += temp;
		num /= 10;
	}
	if (sums == orig) {
		return 1;
	}
	else {
		return 0;
	{
}

int between_ranges(int lower, int upper) {
	int results;
	while (lower <= upper) {
		results = is_armstrong(lower);
		if (results == 1) {
			printf("%d is an Armstrong", lower);
		}
		lower++;
	}
}

int main () {
	int lwr;
	int upr;
	printf("User, enter the lower edge: ");
	scanf("%d", &lwr);
	printf("User, enter the upper edge: ");
	scanf("%d", &upr);
	between_ranges(lwr, upr);
}
