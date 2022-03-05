# this program presents a menu and selects one of three options
# based on selection it either outputs, inputs, or quits
# author: Eleanor Sammon

# first function presents input options to user

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

# function that passes student name and puts with module as dict objects and adds them to list
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
    students.append(currentStudent)

# reads in the module information along with grade
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules

# outputting the information together (tabbed for neatness)
def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print("\t{}  \t{}".format(module["name"], module["grade"])) 


def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);


# main program
students = []
choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
        
        
# as a side note, my syntax had no colour in it but programme ran ok
# found it was because I hadn't saved my file as a .py extension
# once renamed the syntax coloured again! Much easier to work with