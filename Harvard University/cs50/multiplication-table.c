#include <stdio.h>
int
main ()
{
	int i, j, result;
	for (i = 9; i>0; i--)
	{
		for (j = 1; j <= i; j++)
		{
			result = i * j;
			printf ("%d*%d=%d\t",i, j, result);//"\t" means the space betwwen each operation,You can't just use the " "
		}
		printf ("\n");
	}
	return 0;
}