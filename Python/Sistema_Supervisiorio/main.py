from kivy.app import App ## clase base para criação de aplicativos
from mainwidget import MainWidget
from kivy.lang import Builder

class MainApp(App):
    """
    Classe com aplicativo
    """
    def build(self):
        """
        Método que gera o aplicativo com o widget principal
        """
        self._widget = MainWidget(scan_time=1000, server_ip = '127.0.0.1', server_port = 502)
        return self._widget
    
if __name__ == "__main__":
    Builder.load_string(open("mainwidget.kv", encoding = "utf-8").read(), rulesonly = True)
    Builder.load_string(open("popups.kv", encoding = "utf-8").read(), rulesonly = True)
    
    MainApp().run()    
