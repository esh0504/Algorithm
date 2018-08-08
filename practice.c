#include <stdio.h>

int main(void)

{
	for (int numa = 1; numa<10; numa++)
	{
	
		for (int numb = 1; numb<10; numb++)
		{
			
			if(numa*11+numb*11==99)
			{
				printf("%d,%d\n", numa, numb);
			}
		}
	}
	return 0;
}