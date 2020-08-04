namespace aviv_yunker {
	class isIdenticalDigits {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = is_identical_digits(num);
			if (results == 1) {
				System.Console.WriteLine("{0} HAS identical digits", x);
			}
			else {
				System.Console.WriteLine("{0} does NOT have indentical digits", x);
			}
		}
		public static int is_identical_digits (int num) {
			int dig = num % 10;
			int temp;
			while (num > 0) {
				temp = num % 10;
				if (dig != temp) {
					return 0;
				}
				num /= 10;
				//System.Console.WriteLine("{0}", num);
			}
			return 1;
		}
	}
}
