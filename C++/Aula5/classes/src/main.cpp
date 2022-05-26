#include <conta.h>

using namespace std;

int main()
{
	Conta c1;//Cria o objeto c1 que pertence a classe conta
	c1.numero = 2345;//Altera o numero do objeto c1
	c1.titular = "Joao";
	c1.setSenha(1234);
	c1.setSaldo(200);
	c1.exibeDados();//Usa o metodo exibeDados() da classe Conta para o objeto c1
	cout << "Saldo em conta: "<< c1.getSaldo(1234)<< endl;
	return 0;

}
