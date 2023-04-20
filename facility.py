import mainmenu
import patientmenu
import classes

#function to display facility menu screen

def displayFacilityMenu():
    print('')
    print("Facility Menu")
    print('')
    print(format("Selection", "10s"), format("Description", "0s"))
    print(format("=========", "10s"), format("===========", "14s"))
    print(format("    0", "10s"), format("Return to Main Menu", "13s"))
    print(format("    1", "10s"), format("Display Facilities List", "13s"))
    print(format("    2", "10s"), format("Add Facility", "13s"))

    
#addFacilitytToList function that gets facility object 
#and adds it to the facility list.

def addFacilityToList():
    name = input("\nEnter Facility name: ")
    facility = classes.Facility(name)
    facilityList.append(facility)
    
#Reads 'facilities.txt file' into a list of the object
def readFacilitiesFile():
    f_list = []
    file = open('facilities.txt')
    file.readline()
    for line in file:
        attributes = line.rstrip('\n').split()
        facility = classes.Facility(attributes[0])
        f_list.append(facility)
    file.close()
    return f_list


#input validation function to check if input is a number and convert to int. If not will loop
#for new input.

def menuinputValidation(answer):
    while True:
        try:
            answer = int(answer)
            break
        except ValueError:
            print("It must be a number.")
            answer = input("> ")
    while answer not in range(0, 3):
        print("It must be between 0-2.")
        answer = input("> ")
        answer = menuinputValidation(answer)
    return answer

#Function that displays all the facility information(attributes) in the facility list

def displayFacilitiesList():
    print("")
    print(format("Facilities"))
    print(format("=========="))
    for facility in facilityList:
        print(facility)
        
#writeFacilityListToFile function that writes "facilities.txt" file from the list of objects
#maintaing correct formatting.

def writeFacilitiesListToFile():
    file = open('facilities.txt', 'w')
    file.write('Facilities:\n')
    for facility in facilityList:
        file.write(classes.Facility.formatFacilityInfo(facility))
    file.close()

#Function that displays the facility menu options and handles the choices.

def facilityMenu():
    global facilityList
    facilityList = readFacilitiesFile()
    while True:    
        displayFacilityMenu()
        answer = input("\nEnter selection: ")
        answer = menuinputValidation(answer)
        match answer:
            case 0:
                writeFacilitiesListToFile()
                print('\nReturning to main menu...')
                mainmenu.main()
            case 1:
                displayFacilitiesList()
            case 2:
                addFacilityToList()
    
if __name__ == '__main__':
    facilityMenu()
