#include "conta.h"
#include <iostream>
using namespace std;

void Conta::exibeDados()
{
	cout << "Titular: " << this->titular << endl;
	cout << "Numero: " << this->numero << endl;
}

double Conta::getSaldo(int senha)
{
	if(senha == this->senha)
	{
		return this->saldo;
	}
	else
	{
		cout << "Senha Inválida"<< endl;
		return -1;
	}
}

void Conta::setSaldo(double valor)
{
	this->saldo = valor;
}
void Conta::setSenha(int nova_senha)
{
	this->senha = nova_senha;
}