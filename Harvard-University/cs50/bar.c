#include <stdio.h>
int 
main()
{
  int a;
  char *s = "hello, world";
  printf ("%s\n",&s[7]);
  a = 5;
  foo(a);
  return 0;
}

int
foo(int n)
{
  int b;
  b = n;
  b *= 2;
  bar(b);
  return b;
}

void
bar(int m)
{
  printf ("Hi, I'm bar!\n");
}
