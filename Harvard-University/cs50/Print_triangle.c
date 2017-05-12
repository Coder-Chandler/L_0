#include <stdio.h>
int
main()
{
	int i, j, k;
	for (i = 1; i <= 4; i++)
	{
		for (j = i; j < 5; j++)
		{
			printf (" ");
		}
		for (k = 1; k <= 2*i-1;k++)
		{
			printf ("*");
		}
		printf ("\n");
	}
	return 0;
}
/*
Use python -->

for i in range(1,5):
    for j in range(i,5):
	    print ' ',
    for k in range(1,2*i):
	    print '*',
	print '\n'

1、每行输出的空格数等于（最后一行*号数减去当前行的*号数）除2；

2、每行输出的*号等于行数的乘积乘2再减1；

3、参考代码：