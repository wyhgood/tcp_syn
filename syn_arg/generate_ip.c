

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

/*
  本程序用来生产随机的ip地址。
  传入缓冲区的指针即可。
*/


int generate_ip(char *ip){
  //time_t t;
  //srand((unsigned)time(&t));
  //srand(8);
  int ip1 = rand()%256+1;
  int ip2 = rand()%256+1;
  int ip3 = rand()%256+1;
  int ip4 = rand()%256+1;
  
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
  return 0;
}

