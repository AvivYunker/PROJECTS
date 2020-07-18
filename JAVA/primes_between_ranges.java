import java.util.Scanner;
class primes_between_ranges {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int lwr;
		int upr;
		System.out.println("User, enter the lower edge: ");
		lwr = SC.nextInt();
		System.out.println("User, enter the upper edge: ");
		upr = SC.nextInt();
		between_ranges(lwr, upr);
	}
	public static void between_ranges (int lower, int upper) {
		int results;
		while (lower <= upper) {
			results = is_prime(lower);
			if (results == 1) {
				System.out.println(lower + " is prime.");
			}
			lower++;
		}
	System.out.println("\nDONE!\n");
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
