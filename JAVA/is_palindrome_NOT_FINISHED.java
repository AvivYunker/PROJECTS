import java.util.Scanner;
class is_palindrome {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in)
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = is_palindrome(x);
		if (results == 1) {
			System.out.println(x + " is a palindrome");
		else {
			System.out.println(x + " is NOT a palindrome");
		}
	}
	public static int is_palindrome (int num) {
		int d = digit_counter(num);
		int arr[] = new int[d];
		 
	}
	public staic int digit_counter (int num) {
		int counter;
		if (num == int(0)) {
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
	public static int digits_to_array (int arr[], int num) {

	}
}
