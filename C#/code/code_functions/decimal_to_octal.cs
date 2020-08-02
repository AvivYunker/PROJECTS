namespace aviv_yunker {
	class decimalToOctal {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a DECIMAL number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = decimal_to_octal(num);
			System.Console.WriteLine("DEC({0}) = OCT({1})", num, results);
		}
		public static int decimal_to_octal (int num) {
			int tempI, res = 0, level = 1;
			float tempF;
			while (num > 0) {
				tempI = (int)(num / 8);
				tempF = (float)(num / 8.0);
				tempF = (float)(8 * (tempF - tempI));
				res += (int)(tempF * level);
				level *= 10;
				num = tempI;
			}
			return res;
		}
	}
}

