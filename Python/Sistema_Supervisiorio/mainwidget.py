from kivy.uix.boxlayout import BoxLayout
from popups import ModbusPopup, ScanPopup, DataGraphPopup
from pyModbusTCP.client import ModbusClient
from kivy.core.window import Window
from threading import Thread
from time import sleep
from datetime import datetime
import random 
#from timeseriesgraph import TimeSeriesGraph


class MainWidget(BoxLayout):
    """
    widget principal da aplicação
    """
    _updateThread = None
    _updateWidgets = True
    _tags = {}
    _max_points = 20
    
    
    def __init__(self, **kwargs):
        """
        Construtor do widget principal
        """
        super().__init__()
        self._scan_time = kwargs.get('scan_time')
        self._serverIP = kwargs.get('server_ip')
        self._serverPort = kwargs.get('server_port')        
        self._modbusPopup = ModbusPopup(self._serverIP,self._serverPort)
        self._scanPopup = ScanPopup(scantime = self._scan_time)
        self._modbusClient = ModbusClient(host = self._serverIP,port = self._serverPort)
        self._meas = {}
        self._meas['timestamp'] = None
        self._meas['values'] = {}
        for key,value in kwargs.get('modbus_addrs').items():
            if key == 'fornalha':
                plot_color =  (1,0,0,1) # RED
            else:
                plot_color = (random.random(),random.random(),random.random(),1)            
            self._tags[key] = {'addr':  value, 'color': plot_color} # criando um atributo _tags
            
        self._graph = DataGraphPopup(self._max_points, self._tags['fornalha']['color'])
            



    
    def stardDataRead(self, ip, port):
        """
        Método utilizado para a configuração do IP e Porta do servidor MODBUS e 
        inicializar uma thread para a leitura dos dados e atualização da interface 
        gráfica
        """
        self._serverIP = ip
        self._serverPort = port
        self._modbusClient.host = self._serverIP
        self._modbusClient.port = self._serverPort
        try:
            Window.set_system_cursor("wait")
            self._modbusClient.open()
            Window.set_system_cursor("arrow")
            if self._modbusClient.is_open:
                self._updateThread = Thread(target=self.updater)
                self._updateThread.start()
                self.ids.img_con.source = "imgs/conectado.png"
                self._modbusPopup.dismiss()
            else:
                self._modbusPopup.setInfo("Falha na conexão com o servidor")
        except Exception as e:
            print("Erro: ", e.args)
            
    def updater(self):
        """
        Método que invoca as rotinas de leitura dos dados, atualização da interface e 
        inserção dos dados no Banco de dados
        """
        try:
            while self._updateWidgets:
                # ler os dados MODBUS
                self.readData() 
                  
                # atualizar a interface
                self.updateGUI()
                
                # inserir os dados no banco de dados
                sleep(self._scan_time/1000)     
        except Exception as e:
            self._modbusClient.close()
            print("Erro no Update widgets: ", e.args)       
    def readData(self):
        """
        Método para a leitura dos dados por meio do protocolo MODBUS
        """
        
        self._meas['timestamp']= datetime.now() # retorna exatamente o horário corrente do S.O
        
        for key,value in self._tags.items():
            
            self._meas['values'][key]  = self._modbusClient.read_holding_registers(value['addr'],1)[0]
            

    def updateGUI(self):
        """
        Método para a atualização  da interface gráfica
        """
        #Atualização dos labels da tamperatura
        for key,value in self._tags.items():
            print(self.ids[key].text)
            self.ids[key].text = str(self._meas['values'][key]) + ' °C'  
        #Atualização do nivel do termometro
        self.ids.lb_temp.size = (self.ids.lb_temp.size[0], self._meas['values']['fornalha']/450 *self.ids.termometro.size[1])

        #Atualização do gráfico
        self._graph.ids.graph.updateGraph((self._meas['timestamp'],self._meas['values']['fornalha']),0) 

    def stopRefresh(self):
        self._updateWidgets = False