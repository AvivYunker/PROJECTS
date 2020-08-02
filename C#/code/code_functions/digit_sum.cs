namespace aviv_yunker {
	class digit_sum {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = sum_digits_num(num);
			System.Console.WriteLine("sum-digits of {0} is {1}", num, results);
		}
		public static int sum_digits_num (int num) {
			int res = 0;
			while (num > 0) {
				res += num % 10;
				num /= 10;
			}
			return res;
		}
	}
}

