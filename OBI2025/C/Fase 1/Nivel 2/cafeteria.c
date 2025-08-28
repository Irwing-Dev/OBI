#include <stdio.h>

int main() {
    int A, B, C, D;
    
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    scanf("%d", &D);
    
    int possivel = 0;
    
    for (int i = 0; i <= C / D; i++) {
        int volume_cafe = i * D;
        int volume_leite = C - volume_cafe;
        
        if (volume_leite >= A && volume_leite <= B) {
            possivel = 1;
            break;
        }
    }
    
    if (possivel) {
        printf("S\n");
    } else {
        printf("N\n");
    }

    return 0;
}