namespace aviv_yunker {
	class decimalToBinary {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a DECIMAL number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = decimal_to_binary(num);
			System.Console.WriteLine("DEC({0}) = BIN({1})", num, results);
		}
		public static int decimal_to_binary (int num) {
			int tempI, res = 0, level = 1;
			float tempF;
			while (num > 0) {
				tempI = (int)(num / 2);
				tempF = (float)(num / 2.0);
				tempF = (float)(2 * (tempF - tempI));
				res += (int)(tempF * level);
				level *= 10;
				num = tempI;
			}
			return res;
		}
	}
}
