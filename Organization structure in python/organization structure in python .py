from tkinter import *



def functionalStructure():
    global TopManager
    global totalDepartments
    totalDepartments = IntVar(root)
    Label(root,text="Top Manager").place(x = 500, y = 30)
    TopManager = Entry(root)
    TopManager.place(x=580, y=30)
    show = Button(root, text="Show Structure", command=showFunctionalStructure)
    show.place(x=850, y=100)
    Button(root, text="Reset", command=dropMenu).place(x= 10,y=10)
    choices = {1, 2, 3, 4,5,6,7,8}
    totalDepartments.set("Number of Functional Departments")
    numOfDepartments = OptionMenu(root, totalDepartments, *choices)
    numOfDepartments.place(x=500, y= 50)
    EnterDepartments = Button(root, text="Enter Department Names", command=enterDepNames)
    EnterDepartments.place(x=100, y=120)

def enterDepNames():
    global depLst
    n = totalDepartments.get()
    depLst = []
    x = 270
    y = 90
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "Department "+a).place(x=x, y=y)
        depLst.append(Entry(root))
        depLst[i].place(x=x+80, y=y)
        y += 20


def showFunctionalStructure():
    root.title('Functional Structure')
    
    canvas = Canvas(root)   
    canvas.pack(expand=YES, fill=BOTH)
    size = 4 * len(TopManager.get())
    Label(canvas, text=TopManager.get(), fg='white', bg='black').place(x=663-size,y = 100)
    canvas.create_line(663,110,663,160)
    Button(root, text="Reset", command=dropMenu).place(x= 10,y=10)
    n = totalDepartments.get()
    if n == 1:
        xAxis = 663
        l = 0
    else:
        canvas.create_line(80,160,1266,160)
        l = 1186/(n-1)
        xAxis = 80
    for  i in range(0, n):
        size = 4 * len(depLst[i].get())
        canvas.create_line(xAxis,160,xAxis,220)
        Label(canvas, text=depLst[i].get(), fg='white', bg='black').place(x=xAxis-size,y = 220)
        canvas.create_line(xAxis,240,xAxis,320)
        Label(canvas, text=depLst[i].get()+" Manager", fg='white', bg='black').place(x=xAxis-size,y =320)
        canvas.create_line(xAxis,340,xAxis,420)
        Label(canvas, text=depLst[i].get()+" Assistant Manager", fg='white', bg='black').place(x=xAxis-size,y = 420)
        canvas.create_line(xAxis,440,xAxis,520)
        Label(canvas, text=depLst[i].get()+" Officer", fg='white', bg='black').place(x=xAxis-size,y = 520)
        xAxis += l

        
        
def enterDepNames1():
    global depLst1
    n = totalDepartments1.get()
    depLst1 = []
    x = 270
    y = 300
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "Department "+a).place(x=x, y=y)
        depLst1.append(Entry(root))
        depLst1[i].place(x=x+80, y=y)
        y += 20
        
def enterProductsName():
    global proLst
    n = totalProducts.get()
    proLst = []
    x = 270
    y = 90
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "Product "+a).place(x=x, y=y)
        proLst.append(Entry(root))
        proLst[i].place(x=x+80, y=y)
        y += 20
    
        



def productStructure():
    print ("productStructure")
    global TopManager
    global totalProducts
    global totalDepartments1
    totalDepartments1 = IntVar(root)
    totalProducts = IntVar(root)
    Label(root,text="Top Manager").place(x = 500, y = 30)
    TopManager = Entry(root)
    TopManager.place(x=580, y=30)
    show = Button(root, text="Show Structure", command=showProductStructure)
    show.place(x=850, y=100)
    Button(root, text="Reset", command=dropMenu).place(x= 10,y=10)
    choices1 = {1, 2, 3}
    totalProducts.set("Number of Products")
    numOfProducts = OptionMenu(root, totalProducts, *choices1)
    numOfProducts.place(x=500, y=50)
    EnterProducts = Button(root, text="Enter Products Names", command=enterProductsName)
    EnterProducts.place(x=100, y=120)
    choices2 = {1, 2}
    totalDepartments1.set("Number of Functional Departments")
    numOfDepartments1 = OptionMenu(root, totalDepartments1, *choices2)
    numOfDepartments1.place(x=500, y= 250)
    EnterDepartments1 = Button(root, text="Enter Department Names", command=enterDepNames1)
    EnterDepartments1.place(x=100, y=320)
            
def showProductStructure():
    root.title('Product Structure')
    canvas = Canvas(root)   
    canvas.pack(expand=YES, fill=BOTH)  
    size1 = 4 * len(TopManager.get())
    Label(canvas, text=TopManager.get(), fg='white', bg='black').place(x=663-size1,y = 100)
    canvas.create_line(663,110,663,160)
    Button(root, text="Reset", command=dropMenu).place(x= 10,y=10)
    n = totalDepartments1.get()
    m = totalProducts.get()
    if m == 1:
        xAxis1 = 663
        l = 0
    else:
        canvas.create_line(300,160,1066,160)
        l = 766/(m-1)
        xAxis1 = 300
    for i in range(0, m):
        size1 = 4 * len(proLst[i].get())
        canvas.create_line(xAxis1,160,xAxis1,220)
        Label(canvas, text=proLst[i].get(), fg='white', bg='black').place(x=xAxis1-size1,y = 220)
        canvas.create_line(xAxis1,230,xAxis1,290)
        if n == 1:
            xAxis = xAxis1
            c = 0
        else:
            canvas.create_line(xAxis1-150,290,xAxis1+100,290)
            c = 250/(n-1)
            xAxis = xAxis1-150
        for  i in range(0, n):
            size2 = 4 * len(depLst1[i].get())
            canvas.create_line(xAxis,290,xAxis,350)
            Label(canvas, text=depLst1[i].get(), fg='white', bg='black').place(x=xAxis-size2,y = 350)
            canvas.create_line(xAxis,360,xAxis,420)
            Label(canvas, text=depLst1[i].get()+" Manager", fg='white', bg='black').place(x=xAxis-size2,y =420)
            canvas.create_line(xAxis,430,xAxis,490)
            Label(canvas, text=depLst1[i].get()+" Assistant Manager", fg='white', bg='black').place(x=xAxis-size2,y = 490)
            canvas.create_line(xAxis,500,xAxis,560)
            Label(canvas, text=depLst1[i].get()+" Officer", fg='white', bg='black').place(x=xAxis-size2,y = 560)
            xAxis += c
        xAxis1 += l    

def mixStructure():
    print ("MixStructure")

def enterCountriesName():
    global conLst
    global cdLst
    n = totalCountries.get()
    conLst = []
    cdLst = []
    x = 270
    z = 540
    y = 90
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "Country "+a).place(x=x, y=y)
        conLst.append(Entry(root))
        conLst[i].place(x=x+80, y=y)
        Label(root,text= "City Director "+a).place(x=z, y=y)
        cdLst.append(Entry(root))
        cdLst[i].place(x=z+80, y=y)
        y += 20
    
def enterCitiesName():
    global depLst1
    global ciLst
    n = totalCities.get()
    depLst1 = []
    ciLst = []
    x = 540
    z = 270
    y = 300
    for i in range(0, n):
        a = str(i+1)
        Label(root,text= "City "+a).place(x=z, y=y)
        ciLst.append(Entry(root))
        ciLst[i].place(x=z+80, y=y)
        Label(root,text= "Department "+a).place(x=x, y=y)
        depLst1.append(Entry(root))
        depLst1[i].place(x=x+80, y=y)
        y += 20
    
    
def showDivisionalStructure():
    root.title('Divisional Structure')
    canvas = Canvas(root)   
    canvas.pack(expand=YES, fill=BOTH)  
    size1 = 4 * len(TopManager.get())
    Label(canvas, text=TopManager.get(), fg='white', bg='black').place(x=663-size1,y = 100)
    canvas.create_line(663,110,663,160)
    Button(root, text="Reset", command=dropMenu).place(x= 10,y=10)
    n = totalCities.get()
    m = totalCountries.get()
    if m == 1:
        xAxis1 = 663
        l = 0
    else:
        canvas.create_line(300,160,1066,160)
        l = 766/(m-1)
        xAxis1 = 300
    for i in range(0, m):
        size1 = 4 * len(conLst[i].get())
        canvas.create_line(xAxis1,160,xAxis1,220)
        Label(canvas, text=conLst[i].get(), fg='white', bg='black').place(x=xAxis1-size1,y = 220)
        canvas.create_line(xAxis1,230,xAxis1,290)
        size1 = 4 * len(cdLst[i].get())
        Label(canvas, text=cdLst[i].get(), fg='white', bg='black').place(x=xAxis1-size1,y = 290)
        canvas.create_line(xAxis1,300,xAxis1,350)
        if n == 1:
            xAxis = xAxis1
            c = 0
        else:
            canvas.create_line(xAxis1-150,350,xAxis1+100,350)
            c = 250/(n-1)
            xAxis = xAxis1-150
        for  i in range(0, n):
            size2 = 4 * len(ciLst[i].get())
            Label(canvas, text=ciLst[i].get(), fg='white', bg='black').place(x=xAxis-size2,y = 420)
            size2 = 4 * len(depLst1[i].get())
            canvas.create_line(xAxis,360,xAxis,420)
            Label(canvas, text=depLst1[i].get(), fg='white', bg='black').place(x=xAxis-size2,y = 490)
            canvas.create_line(xAxis,430,xAxis,490)
            Label(canvas, text=depLst1[i].get()+" Manager", fg='white', bg='black').place(x=xAxis-size2,y =560)
            canvas.create_line(xAxis,500,xAxis,560)
            Label(canvas, text=depLst1[i].get()+" Assistant Manager", fg='white', bg='black').place(x=xAxis-size2,y = 610)
            canvas.create_line(xAxis,570,xAxis,610)
            Label(canvas, text=depLst1[i].get()+" Officer", fg='white', bg='black').place(x=xAxis-size2,y = 660)
            xAxis += c
        xAxis1 += l 
    
def divisionalStructure():
    print ("MatrixStructure")
    
    global TopManager
    global totalCountries
    global totalCities
    totalCities = IntVar(root)
    totalCountries = IntVar(root)
    Label(root,text="Top Manager").place(x = 500, y = 30)
    TopManager = Entry(root)
    TopManager.place(x=580, y=30)
    show = Button(root, text="Show Structure", command=showDivisionalStructure)
    show.place(x=850, y=100)
    Button(root, text="Reset", command=dropMenu).place(x= 10,y=10)
    choices1 = {1, 2, 3}
    totalCountries.set("Number of Countries")
    numOfCountries = OptionMenu(root, totalCountries, *choices1)
    numOfCountries.place(x=500, y=50)
    EnterCountries = Button(root, text="Enter Countries Names", command=enterCountriesName)
    EnterCountries.place(x=100, y=120)
    choices2 = {1, 2}
    totalCities.set("Number of Cities")
    numOfCities = OptionMenu(root, totalCities, *choices2)
    numOfCities.place(x=500, y= 250)
    EnterCities = Button(root, text="Enter Cities Names", command=enterCitiesName)
    EnterCities.place(x=100, y=320)
       
        
def checkOption(*args):
    if structure.get() == "Functional Structure":
        functionalStructure()
    elif structure.get() == "Product Structure":
        productStructure()
    elif structure.get() == "Mix Structure":
        mixStructure()
    elif structure.get() == "Divisional Structure":
        divisionalStructure()        
        
def dropMenu():
    global root
    root = Tk()
    global structure
    totalDepartments = 0
    structure = StringVar(root)
    root.title('Fundamental')
    root.geometry('1366x768')
    listStructure = {"Functional Structure", "Product Structure", "Mix Structure", "Divisional Structure"}
    structure.set('Select the Structure')
    menu = OptionMenu(root, structure, *listStructure)
    structure.trace('w', checkOption)
    menu.place(x = 500,y=0)
    root.mainloop()
dropMenu()