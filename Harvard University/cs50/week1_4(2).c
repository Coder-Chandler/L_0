//
//  main.c
//  p
//
//  Created by 殷楚楚 on 17/4/29.
//  Copyright © 2017年 Coder-Chandller. All rights reserved.
//

#include <stdio.h>
#include <unistd.h>

int
main(void)
{
    {
    int x = 1;
    int y = 2;
    int z = x + y;
    //printf("%d\n",z);
    }
    {
    float answer = (float)17 / 13;
    //printf("%.2f\n",answer);
    }
    {
        char c;
        double d;
        float f;
        int i;
        long l;
        long long ll;
        
        //printf("char: %d\n",sizeof(c));
        //printf("double: %d\n",sizeof(d));
        //printf("float: %d\n",sizeof(f));
        //printf("int: %d\n",sizeof(i));
        //printf("long: %d\n",sizeof(l));
        //printf("long long: %d\n",sizeof(ll));
    }
    
    {
        //printf("Temperature in F: ");
        //float f;
        //scanf("%f",&f);
        //float c = 5/9.0*(f-32);
        //printf("%.1f F = %.1f C\n",f,c);
    }
    
    {
        //printf("Give me an integer between 1 an 10: ");
        float n;
        //scanf("%f",&n);
        
        if (n >= 1 && n <= 3)
            printf("You picked a small number!\n");
        else if (n >= 4 && n <= 6)
            printf("You picked a medium number!\n");
        else if(n >= 7 && n <= 10)
            printf("You picked a big number!\n");
        else
            printf("You picked an invalid number!\n");
    }
    
    {
        for (int i = 0; i <= 100;i++)
        {
            printf("\rPercent complete: %d%%\r",i);
            fflush(stdout);
            sleep(1);
        }
        printf("for");
    }
    
    
}