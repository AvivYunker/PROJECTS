import java.util.Scanner;
import java.util.Random;
class n_dice_rolls {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		int x;
		int rolls = new int [];
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		n_dice_rolls(rolls, x);
 	}
	public static void n_dice_rolls (int rolls, int x) {
		Random rn = new Random();
		int n = 1 + (int)(Math.random() * ((6 - 1) + 1))
		
	}
}
