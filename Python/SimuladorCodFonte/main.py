from CLP import CLP

def main():
    print("================ Simulador da Planta Industrial =================")
    port = int(input("Digite a porta em que deseja iniciar o servidor MODBUS TCP do CLP: "))
    server = CLP(host='localhost',port=port)
    server.Connection()
    
if __name__ == '__main__':
    main()