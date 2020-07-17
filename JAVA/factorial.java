import java.util.Scanner;
class factorial {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = factorial(x);
		System.out.println(x + " --> " + results);
	}
	public static int factorial (int num) {
		int res = 1;
		while (num > 0) {
			res *= num;
			num -= 1;
		}
		return res;
	}
}
