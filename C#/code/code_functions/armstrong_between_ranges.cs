using System;
using static System.Math;
namespace aviv_yunker {
	class armstrong_between_ranges {
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

			between_ranges(lower,upper);
			
			System.Console.WriteLine("\nDONE!\n");
		}

		public static void between_ranges (int lower, int upper) {
			int results;
			while (lower <= upper) {
				results = is_num_armstrong(lower);
				if (results == 1) {
					System.Console.WriteLine("{0} is an Armstrong", lower);
				}
				lower++;
			}
		}

		public static int is_num_armstrong (int num) {
			int orig = num;
			int d = digit_counter(num);
			int temp, sums = 0;
			while (num > 0) {
				temp = num % 10;
				temp = (int)Math.Pow(temp,d);
				sums += temp;
				num /= 10;
			}
			if (sums == orig) {
				return 1;
			}
			else {
				return 0;
			}
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
