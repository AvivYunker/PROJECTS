# include <stdio.h>

int absolute_value (int num) {
	int res;
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
	printf("User, enter a number: ");
	scanf("%d", &x);
	results = absolute_value(x);
	printf("|%d| --> %d\n", x, results);
}
