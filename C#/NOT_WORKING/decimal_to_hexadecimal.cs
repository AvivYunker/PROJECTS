namespace aviv_yunker {
	class decimalToHexadecimal {
		public static void Main (string [] args) {
			string x, results;
			int num;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = decimal_to_hexadecimal(x);
			System.Console.WriteLine("DEC({0}) --> HEX({1})", x, results);
		}
		public static string decimal_to_hexadecimal (int num) {
			string tmp, res;
			int tempI;
			float tempF;
			while (num > 0) {
				tempI = (int)(num / 2);
				tempF = (float)(num / 2.0);
				tempF = (float)(2 * (tempF - tempI));
				if ((int)tempF >= 0 && (int)tempF <= 9) {
					tmp += tempF;
				}
				else if ((int)tempF >= 10 && (int)tempF <= 16) {
					tmp += (chr)(tempF+55);
				}
				num = tempI;
			}
			for (int i = tmp.length-1; i >= 0; i--) {
				res += tmp[i];
			}
			return res;
		}
	}
}
