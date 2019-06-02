#include <stdio.h>
#include <string.h>
int main(){
    char greeting[] = "Apple_Samsung_Google_BING";
    int i;
    for(i=0;i<sizeof(greeting); i++){
        if(i%2 == 0){
            int x = greeting[i] + 2;
            printf("%c",x);
            }
        else{
            int x = greeting[i] -1;
            printf("%c",x);
            }
    }
    printf("\n\n");
    return 0;
}
