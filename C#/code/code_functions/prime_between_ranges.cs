namespace aviv_yunker {
	class prime_between_ranges {
		public static void Main (string [] args) {
		string x,y;
		int lower, upper;
		System.Console.WriteLine("User, enter the lower edge: ");
		x = System.Console.ReadLine();
		System.Console.WriteLine("User, enter the upper edge: ");
		y = System.Console.ReadLine();
		lower = int.Parse(x);
		upper = int.Parse(y);
		System.Console.WriteLine("");

		between_ranges(lower, upper);
		System.Console.WriteLine("\nDONE!\n");
		}

		public static void between_ranges (int lower, int upper) {
			int results;
			while (lower <= upper) {
				results = is_prime(lower);
				if (results == 1) {
					System.Console.WriteLine("{0} is prime", lower);
				}
				lower++;
			}
		}

		public static int is_prime (int num) {
			int b = num - 1;
			while (b > 1) {
				if (num % b == 0) {
					return 0;
				}
				b--;
			}
			return 1;
		} 

	}
}
