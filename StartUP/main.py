########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        # WORK WITH STACKED WIDGET
        self.ui.homeBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.homeToolPage))
        self.ui.insertBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.insertToolPage))
        self.ui.pageLayoutBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageLayoutPage))
        self.ui.toolsBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.toolsPage))
        self.ui.viewBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.viewPage))
        ########################################################################

        self.show()


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################
