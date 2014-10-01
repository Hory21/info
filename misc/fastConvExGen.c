#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main()
{
	int a[4];
	int i;
	char *c = malloc(1);

	while (1)
	{
		(*c) = 0;
		for (i = 0; i <= 3; i++)
		{
			a[i] = rand() % 2;
			printf("%d", a[i]);
		}
		printf("\n");
		scanf("%c\n", c);
	}
	return (0);
}
