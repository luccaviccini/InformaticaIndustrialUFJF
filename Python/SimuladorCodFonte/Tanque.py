from Motor import Motor
import math
import random


class Tanque:
    """
    class tank

    """

    def __init__(self, tick, iState=False, maxLevel=1000, lowLevel=50, highLevel=950, rst_time=10):
        """
        class constructor
        dictionary to initialize motor params

        """

        self.__tick = tick
        self.__level = 0.0
        self.__solenoides = [iState,iState,iState]
        # Fatores randômicos vazão de saída
        self._rand_factor = [random.random(),random.random(),random.random()]
        self._rst_time = rst_time
        self.__maxLevel = maxLevel
        self.__lowLevel = lowLevel
        self.__highLevel = highLevel
        self.__elapsedTime = 0
        self.__motorDic = {"state": False, "tensao": 220, "eff": 0.8, "polo": 4, "costheta": 0.8, "horsepower": 3, "slipNom": 0.05,
            "load": 0.5, "frequencia": 60, "opFrequencia": 60, "TempAmbiente": 24, "tal": 100, "tstart": 3}
        self.motor = Motor(**self.__motorDic)

    """
    return data to registers
    """

    def getVazao(self):
        return int(self.__vin*100)

    def getNivel(self):
        return int(self.__level*10)

    def getLowLevel(self):
        return self.__level >= self.__lowLevel

    def getHighLevel(self):
        return self.__level >= self.__highLevel

    def getSolenoide(self,sol):
        return self.__solenoides[sol]

    def getTick(self):
        return self.__tick

    def CalculaVazao(self):
            self.__vin = 10*(self.motor.getRotacao() /
                             (self.motor.getWsincrona()))

    def setSolenoide(self, sol, state):
        self.__solenoides[sol] = state

        if self.__vin == 0 and self.__level == 0:
            self.__solenoides[sol] = False

    def CalculaNivel(self):

        if self.__solenoides[0]:
            v1 = 5*self.__level/self.__maxLevel*self._rand_factor[0]
        else:
            v1 = 0

        if self.__solenoides[1]:
            v2 = 5*self.__level/self.__maxLevel*self._rand_factor[1]
        else:
            v2 = 0
        
        if self.__solenoides[2]:
            v3 = 5*self.__level/self.__maxLevel*self._rand_factor[2]
        else:
            v3 = 0
        
        vout = v1+v2+v3

        self.__level += (self.__vin - vout)*self.__tick   
        # print(f'Nivel: {self.__level}  vout: {vout}') 

    def muda_rnd_factor(self):
        if self.__elapsedTime > self._rst_time:
            self._rand_factor[0] = random.random()
            self._rand_factor[1] = random.random()
            self._rand_factor[2] = random.random()
            self.__elapsedTime = 0


    def TankSimulation(self, frequencia, t_partida,motorState, sol1,sol2,sol3):

        """
        set motor/tank params upon user frequency and valve state input 
        """
        self.motor.setTStart(t_partida)
        freq = self.motor.partida(motorState, frequencia, self.__tick)
        self.motor.TorqueNom()
        self.motor.setOpFrequencia(freq)
        self.motor.wSincronaOperacao()
        self.motor.TorqueVazio()
        self.motor.Torque()
        self.motor.Rotacao()
        self.motor.OutPower()
        self.motor.InPower()
        self.motor.CalculaCorrente()
        self.motor.Temperature(self.__tick)

        self.CalculaVazao()
        self.setSolenoide(0,sol1)
        self.setSolenoide(1,sol2)
        self.setSolenoide(2,sol3)
        self.CalculaNivel()
        self.getHighLevel()
        self.getLowLevel()   
        self.__elapsedTime += self.__tick 