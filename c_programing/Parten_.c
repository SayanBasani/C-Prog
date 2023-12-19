#include <stdio.h>

int main()
{

    int i, j, k, l, m, x = 4;
    for (j = x - 1; j >= -1; j--)
    {
        for (i = 0; i < x; i++)
        {
            if (j < i)
            {
                printf("*");
            }
            else
            {
                printf(" ");
            }
        }
        printf("\n");
    }

    return 0;
}