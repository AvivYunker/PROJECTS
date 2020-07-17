import java.util.Scanner;
class sum_two_integers {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		int num1;
		int num2;
		System.out.println("User, enter first number: ");
		num1 = SC.nextInt();
		num2 = SC.nextInt();
		System.out.println("The sum is: " + (num1 + num2));
	}
}
