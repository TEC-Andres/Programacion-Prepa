#include <stdio.h>
#include <time.h>

void a() {
    clock_t start, end;
    volatile long long i; // 'volatile' prevents compiler optimizations

    start = clock();
    
    for (i = 0; i < 1000000000LL; i++) {
    }
    
    end = clock();

    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time taken: %f seconds\n", time_taken);
}