#include <stdio.h>
#include <stdlib.h>
#include "Atv_1.h"

	
int main()
{

INICIO:

n_complex n1(0.0f, 0.0f);
n_complex n2(0.0f, 0.0f);


int opc;

while(opc != 0){

	printf("#==========================================================#\n\n");
	printf("Selecione a operacao desejada: \n\n 1 - Soma\n 2 - Subtracao\n 3 - Multiplicacao\n 4 - Divisao\n\n 9 - Digitar outros valores\n 0 - Cancelar e sair\n\n");
	printf("Operacao: ");
	scanf("%d", &opc);

	switch(opc){
		case 1: printf("\nA soma dos numeros complexos eh: %0.2f + %0.2fi\n\n", soma_real(n1, n2), soma_img(n1, n2));
				break;
		case 2: printf("\nA subtracao dos numeros complexos eh: %0.2f + %0.2fi\n\n", sub_real(n1, n2), sub_img(n1, n2));
				break;
		case 3: printf("\nA multiplicacao dos numeros complexos eh: %0.2f + %0.2fi\n\n", mult_real(n1, n2), mult_img(n1, n2));
				break;
		case 4: printf("\nA divisao dos numeros complexos eh: %0.2f + %0.2fi\n\n", div_real(n1, n2), div_img(n1, n2));
				break;
		case 9: printf("\n#==========================================================#\n\n");
				goto INICIO;
				break;
	}
}

return 0;
}
