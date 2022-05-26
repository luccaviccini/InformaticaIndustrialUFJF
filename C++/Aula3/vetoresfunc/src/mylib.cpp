#include "mylib.h"

void elevaQuadradoVetor(int vet[], int tamVet) // função void... nào retorna nada.
{
	for (int i = 0; i < tamVet ;i++) //Multiplica cada espaço do vetor por ele mesmo
	{
		vet[i] *= vet[i];
	}	
}

void elevaQuadradoElemento(int valor)
{
	std::cout << "Valor do elemento na funcao elevaQuadradoElemento: " << (valor *= valor) << std::endl;
}
