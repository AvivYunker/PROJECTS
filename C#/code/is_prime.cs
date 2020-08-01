namespace aviv_yunker {
	class is_prime {
		public static void Main (string [] args) {
			string x;
			int num, b, answer = 1;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			b = num - 1;
			while (b > 1) {
				if (num % b == 0) {
					answer = 0;
					break;
				}
				b--;
			}
			if (answer == 0) {
				System.Console.WriteLine("{0} is NOT a prime", x);
			}
			else {
				System.Console.WriteLine("{0} IS a prime", x);
			}
		}
	}
}
