/*
 * babyre.c
 * Copyright (C) 2019 vam <jpwan21@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
#include "babyre.h"
#define N 0x100

const char *flag = "./flag.txt";
const char *essay= "If you cannot read all your books...\
fondle them---peer into them, let them fall open where they will,\
 read from the first sentence that arrests the eye, set them back\
 on the shelves with your own hands, arrange them on your own plan\
 so that you at least know where they are. Let them be your friends;\
let them, at any rate, be your acquaintances.";
const char *corpus = "./corpus.txt";

int check(char* result){
  if(strcmp(result, essay)==0)
     return 1;
  return 0;
}

char *decode(char* cipher){
	int size = strlen(cipher);
	char*plain = malloc(size);
	memset(plain, 0, size);
	
	char *dest = malloc(N);
	memset(dest, 0, N);

  int p=0;
  int iter=0;
	for(int i=1; i<=size; i++){
    //从code表里寻找, 找到匹配后，输出相应的name;
		strncpy(dest, cipher+p, i-p);
		for(int j=0; j<N; j++){
			if(strcmp(code[j], dest)==0){
				plain[iter++] = name[j];
				p=i;
				break;
			}
		}
		memset(dest,0,N);
	}
	plain[iter]='\x00';
  free(dest);
  return plain;
}

int main() {
  init();
  int i, j;
  struct stat stat_buf;
  __xstat(1,corpus, &stat_buf);
  ssize_t size = stat_buf.st_size;
  
  int fd =  open(corpus, 4); //读取文件
  char *file_content = malloc(size+0x20);
  ssize_t char_n = read(fd, (void*)file_content, size);
  close(fd);
  x = timesOfChars(file_content, size); //统计字符
  code = malloc(N * sizeof(char*)); //指向每一个符号的编码
  name = malloc(N);
  dict = malloc(N);

  for (i = 0; i < N; i++){
  	  name[i] = i;
  	  dict[i] = i;
      code[i] = malloc(N * sizeof(char)); //最长的码长也为n
      memset(code[i], '\x00', N);
  }

  // 逆序的插入排序; 
  for (i = 0; i < N-1; i++) {
    int v;
    int w;
    for (j = i+1, v = x[j], w=name[j]; v > x[j-1] && j >= 1; j--) {
      name[j] = name[j-1];
      x[j] = x[j-1];
    }
    name[j]=w;
    x[j]=v;
    // printf("x[%d]= %d", i, x[i]);
  }
  for(int i=0; i<N; i++)
  	  dict[name[i]] = i;

  fano(0, N-1);  //费诺编码

  char *cipher = malloc(0x5000);
  memset(cipher,0, 0x5000);
  int input_num = read(0, cipher, 0x5000);

  char *plain = decode(cipher);
  if(check(plain)){
	   int fd_flag = open(flag, 4);
	   char *s_flag = malloc(0x80);
	   memset(s_flag,0,0x80);
	   read(fd_flag,s_flag,0x50);
	   puts(s_flag);
  }
  free(plain);
  free(cipher);
  free(file_content);
  free(name);
  free(dict);
  free(x);
  for (i = 0; i < N; i++)
  	free(code[i]);
  free(code);
  return 0;
}