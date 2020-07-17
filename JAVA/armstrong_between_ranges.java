import java.util.Scanner;
import java.lang.Math;
class armstrong_between_ranges {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		int lwr;
		int upr;
		System.out.println("User, enter the lower edge: ");
		lwr = SC.nextInt();
		System.out.println("User, enter the upper edge: ");
		upr = SC.nextInt();
		between_ranges(lwr, upr);
	}
	public static void between_ranges (int lower, int upper) {
		while (lower <= upper) {
			int results = is_armstrong(lower);
			if (results == 1) {
				System.out.println(lower + " is an Armstrong");
			}
			lower++;
		}
		System.out.println("\nDONE!\n");
	}
	public static int is_armstrong (int num) {
		int orig = num;
		int d = digit_counter(num);
		int sums = 0;
		while (num > 0) {
			int temp = num % 10;
			temp = (int)Math.pow(temp,d);
			sums += temp;
			num /= 10;
		}
		if (sums == orig) {
			return 1;
		}
		else {
			return 0;
		}
	}
	public static int digit_counter (int num) {
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
}

