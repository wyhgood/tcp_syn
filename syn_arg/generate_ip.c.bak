
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

/*
  本程序用来生产随机的ip地址。
  传入缓冲区的指针即可。
*/

#define SUM 10000
//const int num = 1000;

struct data{
  char array[SUM][50];
};

int generate_ip(struct data *ret){
  
  srand((unsigned)time(NULL));
  
  //char ret[num][50];
  int i;
  int t;
  //for(t=0; t<=m-1; t++){
  for(i=0; i<SUM; i++){
    //char ip = ip_sum[i];
    char ip[50];
  int ip1 = rand()%255+1;
  int ip2 = rand()%255+1;
  int ip3 = rand()%255+1;
  int ip4 = rand()%255+1;
  
  //char ip[50];
  char ip1_[50];
  sprintf(ip1_, "%d", ip1);
  char ip2_[50];
  sprintf(ip2_, "%d", ip2);
  char ip3_[50];
  sprintf(ip3_, "%d", ip3);
  char ip4_[50];
  sprintf(ip4_, "%d", ip4);

  //printf("%s\n", ip1_);
  const char c[10] = ".";
  strcpy(ip, ip1_);
  strcat(ip, c);
  strcat(ip, ip2_);
  strcat(ip, c);
  strcat(ip, ip3_);
  strcat(ip, c);
  strcat(ip, ip4_);
  //printf("%s\n", ip);
  //ip_sum[i] = ip;
  strcat(ret->array[i], ip);
  const char end[10] = "\0";
  strcat(ret->array[i], end);
  //printf("%s\n", ret->array[i]);
  }
  //}
  //printf("%s\n", ip);
  return 0;
}


/*
int main(){
  struct data *arr =(struct data*) malloc(sizeof(struct data));
  //char ip[500][50];
  generate_ip(arr);
  int i=0;
  for(i; i<SUM; i++){
    printf("%s\n", arr->array[i]);
  }
  //printf("%s\n", ip);
  return 0;
  
}
*/



