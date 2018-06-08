from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt5.QtCore import Qt, QDate, QTime, QDateTime


"""
QWidget is the base class for the central widget
QHBoxLayout and QVBoxLayout are layout classes, H puts in widgets left to right and V Top to bottom
QLabel allows for graphical text boxes
QPushButton class for pushable buttons
QSizePolicy class to dynamically resize, used in Label
QDate class which gives calendar dates
QTime class that allows clock time
QDateTime a class of both QDate and QTime
"""

class CentralWidget(QWidget):
	"""
	Making a class from the QWidget class, specify variables and behavior 

	Variables:
		mainLayout <QVBoxLayout>
		buttonLayout <QHBoxLayout>
		theLabel <QLabel>
		aButton <QPushButton>
		bButton <QPushButton>
		cButton <QPushButton>

	Methods:
		Inherited from QWidgets:
			addWidget
			addLayout
	"""
	def __init__(self):
		super().__init__()


		######################################################################################################
		# Creating Layouts
		######################################################################################################

		# Sets as child to CentralWidget
		self.mainLayout = QVBoxLayout(self)

		self.buttonLayout = QHBoxLayout()

		self.dateAndTimeLayout = QVBoxLayout()


		######################################################################################################
		# Creating widgets to go in layouts
		######################################################################################################
		self.theLabel = QLabel("Git gud")

		# Formats date strangely
		self.now = QDate.currentDate()
		# Makes Date look clean in two different ways
		self.dateLabel = QLabel(self.now.toString(Qt.ISODate) + " " + self.now.toString(Qt.DefaultLocaleLongDate))

		# examples of time and date time
		self.dateTime = QDateTime.currentDateTime()
		self.dateTimeLabel = QLabel(self.dateTime.toString())

		self.time = QTime.currentTime()
		self.timeLabel = QLabel(self.time.toString(Qt.DefaultLocaleLongDate))

		self.aButton = QPushButton("A")
		self.bButton = QPushButton("B")
		self.cButton = QPushButton("C")


		######################################################################################################
		# Changing the properties of the widgets
		######################################################################################################

		# Set object names to use setStyleSheet to apply to only one thing
		self.cButton.setObjectName("cButtonName")

		# Changes the size of the 'box' for the label
		self.theLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

		# Places the label in the center of the space for it
		self.theLabel.setAlignment(Qt.AlignCenter)

		# Changes the color of the space filled by the label and the font size
		self.theLabel.setStyleSheet("background-color: green; font: 50pt Arial; color: black")

		# Makes aButton appear with blue font and red background
		self.aButton.setStyleSheet("color: blue; background-color: red")

		# Set a tooltip mouse over
		self.bButton.setToolTip("If you click me I will demonstrate the scale effect of setStyleSheet")
		self.cButton.setToolTip("Click me to get a print response and turn me purple and green")

		# Connects on_click method with clicked state of pushButton
		self.bButton.clicked.connect(self.big_click)
		self.cButton.clicked.connect(self.on_click)


		######################################################################################################
		# re-Parenting mainLayout
		######################################################################################################

		# The order widgets are added change the order they appear in the layout
		# Since main is QV order determines top to bottom
		self.mainLayout.addLayout(self.dateAndTimeLayout)

		self.mainLayout.addWidget(self.theLabel)

		self.mainLayout.addLayout(self.buttonLayout)

		self.mainLayout.addWidget(self.dateLabel)

		self.mainLayout.addWidget(self.cButton)

		######################################################################################################
		# re-Parenting buttonLayout
		######################################################################################################

		# The order widgets are added change the order they appear in the layout
		# Since button is QH order determines left to right
		self.buttonLayout.addWidget(self.aButton)
		self.buttonLayout.addWidget(self.bButton)

		self.dateAndTimeLayout.addWidget(self.dateTimeLabel)
		self.dateAndTimeLayout.addWidget(self.timeLabel)



	def on_click(self):
		"""
		Define click functionality

		Input: None

		Output:
			print statement
		"""
		print("Look at you, you clicked a button")
		self.setStyleSheet("QPushButton#cButtonName {color: green; background-color: purple}")

	def big_click(self):
		"""
		Demonstrates the cascade effect of setStyleSheet if not careful

		Input: None

		Output:
			Changes buttons
		"""
		self.setStyleSheet("font: 80pt")
