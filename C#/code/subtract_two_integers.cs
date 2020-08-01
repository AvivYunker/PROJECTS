using System;

namespace aviv_yunker {
        class subtract_two_integers {
                public static void Main (string[] args) {
			string x,y;
			int num1, num2;
                        Console.WriteLine("User, enter the first number: ");
			x = Console.ReadLine();
			Console.WriteLine("User, enter the second number: ");
			y = Console.ReadLine();
			num1 = int.Parse(x);
			num2 = int.Parse(y);
			Console.WriteLine("The subtraction is: " + (num1-num2));
                        // Console.ReadKey();
                }
        }
}

