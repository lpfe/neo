OBJF = test1.o test2.o test3.o
test : $(OBJF)
	gcc -o $@ $^
.c.o :
	gcc -c $<
# test1.o : test1.c a.h b.h
# 	gcc -c $<
# test2.o : test2.c a.h b.h
# 	gcc -c $*.c
# test3.o : test3.c b.h c.h
# 	gcc -c $<
clean:test $(OBJF)
	rm -rf $^


#명시적이지만 ~