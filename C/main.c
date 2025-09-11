#include <stdio.h>
#define MAX 10

typedef int arr[MAX];

int check_midian(int x, int y, int z);
arr *median_filter(arr x);
arr *sum_of_x1_x2(arr x1 , arr x2);


int check_midian(int i1, int i2, int i3){
    if(i1 > i2){
        i1 = i1;
    }else{
        i1 = i2;
    }
    
    return(i1 > i3)? i3: i2;
    
}

arr *median_filter(arr x){
    arr newArr = (arr *)malloc(sizeof(arr));
    if(newArr != NULL){
        for(int i = 0; i < MAX; i++){
            int i1 = x[i--];
            int i2 = x[i];
            int i3 = x[i++];
            newArr[i] =  check_midian(i1, i2, i3);
        }
    }else{
        printf("Memory Allocation failed\n");
    }
    return newArr;
}

arr *sum_of_x1_x2(arr x1 , arr x2){

}


int main(){
    arr x1;
    arr x2;

    arr *y1 = median_filter(x1);
    arr *y2 = median_filter(x2);


    return 0;
}