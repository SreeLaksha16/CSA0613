#include <stdio.h>

int T(int n)
{
    if (n <= 1)
        return 1;

    return 2 * T(n / 2) + (n * n);
}

int main()
{
    int n;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    printf("Result of T(%d) = %d\n", n, T(n));

    printf("Time Complexity using Master Theorem: Theta(n^2)\n");

    return 0;
}
