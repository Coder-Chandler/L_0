#include <stdio.h>
int
main ()
{
  int a;
  int (*p);
  p = (&a);
  printf ("address p is %d\n",p);
  printf ("value p is %d\n",(*p));
  int b = 20;
  (*p) = b;
  printf ("address pis %d\n",p);
  printf ("value p is %d\n",(*p));
  return 0;
}
