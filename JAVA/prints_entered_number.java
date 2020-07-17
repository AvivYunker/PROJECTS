import java.util.Scanner;
class prints_entered_number {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		System.out.println("User, enter a number: ");
		int x = SC.nextInt();
		System.out.println("The entered number is: " + x);
	}
}
