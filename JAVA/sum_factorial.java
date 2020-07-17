import java.util.Scanner;
class sum_factorial {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = sum_factorial(x);
		System.out.println(x + " --> " + results);
	}
	public static int sum_factorial (int num) {
		int res = 0;
		while (num > 0) {
			res += num;
			num--;
		}
		return res;
	}
}
