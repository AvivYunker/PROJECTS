namespace aviv_yunker {
	class is_armstrong {
		public static void Main (string [] args) {
			string x;
			int num, num_dig, orig;
			int d = 0;
			int sums = 0;
			float temp;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);

			num_dig = num;
			orig = num;

			if (num_dig == 0) {
				d = 1;
			}
			else {
				while (num_dig > 0) {
					d++;
					num_dig /= 10;
				}
			}
			while (num > 0) {
				temp = num % 10;
				temp = (float)(Math.Pow(temp,d));
				sums += temp;
				num /= 10;
			}
			if (sums == orig) {
				System.Console.WriteLine("{0} IS an Armstrong", orig);
			}
			else {
				System.Console.WriteLine("{0} is NOT an Armstrong", orig);
			}
		}
	}
}
