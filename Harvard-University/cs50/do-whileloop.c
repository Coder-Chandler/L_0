#include <stdio.h>
int main()
{
    int number=200;
    int year=2014;
    do{
      year++;     
      number *= 1.2;       
    }while(number<1000);   //when use do-while,You must write a ";" behand the "while"!
    printf("we will have more than 1000 pople at %d\n", year);
    return 0;
}