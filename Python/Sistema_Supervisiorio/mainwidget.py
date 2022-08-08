from kivy.uix.boxlayout import BoxLayout
from popups import ModbusPopup, ScanPopup

class MainWidget(BoxLayout):
    """
    widget principal da aplicação
    """
    def __init__(self, **kwargs):
        """
        Construtor do widget principal
        """
        super().__init__()
        self._scan_time = kwargs.get('scan_time')
        self._modbusPopup = ModbusPopup()
        self._scanPopup = ScanPopup(scantime = self._scan_time)
    pass
