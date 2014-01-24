#include <stdio.h>
#include <time.h>

#define MAX_BUF_SIZE 256
static const char *format = "%Y-%m-%d %H:%M:%S";

static void dump_time(time_t t)
{
    struct tm tm;
    char buf[MAX_BUF_SIZE] = {0};
    gmtime_r(&t,&tm);
    printf("dec : %ld\n", t);
    printf("hex : %x\n", t);
    printf("hexi: 0x%x\n", t);
    strftime(buf, MAX_BUF_SIZE, format, &tm);
    printf("str : %s\n", buf);
}

int main()
{
    
    time_t t = time(NULL);
    dump_time(t); 

    return 0;
}
