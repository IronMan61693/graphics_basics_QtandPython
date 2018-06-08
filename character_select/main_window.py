from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap, QPalette, QBrush

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
		self.centralWidget.setObjectName("centralWidget")
		self.centralWidget.setStyleSheet("#centralWidget {background-color: blue ; color : #f8f8f8}")

		self.setCentralWidget(self.centralWidget)
		self.setWindowTitle("Character Select")




		"""
		Palette attempt
		# Set the background as a Pixmap /home/dopo2697/Documents/py/graphics_Basics/character_select/resources/burning_guy_background.jpeg
		self.backgroundPixmap = QPixmap("burning_guy_background.jpeg")

		# Create the background Palette and set its background to the Pixmap
		self.backgroundPalette = QPalette()

		self.backgroundBrush = QBrush()
		self.backgroundBrush.setTexture(self.backgroundPixmap)

		self.backgroundPalette.setBrush(QPalette.Background, self.backgroundBrush)

		# change the Palette for the widget
		self.centralWidget.setPalette(self.backgroundPalette)

		"""

		
