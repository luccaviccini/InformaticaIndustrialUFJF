class Conta():
    """
    Classe Conta Conta
    """
    _saldo = 0.0 #atributo protegido 
    
    def __init__(self,numero, titular, senha, saldoi=0.0):
        """
        Classe Conta Conta
        :param numero:numero da conta
        :param titular: nome do titular
        :param senha: senha da conta
        :param saldoi:saldo inicial da conta (padrão = 0.0)
        
        """
    
        self._numero = numero   
        self.titular = titular
        self.__senha = senha
        self.saldoi = saldoi
        
    def getSaldo(self, senha):
        """
        Método para obtenção do saldo mediande valicadao da senha passada como argumento
        :param senha: senha da conta
        :return: saldo da conta
        """
        if self.__senha == senha:
            return self.saldo

    def setSaldo(self, valor):
        """
        Método para configuração do saldo

        Args:
        :param valor: valor desejado para o saldo
        """
        self.saldo = valor
    
    def setSenha(self, novaSenha):
        """
        Método para configuração de nova senha para a conta

        Args:
        :param novaSenha: nova senha desejada
        """
        self.__senha = novaSenha
    
    def saque(self, senha, valor):
        """
        Método para realizção de um saque

        Args:
        :param senha: senha da conta
        :param valor: valor da
        """
        if senha == self.__senha:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f"Saque no valor de R$ {valor} realizado com sucesso!\n")
            else:
                print("Saldo Insuficiente")
        else:
            print(f"Senha Inválida")

    def deposito(self, valor):
        """Método para realizção de um deposito
        

        Args:
            :param valor: valor to deposito
        """