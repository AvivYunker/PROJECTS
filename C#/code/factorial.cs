namespace aviv_yunker {
	class factorial {
		public static void Main (string [] args) {
			string x;
			int num;
			int res = 1;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			while (num > 0) {
				res *= num;
				num --;
			}
			System.Console.WriteLine("{0} --> {1}", x, res);
		}
	}
}
