# include <stdio.h>
int factorial (int num) {
	int res = 1;
	while (num > 0) {
		res *= num;
		num -= 1;
	}
	return res;
}
int main () {
	int x;
	int results;
	printf("User, enter a number: ");
	scanf("%d", &x);
	results = factorial(x);
	printf("%d --> %d\n", x, results);
}
