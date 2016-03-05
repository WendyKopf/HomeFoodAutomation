from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Edit Recipes', self)
        self.button2 = QtGui.QPushButton('Make Meal Plan', self)
        self.button3 = QtGui.QPushButton('Update Inventory', self)
        self.button.clicked.connect(self.editRecipes)
        self.button2.clicked.connect(self.makeMealPlans)
        self.button3.clicked.connect(self.updateInventory)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.button, 0,0)
        grid.addWidget(self.button2, 1, 1)
        grid.addWidget(self.button3, 2, 2)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Home Meal Planning')    
        self.show() 

    def editRecipes(self):
        print 'I want this to work!'
        QtGui.QWidget.__init__(self)
        self.addnewrecipebutton = QtGui.QPushButton('Add New Recipe', self)
        self.editrecipebutton = QtGui.QPushButton('Edit Existing Recipe', self)
        self.backbutton = QtGui.QPushButton('Back', self)
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.addnewrecipebutton, 0,1)
        grid.addWidget(self.editrecipebutton, 1,1)
        grid.addWidget(self.backbutton, 2,1)
        
        self.setLayout(grid)
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('Home Meal Planning')
        self.show()
    def makeMealPlans(self):
        print 'I love to make a meal plan!'
    def updateInventory(self):
        print 'We should update what we have!'

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.resize(640, 480)
    window.show()
    sys.exit(app.exec_())