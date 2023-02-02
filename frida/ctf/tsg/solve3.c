#define _GNU_SOURCE
#include <stdio.h>
#include <link.h>
#include <string.h>
#include <elf.h>

#define FOO_VADDR 0x1280

typedef int(*func_t)();

int callback(struct dl_phdr_info *info, size_t size, void *data)
{
    if (!(strstr(info->dlpi_name, "PATCHED.so")))
        return 0;
    Elf64_Addr addr = info->dlpi_addr + FOO_VADDR;
    func_t f = (func_t)addr;
    // int res = f();
    
    char flag[0x21] = {};
    for (int i=0; i<0x20; i++)
        for (int j=0; j<256; j++)
            if (f(j, i))
                flag[i] = j;
    puts(flag);
    return 0;
}

int main()
{
    void *handle = dlopen("./PATCHED.so", RTLD_LAZY);
    if (!handle) {
        puts("failed to load");
        return 1;
    }
    dl_iterate_phdr(&callback, NULL);
    dlclose(handle);
    return 0;
}