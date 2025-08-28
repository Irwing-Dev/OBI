#include <stdio.h>

int main() {
    int n,m,p,g,c,capacidade=0;
    scanf("%d", &n);
    scanf("%d", &m);

    for (int i = 0; i < n; i++) {
        scanf("%d", &p);
        scanf("%d", &g);
        scanf("%d", &c);

        capacidade += p*4 + g*9 + c*4;
    }

    printf("%d", m - capacidade);

    return 0;
}