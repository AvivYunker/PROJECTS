using System;
using static System.Math;
namespace aviv_yunker {
	class reverseNumber {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = reverse_number(num);
			System.Console.WriteLine("{0} --> {1}", x, results);
		}
		public static int reverse_number (int num) {
			int res = 0;
			int d = digit_counter(num);
			int level = (int)Math.Pow(10,d-1);
			while (num > 0) {
				int temp = num % 10;
				res += temp*level;
				level /= 10;
				num /= 10;
			}
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
