import mainmenu
import patientmenu
import classes
import facility

#Displays the lab Menu
def displayLabMenu():
    print('')
    print("Laboratory Menu")
    print('')
    print(format("Selection", "10s"), format("Description", "0s"))
    print(format("=========", "10s"), format("===========", "14s"))
    print(format("    0", "10s"), format("Return to Main Menu", "13s"))
    print(format("    1", "10s"), format("Display laboratories List", "13s"))
    print(format("    2", "10s"), format("Add laboratory", "13s"))

#Gets new Laboratory object (with user-entered lab information) and adds it to the laboratories list
def addLabToList():
    labList.append(enterLaboratoryInfo())

#Displays all the Laboratory information in the laboratories list   
def displayLabsList():
    print("")
    print(format("Lab Name", "22s"), format("Cost"))
    print(format("========", "22s"), format("===="))
    for lab in labList:
        print(lab)
        
#Asks the user to enter lab name and cost, then creates and returns a Laboratory object
def enterLaboratoryInfo():
    name = input("Enter Lab Name: ")
    cost = input("Enter Lab Cost: ")
    lab = classes.Laboratory(name, cost)
    return lab

#Reads 'laboratories.txt file' into a list of Laboratory objects
def readLaboratoriesFile():
    l_list = []
    file = open('laboratories.txt')
    file.readline()
    for line in file:
        attributes = line.strip().split('_')
        lab = classes.Laboratory(attributes[0], attributes[1])
        l_list.append(lab)
    file.close()
    return l_list

#Writes “laboratories.txt” file from the list of Laboratory objects, maintaining correct formatting
def writeLabsListToFile():
    file = open('laboratories.txt', 'w')
    file.write("Lab Name_Cost")
    for lab in labList:
        file.write(classes.Laboratory.formatLaboratoryInfo(lab))
    file.close()

#Main function for this module is the labMenu
#Displays the menu and handles input
def labMenu():
    global labList
    
    #Creates a list of lab objects from the 'laboratories.txt' file
    labList = readLaboratoriesFile()
    while True:
        
        #Displays the menu
        displayLabMenu()
        answer = input("\nEnter selection: ")
        answer = facility.menuinputValidation(answer)
        match answer:
            #If 0 writes the list of labs back to the file and returns to the main menu
            case 0:
                writeLabsListToFile()
                print("\nReturning to main menu...")
                mainmenu.main()
            #If 1 shows a list of all lab objects
            case 1:
                displayLabsList()
            #If 2 it will ask for user input to add a new lab to the list
            case 2:
                addLabToList()
        
if __name__ == '__main__':
    labMenu()
