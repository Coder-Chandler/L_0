#include <stdio.h>
int main()
{
    int sum = 0;
    int i;
    for(i=1; i<=10; i++)
    {
        printf("%d\n", i);
        if(i==3)
        {
            goto END;
        }                   
    }
    END:printf("end!");  
    return 0;    
}

/*
COMPUTE THE SUM FROM 1 TO 100;(1<= i <= 100)

#include <stdio.h>
int main(void){
    int i,sum=0;
    i=1;
    loop: if(i<=100){
        sum=sum+i;
        i++;
        goto loop;
    }
    printf("%d\n",sum);
    return 0;
}
*/