namespace aviv_yunker {
	class digit_counter {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = digit_count(num);
			System.Console.WriteLine("{0} has {1} digits", x, results);
		}
		public static int digit_count (int num) {
			int counter = 0;
			if (num == 0) {
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
	}
}

