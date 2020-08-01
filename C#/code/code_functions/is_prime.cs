namespace aviv_yunker {
	class is_prime {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = is_number_prime(num);
			if (results == 1) {
				System.Console.WriteLine("{0} IS a prime number", num);
			}
			else {
				System.Console.WriteLine("{0} is NOT a prime number", num);
			}
		}
		public static int is_number_prime (int num) {
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
