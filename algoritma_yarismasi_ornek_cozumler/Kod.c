#include <stdio.h>
#include <conio.h>
int main()
{
    int v, f, b, n;
    do
    {
    printf("vize Notunu Giriniz:\n");
    scanf("%d", &v);
    }while(v>100);
    do
    {
    printf("Final Notunu Giriniz:\n");
    scanf("%d", &f);
    }while(f>100);
    n=f*0.6+v*0.4;
    if(f<50)
    {
        if(n<50)
        {
            do
            {
            printf("Butunleme Notunu Giriniz:\n");
            scanf("%d", &b);
            }while(b>100);
            n=b*0.6+v*0.4;
            if(n<50)
        }
        else
        printf("Notun:FD");
    }
    else if(n<50)
    {
    do
    {
            printf("Butunleme Notunu Giriniz:\n");
            scanf("%d", &b);
    }while(b>100);
    n=b*0.6+v*0.4;
    };
    if(n<50)
    {
        if(b<50)
    printf("Notun:FF");
        else
     printf("Notun:FD");
    }
    else if(n<101)
    {
    printf("Dersi gectin\nOrtalamaniz:%d\n", n);
        if(n<55)
        printf("Notun: CC");
        else if(n<65)
        printf("Notun: CB");
        else if(n<75)
        printf("Notun: BB");
        else if(n<85)
        printf("Notun: BA");
        else if(n<101)
        printf("Notun: AA");
        else
        printf("Something wrong.");
    }
    else
    printf("Girdigin notlar hatalý!");
    getch();
}
