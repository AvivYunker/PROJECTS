namespace aviv_yunker {
	class identicalDigitsBetweenRanges {
		public static void Main (string [] args) {
			string x,y;
			int lwr, upr;
			System.Console.WriteLine("User, enter the lower edge: ");
			x = System.Console.ReadLine();
			System.Console.WriteLine("User, enter the upper edge: ");
			y = System.Console.ReadLine();

			lwr = int.Parse(x);
			upr = int.Parse(y);

			between_ranges(lwr,upr);
			System.Console.WriteLine("\nDONE!\n");
		}
		public static void between_ranges (int lower, int upper) {
			int results;
			while (lower <= upper) {
				results = is_identical_digits(lower);
				if (results == 1) {
					System.Console.WriteLine("{0} has identical digits", lower);
				}
				lower++;
			}
		}
		public static int is_identical_digits (int num) {
			int dig = num % 10;
			num /= 10;
			while (num > 0) {
				if ((num % 10) != dig) {
					return 0;
				}
				num /= 10;
			}
			return 1;
		}
	}
}
