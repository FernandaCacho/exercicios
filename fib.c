//Programadora: Fernanda LC
//Data 23/06/2022
//Teste - exercício de Fibonacci

#include<stdio.h>


int main(void)
{
	int n, i, n1, n2, n3;
    n1 = 0;
    n2 = 1;
    n3 = 0;
	printf("Informe um número a ser verificado:\n");
	scanf("%d", &n);
	if(n==0 || n==1){
		printf("Número %d pertence a sequência\n", n);
	} else{
	    printf("%d", n1);
	    while(n3<n){
	        n3=n1+n2;
	        //Mostra a sequência de Fibonacci
			printf(" %d", n3);
			n1=n2;
			n2=n3;
	    }
	    printf("\n");
	    if(n3!=n){
	        printf("Número %d não pertence a sequência\n", n);
    	}else{
	        printf("Número %d pertence a sequência\n", n);
	    }
	}
		
	return 0;
}