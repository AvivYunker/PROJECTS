import java.util.Scanner;
class decimal_to_binary {
	public static void main (String [] args) {
		Scanner SC = new Scanner(System.in);
		int x;
		int results;
		System.out.println("User, enter a number: ");
		x = SC.nextInt();
		results = decimal_to_octal(x);
		System.out.println(x + " --> " + results);
	}
	public static int decimal_to_octal (int num) {
		int res = 0;
		int level = 1;
		while (num > 0) {
			int tempI = (int)(num / 8);
			float tempF = (float)(num / 8.0);
			tempF = tempF - tempI;
			tempF = (int)(tempF * 8);
			res += tempF * level;
			level *= 10;
			num = tempI;
		}
	return res;
	}
}
