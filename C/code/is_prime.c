# include <stdio.h>
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
	printf("User, enter a number: ");
	scanf("%d", &x);
	results = is_prime(x);
	if (results == 1) {
		printf("%d IS a prime\n", x);
	}
	else {
		printf("%d is NOT a prime\n", x);
	}
}
