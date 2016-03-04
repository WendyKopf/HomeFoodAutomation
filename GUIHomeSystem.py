#Want a basic GUI for the home project. 

import Tkinter
import ttk

class APP(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master, height = 300, width = 300)
        self.grid(row = 0, column = 2)        

root = Tkinter.Tk()
root.geometry('{}x{}'.format(550, 350))
app = APP(master=root)
app.master.title("Healthy Planner")


def editRecipes():
    root2 = Tkinter.Tk()
    root2.geometry('300x350')
    app = APP(master = root2)
    app.master.title("Edit Recipes")
    close = Tkinter.Button(app.master, text = "Home", width = 15, command = root2.destroy)
    submit = Tkinter.Button(app.master, text = "Edit Recipes", width = 15, command = updateRecipeDatabase)
    close.grid(row = 1, column = 2)
    submit.grid(row = 0, column = 2)
    
def makeMealPlan():
    root3 = Tkinter.Tk()
    root3.geometry('500x350')
    app = APP(master = root3)
    app.master.title("Make Meal Plan")
    close2 = Tkinter.Button(app.master, text = "Home", width = 15, command = root3.destroy)
    select = Tkinter.Button(app.master, text = "Select Recipes", width = 15, command = selectRecipes)
    auto_generate = Tkinter.Button(app.master, text = "Generate Random Plan", width = 15, command = selectRandom)
    close2.grid(row = 1, column = 1)
    select.grid(row = 0, column = 2)
    auto_generate.grid(row = 0, column = 0)
    
def updateInventory():
    root4 = Tkinter.Tk()
    root4.geometry('500x350')
    app = APP(master = root4)
    app.master.title("Update Inventory")
    close3 = Tkinter.Button(app.master, text = "Home", width = 15, command = root4.destroy)
    update_existing = Tkinter.Button(app.master, text = "Update Existing", width = 15,  command = updateExistingItem)
    add_new = Tkinter.Button(app.master, text = "Add New Item", width = 15, command = addNewItem)
    close3.grid(row = 1, column = 1)
    update_existing.grid(row = 0, column = 2)
    add_new.grid(row = 0, column = 0)

def updateRecipeDatabase():
    root = Tkinter.Tk()
    app = APP(master= root)
    app.master.title("Update Recipe Database")
    back_to_previous = Tkinter.Button(app.master, text = "Back", width = 15, command = root.destroy) 
    close = Tkinter.Button(app.master, text = "Home", width = 15, command = root.destroy)
    update_existing = Tkinter.Button(app.master, text = "Update Existing Recipe", width = 15, command = updateExistingRecipe)
    add_new_recipe = Tkinter.Button(app.master, text = "Add New Recipe", width = 15, command = addNewRecipeDatabase)
    back_to_previous.grid(row = 0, column =1)
    close.grid(row = 3, column =1)
    update_existing.grid(row = 2 , column = 1)
    add_new_recipe.grid(row = 1, column =1)

def updateExistingRecipe():
    root = Tkinter.Tk()
    app = APP(master = root)
    app.master.title("Update Existing Recipe")
    back_to_previous = Tkinter.Button(app.master, text = "Back", width = 15, command = root.destroy)
    close = Tkinter.Button(app.master, text = "Home", width = 15, command = destroyBothParentChild)
    submit = Tkinter.Button(app.master, text = "Submit", width = 15, command = updateDatabase)
    back_to_previous.grid(row = 2, column = 0)
    close.grid(row = 2, column = 1)
    submit.grid(row =1 , column = 0)
def updateDatabase():
    print "Will Update Recipes in Recipe Database"
def destroyBothParentChild(c):
    print "Destroys both child and parent window"
def addNewRecipeDatabase():
    print "Adds New Recipe to Recipe Database"
def selectRecipes():
    print "Allow Recipe Selection"
def selectRandom():
    print "Randomly Selected Menu Appears!"
def updateExistingItem():
    print "Update Existing Data"
def addNewItem():
    print "Adds New Item to Database"


recipe = Tkinter.Button(app, text="Add New Recipe", width = 20, height = 10, command=editRecipes)
meal_plan = Tkinter.Button(app, text = "Make Meal Plan", width = 20, height = 10, command = makeMealPlan)
update_inventory = Tkinter.Button(app, text = "Update Inventory", width =20, height = 10, command = updateInventory)

recipe.grid(row = 0, column = 0)
meal_plan.grid(row = 0, column = 2)
update_inventory.grid(row = 1, column = 1)

app.mainloop()