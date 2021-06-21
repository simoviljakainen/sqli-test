#include <stdio.h>

int main(void){
  char buffer[25];

  printf("Give me your name: ");
  gets(buffer);

  printf("Welcome %s\n", buffer);

  return 0;
}