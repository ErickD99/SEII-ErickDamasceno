#ifndef ATIVIDADE_1
#define ATIVIDADE_1
#include <math.h>

class n_complex
{
	float real, img; //Parte real e imaginária do número complexo
public:
	n_complex(float, float);
	float p_real(){return real;};
	float p_img(){return img;};
};

n_complex::n_complex(float a, float b){

	printf("Digite a parte real do numero complexo: ");
	scanf("%f", &a);

	printf("Digite a parte imaginaria do numero complexo: ");
	scanf("%f", &b);

	printf("\nNumero complexo: %0.2f + %0.2fi \n", a, b);

	float modulo = sqrt(a * a + b * b);
	float arg = atan(b/a);

	printf("Forma polar: %0.2f(cos(%0.2f) + i.sen(%0.2f)) \n\n", modulo, arg, arg);

	real = a;
	img = b;
}


//Soma:

float soma_real(n_complex n1, n_complex n2){

	return n1.p_real() + n2.p_real();
}

float soma_img(n_complex n1, n_complex n2){

	return n1.p_img() + n2.p_img();
}

//Subtração:

float sub_real(n_complex n1, n_complex n2){

	return n1.p_real() - n2.p_real();
}

float sub_img(n_complex n1, n_complex n2){

	return n1.p_img() - n2.p_img();
}

//Multiplicação:

float mult_real(n_complex n1, n_complex n2){

	return n1.p_real() * n2.p_real() - n1.p_img() * n2.p_img();
}

float mult_img(n_complex n1, n_complex n2){

	return n1.p_real() * n2.p_img() + n1.p_img() * n2.p_real();
}

//Divisão:

float div_real(n_complex n1, n_complex n2){

	return (n1.p_real() * n2.p_real() + n1.p_img() * n2.p_img()) / (n2.p_real() * n2.p_real() + n2.p_img() * n2.p_img());
}

float div_img(n_complex n1, n_complex n2){

	return (n1.p_img() * n2.p_real() - n1.p_real() * n2.p_img()) / (n2.p_real() * n2.p_real() + n2.p_img() * n2.p_img());
}


#endif
