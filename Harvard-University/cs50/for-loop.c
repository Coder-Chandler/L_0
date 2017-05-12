#include <stdio.h>
int
main ()
{
	int sum, num;
	for (sum = 0, num = 0; num <= 3 && sum <= 5 && 1; num++, sum++)// "&&1" means progranm does not run if the value equal 0 
	{
		sum += num;
		printf ("num = %d, sum = %d\n", num, sum);
	}
}

/*
print --> 
num = 0, sum = 0
num = 1, sum = 2
num = 2, sum = 5
*/
