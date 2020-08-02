namespace aviv_yunker {
	class digitAverage {
		public static void Main (string [] args) {
			string x;
			int num;
			float results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = digit_average(num);
			System.Console.WriteLine("\ndigit_average of: {0}\nis: {1}", x, results);
		}
		public static float digit_average (int num) {
			float res = 0;
			int d = digit_counter(num);
			while (num > 0) {
				res += num % 10;
				num /= 10;
			}
			res /= d;
			return res;
		}
		public static int digit_counter (int num) {
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
