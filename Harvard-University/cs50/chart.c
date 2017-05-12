#include <stdio.h>
#include <unistd.h>

int
main (int argc,char *argv[])
{
	//print top row of numbers
	printf ("\n   ");
	for (int i = 1; i <= 10; i++)
		printf ("%d  ", i);
    printf ("\n");
	
	//print rows of holes,with letters in leftw column
	for (int i = 0; i < 10; i++)
	{
		printf ("%c  ",'A' + i);
		for (int j = 1; j <= 10; j++)
			printf ("0  ");
		printf ("\n"); 
	}
	printf ("\n");
}
		

