# include <stdio.h>
int main () {
	int num1;
	int num2;
	printf("User, enter first number: ");
	scanf("%d", &num1);
	printf("User, enter second number: ");
	scanf("%d", &num2);
	printf("%d+%d=%d\n",num1, num2, (num1+num2));
}
