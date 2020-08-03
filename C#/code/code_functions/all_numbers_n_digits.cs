using System;
using static System.Math;
namespace aviv_yunker {
	class allNumbersNDigits {
		public static void Main (string [] args) {
			string x;
			int num;
			System.Console.WriteLine("User, how many digits? ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			all_nums_n_digits(num);
			System.Console.WriteLine("\nDONE!\n");
		}
		public static void all_nums_n_digits (int num) {
			int lower = (int)(Math.Pow(10,num-1));
                        int upper = (int)(Math.Pow(10,num)-1);
			while (lower <= upper) {
				System.Console.WriteLine("{0}", lower);
				lower++;
			}
		}
	}
}
