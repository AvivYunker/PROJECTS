import java.util.Scanner;
class absoute_value {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = absolute_value(x);
		System.out.println("|" + x + "| --> " + results);
	}
	public static int absolute_value (int num) {
		if (num >= 0) {
			return num;
		}
		else {
			return -num;
		}
	}
}
