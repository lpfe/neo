#모든 소스 파일을 대체할거임
SRCS = $(wildcard *.c)

#확장자없는?
PROGS = $(patsubst %.c, %, $(SRCS))
all : $(PROGS)
% : %.c
	gcc -o $@ $^
	
clean : $(PROGS)
	rm -rf $^