#include <stdio.h>
#include <stdlib.h>

int main() {
    int escola, supermercado, lojinha;
    scanf("%d", &escola);
    scanf("%d", &supermercado);
    scanf("%d", &lojinha);
    int diffmin = abs(escola - supermercado) + abs(supermercado - lojinha) + abs(lojinha - escola);
    int diffmin2 = abs(escola - lojinha) + abs(lojinha - supermercado) + abs(supermercado - escola);

    if (diffmin > diffmin2) {
        printf("%d", diffmin2);
    } else {
        printf("%d", diffmin);
    }
    

    return 0;
}