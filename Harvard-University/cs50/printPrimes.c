#include <stdio.h

int main()
{
    int m, n;
	//start from 2 to 50;2 is the smallest prime
    for(m=2; m<=50; m++)
    {   
		//From 2 to m, except "m" itself whether still have other factors
		for(n=2; n<m; n++)
        {	
			// if still have other factors,then break
            if(m % n == 0)       
                break;              
		}
        /*
		If m is a even,such as "4",you know 4 % 2 == 0(True),
		So it will be break and print if there is no "if(m == n)"
		Then,as you konw,a BUG!!!!
		*/
		if(m == n) 
            printf("%d  ", m);
	}
	return 0;    
}

