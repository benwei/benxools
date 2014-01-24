CFILES=time_disp.c
OBJS=$(CFILES:.c=.o)
BINFILE=time_disp

all: $(BINFILE)
	@echo "build done"

.c.o:
	$(CC) -c $< $(CFLAGS) $(INCS)

$(BINFILE): $(OBJS)
	$(CC)  -o $@ $^ $(LDFLAGS)

run: $(BINFILE)
	./$^

clean:
	rm *.o time_disp
