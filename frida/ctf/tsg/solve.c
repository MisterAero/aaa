#include <stdio.h>
#include <dlfcn.h>

int main()
{
    // void *h = dlopen("./beginners_rev", RTLD_LAZY);
    // void *h = dlopen("./beginners_rev", RTLD_NOW);
    void *h = dlopen("./PATCHED", RTLD_LAZY);
    if (!h) puts("FUCK");
    // RTLD_NOW
    printf("%lld\n",*(long long int*)h);
    // int (*is_correct)(int, int) = dlsym(h, "is_correct");
    int (*is_correct)(int, int) = (void *)((*(long*)h) + 0x1280);
    puts("sadsa");
    char flag[0x21] = {0};
    
    for (int i=0; i<0x20; i++)
        for (int j=0; j<256; j++)
            if (is_correct(j, i)){
                
                flag[i] = j;
                }
    puts(flag);
}