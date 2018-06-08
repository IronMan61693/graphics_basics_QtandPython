from PyQt5.QtWidgets import QMainWindow
from central_widget import CentralWidget

class MainWindow(QMainWindow):
	"""
	We are modifying some of the attributes of a QMainWindow class
	Create an instance of CentralWidget class
	
	Variables:
		centralWidget <CentralWidget>

	Methods:
		Inherited from QMainWindow:
			setCentralWidget 
			setWindowTitle
	"""
	def __init__(self):
		super().__init__()
		self.centralWidget = CentralWidget()
		self.setCentralWidget(self.centralWidget)
		self.setWindowTitle("Wubba Lubba Dub Dub")
