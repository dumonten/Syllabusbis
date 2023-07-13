from main import *

class UIFunctions(MainWindow):

	def toggleMenu(self):
		height = self.ui.bottomToolSubContainer.height()
		standart = 80
		
		if height == 0:
			heightNew = standart
		else:
			heightNew = 0
			
		self.animation = QPropertyAnimation(self.ui.bottomToolSubContainer, b"maximumHeight")
		self.animation.setDuration(400)
		self.animation.setStartValue(height)
		self.animation.setEndValue(heightNew)
		self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
		self.animation.start()	
			
		
	def showMenuIfToggled(self, stackedWidget, page):
		stackedWidget.setCurrentWidget(page)
	
		height = self.ui.bottomToolSubContainer.height()
		standart = 80
		
		if height == 0:
			heightNew = standart
			self.animation = QPropertyAnimation(self.ui.bottomToolSubContainer, b"maximumHeight")
			self.animation.setDuration(400)
			self.animation.setStartValue(height)
			self.animation.setEndValue(heightNew)
			self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
			self.animation.start()		
			
