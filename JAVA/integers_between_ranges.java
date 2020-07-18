import java.util.Scanner;
class integers_between_ranges {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int lwr;
		int upr;
		System.out.println("User, enter the lower edge: ");
		lwr = SC.nextInt();
		System.out.println("User. enter the upper edge: ");
		upr = SC.nextInt();
		between_ranges(lwr, upr);
	}
	public static void between_ranges (int lower, int upper) {
		while (lower <= upper) {
			System.out.println(lower);
			lower++;
		}
	}
}
