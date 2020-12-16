#include<stdio.h>
int main()
{
	int a = 5;
	int *p;

	p = &a;
	printf("%d\n", *p);
	printf("%p\n", p);
	printf("\n");

	*p = *p + 1;
	printf("%d\n", *p);
	printf("%p\n", p);
	printf("\n");

	p = p + 1;
	printf("%d\n", *p);
	printf("%p\n", p);
	printf("\n");

	p = p + 1000000;
	printf("%d\n", *p);
	printf("%p\n", p);
	printf("\n");

	return 0;
}

