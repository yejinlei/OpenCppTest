#include<stdio.h>
void test1(int x1, int x2){
    if(x1 > x2)
        if(x1 >= 10)
            if((2 * x1 + x2) == 40)
                if((x1 - x2) == 5)
                    printf("Solved!");
}