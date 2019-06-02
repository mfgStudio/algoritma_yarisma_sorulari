#include <stdio.h>
#include <math.h>

int main()
{
    int n,b=0, i;
printf("Bir sayi girin.");
scanf("%d", &n);
for(i=0; i<n; i++)
{
    b=b+i;
};
    b=b*2;
    b=b+n;
    b=sqrt(b);
    printf("\n deger:%d", b);
    getch();
}
