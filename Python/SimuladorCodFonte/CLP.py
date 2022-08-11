from pyModbusTCP.server import ModbusServer
from Tanque import Tanque
from time import sleep
from random import randrange
class CLP():
    """
    class CLP - Server - ModBus TCP

    attribute: tick : CLP cycle time


    """

    __tick = 0.1

    def __init__(self,host,port):
        """
        class constructor
        param: host: server IP address
        param: port : server port

        """
        self.__server = ModbusServer(host=host, port=port, no_block=True)
        self.__tank = Tanque(self.__tick)
        
        self.__server.data_bank.set_holding_registers(799,(self.__tank.motor.getOpFrequencia()/10,))  
        self.__server.data_bank.set_holding_registers(798,(self.__tank.motor.getTStart()*10,))       
        self.__server.data_bank.set_coils(801,(self.__tank.getSolenoide(0),))
        self.__server.data_bank.set_coils(802,(self.__tank.getSolenoide(1),))
        self.__server.data_bank.set_coils(803,(self.__tank.getSolenoide(2),))

    def Connection(self):
        """
        starts server
        listen client

        """
        self.__server.start()
        print('Simulador Online... Ctrl+C para parar')
        while True:
            try:
                self.DoService()
                sleep(self.__tick)
            except Exception as e:
                print("Error: ",e.args)
    
    def DoService(self):
        """
        serve client
        simulate tank
        set tank/motor parmas thru registers
        random noise added when reading data 

        """
        motorState = self.__server.data_bank.get_coils(800)[0]
        sol1 = self.__server.data_bank.get_coils(801)[0]
        sol2 = self.__server.data_bank.get_coils(802)[0]
        sol3 = self.__server.data_bank.get_coils(803)[0]
        frequency = self.__server.data_bank.get_holding_registers(799)[0]
        t_partida = self.__server.data_bank.get_holding_registers(798)[0]/10
        
        self.__tank.TankSimulation(frequency, t_partida,motorState,sol1,sol2,sol3)

        self.__server.data_bank.set_input_registers(801, (self.__tank.motor.getTensao()+ randrange(-3,4),))
        self.__server.data_bank.set_input_registers(802, (self.__tank.motor.getTorque(),))
        self.__server.data_bank.set_input_registers(800,(max(self.__tank.motor.getOpFrequencia()+ randrange(-3,4),0),))
        self.__server.data_bank.set_input_registers(803, (max(self.__tank.motor.getRotacao() + randrange(-3,4),0),))
        self.__server.data_bank.set_input_registers(804,(max(self.__tank.motor.getInPower()+ randrange(-3,4),0),))
        self.__server.data_bank.set_input_registers(805, (max(self.__tank.motor.getCorrente() + 10*randrange(-2,2),0),))
        self.__server.data_bank.set_input_registers(806,(max(self.__tank.motor.getTemperature()+ randrange(-2,3),0),))
        self.__server.data_bank.set_input_registers(807,(max(self.__tank.getVazao()+ 10*randrange(-1,1),0),))
        self.__server.data_bank.set_input_registers(808,(max(self.__tank.getNivel()+ 10*randrange(-3,4),0),))       
        self.__server.data_bank.set_coils(801,(self.__tank.getSolenoide(0),))
        self.__server.data_bank.set_coils(802,(self.__tank.getSolenoide(1),))
        self.__server.data_bank.set_coils(803,(self.__tank.getSolenoide(2),))
        high_l = self.__tank.getHighLevel()
        low_level = self.__tank.getLowLevel()
        self.__server.data_bank.set_discrete_inputs(809,(high_l,))
        self.__server.data_bank.set_discrete_inputs(810,(low_level,))
        if high_l:
            self.__server.data_bank.set_coils(800,(False,))
     