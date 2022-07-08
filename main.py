from IPweather.IPweather import IPweather # import everything from IPweather
import threading # import threading to keep the weather up to date
import time # import time to use less cpu in loops and stays in the API call limit
import os # import to get the current directory


ip          = IPweather.get_ip() # get the ip address of the user
current_dir = os.path.dirname(os.path.abspath(__file__)) # get the current directory
theme_path  = os.path.join(current_dir+"/theme/dark_red.xml")


# create function to keep the weather data up to date and Call the weather API
def update_weather(self, MainWindow):
    while True:
        weather = IPweather.get_weather(ip, True, True, True, True, True, True) # get the weather data

        self.values_display.setText(f"wind-speed: {weather[4]} ; Air-humidity: {weather[3]} ; Temperature: {weather[2]}") # set the text of the values_display
        self.ip_display.setText(f"  IP: {ip}") # set the text of the ip_display
        self.time_location_display.setText(weather[1] +" : "+ weather[5]) # set the text of the time_location_display
        self.current_weather_display.setText("Current-weather: "+ weather[0]) # set the text of the current_weather_display

        time.sleep(60) # wait 60 seconds before calling the API again



# open a simple gui to display the weather data
from PyQt5 import QtCore, QtWidgets # import all the libraries for the gui
from qt_material import apply_stylesheet # import the qt_material library

# create a class to create the gui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 100)
        MainWindow.setWindowTitle("""Weather App using "IPweather" """)
        self.ip_display = QtWidgets.QLabel(MainWindow)
        self.ip_display.setGeometry(QtCore.QRect(-5, 0, 500, 20))
        self.ip_display.setStyleSheet("background-color: rgb(108, 108, 108);")
        self.ip_display.setObjectName("ip_display")
        self.current_weather_display = QtWidgets.QLabel(MainWindow)
        self.current_weather_display.setGeometry(QtCore.QRect(0, 20, 471, 41))
        self.current_weather_display.setText("")
        self.current_weather_display.setAlignment(QtCore.Qt.AlignCenter)
        self.current_weather_display.setObjectName("current_weather_display")
        self.values_display = QtWidgets.QLabel(MainWindow)
        self.values_display.setGeometry(QtCore.QRect(0, 60, 471, 16))
        self.values_display.setAlignment(QtCore.Qt.AlignCenter)
        self.values_display.setObjectName("values_display")
        self.time_location_display = QtWidgets.QLabel(MainWindow)
        self.time_location_display.setGeometry(QtCore.QRect(0, 80, 471, 21))
        self.time_location_display.setText("")
        self.time_location_display.setAlignment(QtCore.Qt.AlignCenter)
        self.time_location_display.setObjectName("time_location_display")#
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # apply theme to the gui
        apply_stylesheet(MainWindow, theme_path)

        extra = {
            # Density Scale
            'density_scale': '+8',
        }
        apply_stylesheet(self.current_weather_display, theme_path, extra=extra)

        # create a thread to keep the weather data up to date
        threading.Thread(target=update_weather, args=(self, MainWindow)).start()
        
# create the main window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
