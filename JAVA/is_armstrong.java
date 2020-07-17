import java.util.Scanner;
import java.lang.Math;
class is_armstrong {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = is_armstrong(x);
		if (results == 1) {
			System.out.println(x + " is an Armstrong");
		}
		else {
			System.out.println(x + " is NOT an Armstrong");
		}
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
