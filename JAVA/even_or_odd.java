import java.util.Scanner;
class even_or_odd {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = even_or_odd(x);
		if (results == 1) {
			System.out.println(x + " is an even number.");
		}
		else {
			System.out.println(x + " is an odd number.");
		}
	}
	public static int even_or_odd (int num) {
		if (num % 2 == 0) {
			return 1;
		}
		else {
			return 0;
		}
	}
}
