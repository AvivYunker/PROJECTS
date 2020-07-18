import java.util.Scanner;
class is_prime {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = is_prime(x);
		if (results == 1) {
			System.out.println(x + " is a prime number.");
		}
		else {
			System.out.println(x + " is NOT a prime number.");
		}
	}
	public static int is_prime (int num) {
		int b = num - 1;
		while (b > 1) {
			if (num % b == 0) {
				return 0;
			}
			b--;
		}
		return 1;
	}
}
