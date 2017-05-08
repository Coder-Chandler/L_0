#include <stdio.h>
#include <unistd.h>

int
main (int argc,char *argv)
{
	for (int i = 65; i < 65 + 26; i++)
		printf ("%c: %d\n", (char) i, i);
	printf ("\n");
	for (int i = 97;i <97 +26; i++)
		printf ("%c: %d\n",(char) i ,i);
}


