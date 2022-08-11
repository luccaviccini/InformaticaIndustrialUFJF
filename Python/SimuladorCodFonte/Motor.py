import math

class Motor:
    """
    class motor
    """
    def __init__(self, **params):
        """
        class constructor
        param : **params : dictionary passed from tank class
        """     
        self.__tensao = params["tensao"]
        self.__eff = params["eff"]
        self.__polo = params["polo"]
        self.__costheta = params["costheta"]
        self.__horsepower = params["horsepower"]
        self. __slipNom = params["slipNom"]
        self.__frequencia = params["frequencia"]
        self.__load = params["load"]
        self.__opFrequencia = params["opFrequencia"]
        self.__tempAmb = params["TempAmbiente"]
        self.__temp_level = 0
        self.__oldTemp = self.__tempAmb
        self.__state = params["state"]
        self.__elapsedTime = 0
        self.__tal = params["tal"]
        self.__tstart = params["tstart"]
        self.__f = 0
        
        self.__efInversor = 0.85
        self.__torqueNom = 0
        self.__torqueVazio = 0
        self.__wSincronaNom = int((120*self.__frequencia)/self.__polo)
        self.__rotNom = (1-self.__slipNom)*self.__wSincronaNom

    """
    return data to registers
    """
    def getWsincrona(self):
        return self.__wSincronaNom
    def getRotNom(self):
        return self.__rotNom
    def getTensao(self):
        return int(self.__tensao)
    def getLoad(self):
        return int(self.__load*10)
    def getFrequencia(self):
        return int(self.__frequencia*10)
    def getOpFrequencia(self):
        return int(self.__opFrequencia*10)
    def getOpWsincrona(self):
        return self.__wSincronaOperacao
    def getTorque(self):
        return int(self.__torque*100)
    def getRotacao(self):
        return int(self.__rotacao)    
    def getOutPower(self):
        return int(self.__outpower)
    def getInPower(self):
        return int(self.__inpower*10)
    def getCorrente(self):
        return int(self.__corrente*100)
    def getTemperature(self):
        return int(self.__temp*10)
    def getState(self):
        return self.__state
    def getTStart(self):
        return self.__tstart

    """
    motor params calc
    """
    def setTStart(self, tstart):
        self.__tstart = tstart
    def setState(self, state):
        self.__state = state

    def TorqueNom(self):
        if not self.__rotNom == 0:
            self.__torqueNom = self.__horsepower*746/self.__rotNom
        else:
            self.__torqueNom = 0

    def setOpFrequencia(self, frequencia):
        self.__opFrequencia = frequencia

    def wSincronaOperacao(self):
        self.__wSincronaOperacao = 120*self.__opFrequencia/self.__polo

    def TorqueVazio(self):
        if not self.__wSincronaOperacao == 0:
            self.__torqueVazio = self.__horsepower*746/(0.99*self.__wSincronaOperacao)
        else:
            self.__torqueVazio = 0

    def Torque(self):
        if self.__load == 0:
            self.__torque = self.__torqueVazio
        else:
            self.__torque = self.__load*self.__torqueNom

    def Rotacao(self):
        if  not self.__wSincronaOperacao == 0:
            self.__rotacao = -(self.__wSincronaOperacao/self.__torqueNom)*\
                                                    (self.__slipNom*self.__torque-self.__torqueNom)
        else:
            self.__rotacao = 0

    def OutPower(self):
        self.__outpower = self.__torque*self.__rotacao

    def InPower(self):
        self.__inpower = (self.__outpower/(self.__eff*self.__efInversor))

    def CalculaCorrente(self):
            self.__corrente = self.__inpower/(math.sqrt(3)*self.__tensao*self.__costheta)

    def Temperature(self,tick):
        
        if (40*self.__outpower/(self.__rotNom*self.__torque)) > self.__temp_level: 
            self.__oldTemp = self.__temp
            self.__elapsedTime = 0

        elif (40*self.__outpower/(self.__rotNom*self.__torque)) < self.__temp_level:
            self.__oldTemp = self.__temp
            self.__elapsedTime = 0
    
        self.__temp_level = 40*self.__outpower/(self.__rotNom*self.__torque)

        self.__elapsedTime += tick
        self.__temp = (self.__tempAmb+ self.__temp_level) + (self.__oldTemp-(self.__tempAmb+ self.__temp_level))*(math.exp(-self.__elapsedTime/self.__tal))

    def partida(self, estado, frequencia_desejada,tick):

        if estado is False:
           self.setState(False)
           return 0

        #Algoritmo de partida do motor
        if self.getState():
            self.__f = frequencia_desejada
        else:
            if self.__f < frequencia_desejada and estado is True:
                self.__f += frequencia_desejada/(self.__tstart
    /tick)
            elif (self.__f >= frequencia_desejada) and (estado is True):
                self.setState(True)
        return self.__f