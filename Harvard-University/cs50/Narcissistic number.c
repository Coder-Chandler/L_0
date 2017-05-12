#include <stdio.h>
int main()
{
    //Define a three digit named num,and his single digits named sd,ten digits named td,hundrend digits named hd
    int num, sd, td, hd;
    //Loop all three digits
    for(num = 100; num < 1000; num++)
    {
        //give me the hundrend digits
        hd = (int) num / 100;
        //give me the ten digits
        td = ((int) num % 100) / 10;
        //give me the Single digits
        sd = ((int) num % 100) % 10;
        //what is thr Narcissistic number ?
    if(hd * hd * hd + td * td * td + sd * sd * sd == num) 
        {
            printf("Narcissistic number : %d\n", num);    
        }
    }
    return 0;    
}
/*
##############
Use python-->
##############
def Narcissistic_number():
    return [i for i in xrange(100,1000) \
	if (i/100)**3 + (i%100/10)**3 + (i%10)**3 == i]
print Narcissistic_number()
*/