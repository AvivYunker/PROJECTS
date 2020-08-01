namespace aviv_yunker {
	class prints_between_ranges {
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
			while (lower <= upper) {
				System.Console.WriteLine("{0}", lower);
				lower++;
			}
		}
	}
}
