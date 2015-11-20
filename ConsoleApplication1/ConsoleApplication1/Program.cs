using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    internal class Program
    {
        private static string var = "";

        private static void Main(string[] args)
        {
        TRY:
            {
                var = Console.ReadLine();

                switch (var)
                {
                    case "":
                        Console.WriteLine("dit is leeg");
                        break;

                    case "karel":
                        Console.WriteLine("dit is karel");

                        break;

                    default:
                        Console.WriteLine("dit is geen van allen");

                        break;
                }

                goto TRY;
            }
        }
    }
}