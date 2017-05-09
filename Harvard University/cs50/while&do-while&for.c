#include <stdio.h>
int main()
{
    /* 小伙伴们：
           选择你们认为最合理的循环结构完成功能吧 */
    int sum = 0;  //定义计算结果变量sum
    int i = 1;    //定义循环数字变量i
    int flag = 1; //定义符号状态变量flag
    /*
    //使用while循环
    while(i<=100)
    {
        sum += i*flag;
        i++;
        flag *= -1;
    }
    
    i = 1;  //重新初始化变量i
    
    //do-while循环
    do{
        sum += i*falg;
        i++;
        flag *= -1;
    }while(i<=100);
    
    i = 1;  //重新初始化变量i
    */
    //使用for循环
    for(i=1;i<=100;i++)
    {
        if (i % 2 == 0)
        {
            sum -= i;
        }
        else
        {
            sum += i;
        }
    }
    
    printf("sum=%d\n",sum); 
    
    return 0;    
}