using System;
using static System.Math;
namespace aviv_yunker {
	class is_armstrong {
		public static void Main (string [] args) {
			string x;
			int num, results;
			System.Console.WriteLine("User, enter a number: ");
			x = System.Console.ReadLine();
			num = int.Parse(x);
			results = is_num_armstrong(num);
			if (results == 1) {
				System.Console.WriteLine("{0} IS an Armstrong", num);
			}
			else {
				System.Console.WriteLine("{0} is NOT an Armstrong", num);
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
