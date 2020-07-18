import java.util.Scanner;
import java.lang.Math;
class binary_to_decimal {
	public static void main (String [] args) {
		Scanner SC = new Scanner (System.in);
		int x;
		int results;
		System.out.println("User, enter a BINARY number: ");
		x = SC.nextInt();
		if (valid_binary(x) == 1) {
			results = binary_to_decimal(x);
			System.out.println(x + " --> " + results);
		}
		else {
			System.out.println("Not a binary number...");
		}
	}

	public static int valid_binary (int num) {
		while (num > 0) {
			int temp = num % 10;
			if (temp >= 2) {
				return 0;
			}
			num /= 10;
		}
	return 1;
	}

	public static int binary_to_decimal (int num) {
		int res = 0;
		int level = 0;
		while (num > 0) {
			int temp = num % 10;
			temp = temp * (int)(Math.pow(2,level));
			res += temp;
			level++;
		num /= 10;
		}
	return res;
	}
}
