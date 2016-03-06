from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(Window, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        home_page = HomeWidget(self)
	#home_page.button.clicked.connect(self.login)
        self.central_widget.addWidget(home_page)
	
        self.setWindowTitle('Home Meal Planning')    
        self.show() 
    def homepage(self):
        getmainpage = HomeWidget(self)
	self.central_widget.addWidget(getmainpage)
	self.central_widget.setCurrentWidget(getmainpage)
    def recipe(self):
        getrecipespage = Recipes(self)
	self.central_widget.addWidget(getrecipespage)
        self.central_widget.setCurrentWidget(getrecipespage)
    def makeMealPlans(self):
        makeplanpage = MealPlan(self)
	self.central_widget.addWidget(makeplanpage)
        self.central_widget.setCurrentWidget(makeplanpage)
	
    
class HomeWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HomeWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
	self.button = QtGui.QPushButton('Edit Recipes', self)
        self.button2 = QtGui.QPushButton('Make Meal Plan', self)
        self.button3 = QtGui.QPushButton('Update Inventory', self)
        self.button.clicked.connect(self.parent().recipe)
        self.button2.clicked.connect(self.parent().makeMealPlans)
        #self.button3.clicked.connect(self.updateInventory)
        #grid = QtGui.QGridLayout()
        #grid.setSpacing(10)

        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        self.setLayout(layout)
    
	
class Recipes(QtGui.QWidget):
    def __init__(self, parent = None):
        super(Recipes, self).__init__(parent)
	layout = QtGui.QHBoxLayout()
        self.addnewrecipebutton = QtGui.QPushButton('Add New Recipe', self)
        self.editrecipebutton = QtGui.QPushButton('Edit Existing Recipe', self)
        self.backbutton = QtGui.QPushButton('Back', self) 
	#Set the functionality of the buttons on the page
        self.backbutton.clicked.connect(self.parent().homepage)
	#Have to make the following two buttons do the correct thing
	self.addnewrecipebutton.clicked.connect(self.parent().homepage)
	self.editrecipebutton.clicked.connect(self.parent().homepage)
	
        layout.addWidget(self.addnewrecipebutton)
        layout.addWidget(self.editrecipebutton)
        layout.addWidget(self.backbutton)
        
        self.setLayout(layout)
    
class MealPlan(QtGui.QWidget):
    def __init__(self, parent = None):
        super(MealPlan, self).__init__(parent)
	layout = QtGui.QHBoxLayout()
        
	#Buttons for this page
	self.randomplanbutton = QtGui.QPushButton('Make Random Plan', self)
        self.choosemealsbutton = QtGui.QPushButton('Choose Meals', self)
        self.backbutton = QtGui.QPushButton('Back', self) 
	#Actions of each of the buttons
        self.backbutton.clicked.connect(self.parent().homepage)
	#Have to change the following two buttons to do the right actions
	self.randomplanbutton.clicked.connect(self.parent().homepage)
	
	self.choosemealsbutton.clicked.connect(self.parent().homepage)
	
	#Add each button to the overall layout of this particular page
        layout.addWidget(self.randomplanbutton)
        layout.addWidget(self.choosemealsbutton)
        layout.addWidget(self.backbutton)
        
        self.setLayout(layout)
	
class  UpdateInventory(QtGui.QWidget):
    def updateInventory(self):
        print 'We should update what we have!'

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())