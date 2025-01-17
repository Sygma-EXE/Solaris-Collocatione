import sys
import subprocess
from datetime import date
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtGui import QPixmap, QIcon

from map import *
from maj.majsys import *

#last update date system
datetoday =str(date.today())    #catch today date
datenow = date(int(datetoday[:4]),int(datetoday[5:7]),int(datetoday[8:10])) #transform it to be usable by the lib
datecatchLU= datecatch()    #cacth saved last update date
lastupdate = date(datecatchLU[0],datecatchLU[1],datecatchLU[2]) #transform it to be usable by the lib
dayupdate = (datenow - lastupdate).days #count how many days since last update


#the log system still in dev

#
class SimpleGUI(QWidget):
    def __init__(self):
        super().__init__()
        
        #set app name
        self.setWindowTitle("Solaris Collocatione")

        #set app icon
        

        #set window size
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        #image
        self.image_label = QLabel(self)
        self.pixmap = QPixmap("SC-logo.png")
        self.image_label.setPixmap(self.pixmap)
        layout.addWidget(self.image_label)

        #day(s) since last update
        self.label = QLabel("Last files update: "+ str(dayupdate)+" day(s) ago")
        layout.addWidget(self.label)

        #button for the html map
        self.map_button = QPushButton("Generate and open map", self)
        self.map_button.clicked.connect(self.openmap)
        layout.addWidget(self.map_button)

        #button for the html map with saved data
        #self.logmap_button = QPushButton("Open log map", self)
        #self.logmap_button.clicked.connect(self.openlogmap)
        #layout.addWidget(self.logmap_button)

        #button ti update data
        self.update_button = QPushButton("Update file", self)
        self.update_button.clicked.connect(self.Update)
        layout.addWidget(self.update_button)

        #set the layout of the gui
        self.setLayout(layout)

    def openmap(self):  #for the html map button
        MapGeneration(0)    #generate the map
        subprocess.run(["start", "map.html"], shell=True, check=True)   #open the map file

#    def openlogmap(self):
#        MapGeneration(1)
#        subprocess.run(["start", "map.html"], shell=True, check=True)

    def show_popup(self,title,text):    #popup :)
            msg = QMessageBox() #set popup object
            msg.setIcon(QMessageBox.Information)    #set the icon
            msg.setWindowTitle(title)   #set the popup name
            msg.setText(text)   #set the text op the popup
            msg.setStandardButtons(QMessageBox.Ok)  #set a button for the popup
            msg.exec()  #execute the button
    
    def Update(self):   #update button
        result = DoMaj()    #do the update

        if result == 0: #if no maj need (code 0)
            self.show_popup("SC Update System","No update Needed")
        
        elif result == 1: #if maj done (code 1)
            self.show_popup("SC Update System","Update Done")
        
        elif result == 3: #if error (code 3)
            self.show_popup("SC Update System","Error")

#start the GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleGUI()
    icon = QIcon("Sc-logo.ico")
    app.setWindowIcon(icon)
    window.show()
    sys.exit(app.exec())
